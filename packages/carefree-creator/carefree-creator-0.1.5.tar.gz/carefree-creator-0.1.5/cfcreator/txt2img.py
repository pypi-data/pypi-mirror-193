import time

from enum import Enum
from typing import Any
from fastapi import Response
from pydantic import Field
from cfclient.models import ImageModel

from .common import cleanup
from .common import init_sd_ms
from .common import get_sd_from
from .common import get_sd_inpainting
from .common import handle_diffusion_model
from .common import get_bytes_from_diffusion
from .common import IAlgorithm
from .common import Txt2ImgModel
from .common import CommonSDInpaintingModel
from .parameters import need_change_device


txt2img_sd_endpoint = "/txt2img/sd"
txt2img_sd_inpainting_endpoint = "/txt2img/sd.inpainting"
txt2img_sd_outpainting_endpoint = "/txt2img/sd.outpainting"


class Txt2ImgSDModel(Txt2ImgModel):
    w: int = Field(512, description="The desired output width.")
    h: int = Field(512, description="The desired output height.")


@IAlgorithm.auto_register()
class Txt2ImgSD(IAlgorithm):
    model_class = Txt2ImgSDModel

    endpoint = txt2img_sd_endpoint

    def initialize(self) -> None:
        self.ms = init_sd_ms()

    async def run(self, data: Txt2ImgSDModel, *args: Any) -> Response:
        self.log_endpoint(data)
        t0 = time.time()
        m = get_sd_from(self.ms, data)
        t1 = time.time()
        size = data.w, data.h
        kwargs = handle_diffusion_model(m, data)
        img_arr = m.txt2img(
            data.text,
            size=size,
            max_wh=data.max_wh,
            **kwargs,
        ).numpy()[0]
        content = get_bytes_from_diffusion(img_arr)
        t2 = time.time()
        cleanup(m)
        self.log_times(
            {
                "get_model": t1 - t0,
                "inference": t2 - t1,
                "cleanup": time.time() - t2,
            }
        )
        return Response(content=content, media_type="image/png")


class PaddingModes(str, Enum):
    CV2_NS = "cv2_ns"
    CV2_TELEA = "cv2_telea"


class Txt2ImgSDInpaintingModel(Txt2ImgModel, ImageModel, CommonSDInpaintingModel):
    mask_url: str = Field(
        ...,
        description="""
The `cdn` / `cos` url of the user's mask.
> `cos` url from `qcloud` is preferred.
> If empty string is provided, then we will use an empty mask, which means we will simply perform an image-to-image transform.  
""",
    )


class Txt2ImgSDOutpaintingModel(Txt2ImgModel, ImageModel, CommonSDInpaintingModel):
    pass


@IAlgorithm.auto_register()
class Txt2ImgSDInpainting(IAlgorithm):
    model_class = Txt2ImgSDInpaintingModel
    sd_inpainting_key = "$inpainting$"

    endpoint = txt2img_sd_inpainting_endpoint

    def initialize(self) -> None:
        self.ms = init_sd_ms()
        self.ms[self.sd_inpainting_key] = get_sd_inpainting()

    async def run(self, data: Txt2ImgSDInpaintingModel, *args: Any) -> Response:
        self.log_endpoint(data)
        t0 = time.time()
        image = await self.download_image_with_retry(data.url)
        mask = await self.download_image_with_retry(data.mask_url)
        m = self.ms[data.version if data.use_raw_inpainting else self.sd_inpainting_key]
        t1 = time.time()
        if need_change_device():
            m.to("cuda:0", use_half=True)
        t2 = time.time()
        kwargs = handle_diffusion_model(m, data)
        kwargs.update(await self.handle_diffusion_inpainting_model(data))
        img_arr = m.txt2img_inpainting(
            data.text,
            image,
            mask,
            anchor=64,
            max_wh=data.max_wh,
            keep_original=data.keep_original,
            **kwargs,
        ).numpy()[0]
        content = get_bytes_from_diffusion(img_arr)
        t3 = time.time()
        cleanup(m)
        self.log_times(
            {
                "download": t1 - t0,
                "get_model": t2 - t1,
                "inference": t3 - t2,
                "cleanup": time.time() - t3,
            }
        )
        return Response(content=content, media_type="image/png")


@IAlgorithm.auto_register()
class Txt2ImgSDOutpainting(IAlgorithm):
    model_class = Txt2ImgSDOutpaintingModel

    endpoint = txt2img_sd_outpainting_endpoint

    def initialize(self) -> None:
        self.m = get_sd_inpainting()

    async def run(self, data: Txt2ImgSDOutpaintingModel, *args: Any) -> Response:
        self.log_endpoint(data)
        t0 = time.time()
        image = await self.download_image_with_retry(data.url)
        t1 = time.time()
        if need_change_device():
            self.m.to("cuda:0", use_half=True)
        t2 = time.time()
        kwargs = handle_diffusion_model(self.m, data)
        kwargs.update(await self.handle_diffusion_inpainting_model(data))
        img_arr = self.m.outpainting(
            data.text,
            image,
            anchor=64,
            max_wh=data.max_wh,
            keep_original=data.keep_original,
            **kwargs,
        ).numpy()[0]
        content = get_bytes_from_diffusion(img_arr)
        t3 = time.time()
        cleanup(self.m)
        self.log_times(
            {
                "download": t1 - t0,
                "get_model": t2 - t1,
                "inference": t3 - t2,
                "cleanup": time.time() - t3,
            }
        )
        return Response(content=content, media_type="image/png")


__all__ = [
    "txt2img_sd_endpoint",
    "txt2img_sd_inpainting_endpoint",
    "txt2img_sd_outpainting_endpoint",
    "Txt2ImgSDModel",
    "Txt2ImgSDInpaintingModel",
    "Txt2ImgSDOutpaintingModel",
    "Txt2ImgSD",
    "Txt2ImgSDInpainting",
    "Txt2ImgSDOutpainting",
]

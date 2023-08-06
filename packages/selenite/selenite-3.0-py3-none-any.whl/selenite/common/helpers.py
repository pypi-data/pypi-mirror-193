from io import BytesIO

import ddddocr
from PIL import Image


def is_absolute_url(relative_or_absolute_url: str) -> bool:
    url = relative_or_absolute_url.lower()
    return (
            url.startswith('http:')
            or url.startswith('https:')
            or url.startswith('file:')
            or url.startswith('about:')
            or url.startswith('data:')
    )


def recognize_text_in_image(image_bytes: bytes) -> str:
    with Image.open(BytesIO(image_bytes)) as img:
        ocr = ddddocr.DdddOcr(show_ad=False)
        return (
            ocr.classification(img)
            or None
        )


def by_with_args(by: tuple, *args):
    by_, value = by
    return (
        by_,
        value.format(*args)
    )

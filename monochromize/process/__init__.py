from monochromize.process import processor


def monochromize(image: str) -> str:
    """画像をモノクロ化して保存し、そのパスを返す"""
    return processor.monochromize(image)

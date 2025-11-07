from pathlib import Path

from PIL import Image


def monochromize(image_path: str) -> str:
    """画像をモノクロ化して保存し、そのパスを返す"""
    # 画像を読み込む
    img = Image.open(image_path)

    # グレースケールに変換
    monochrome_img = img.convert("L")

    # 出力ファイルパスを生成
    path = Path(image_path)
    monochrome_image_path = str(path.parent / f"{path.stem}_monochrome{path.suffix}")

    # モノクロ画像を保存
    monochrome_img.save(monochrome_image_path)

    return monochrome_image_path

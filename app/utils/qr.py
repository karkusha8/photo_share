import qrcode
import os


def generate_qr(data: str, filename: str):
    os.makedirs("qr_codes", exist_ok=True)

    path = f"qr_codes/{filename}.png"

    img = qrcode.make(data)
    img.save(path)

    return path
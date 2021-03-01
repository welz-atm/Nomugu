from PIL import Image


def resize(pic):
    img = Image.open(pic)
    if img.height > 220 or img.weight > 220:
        output_size = (220, 220)
        img.thumbnail(output_size)
        img.save(pic.path)
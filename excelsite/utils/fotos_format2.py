import os
from pathlib import Path
from PIL import Image
import os.path


def format_w (img, width_to):
    width, height = img.size
    aspect = width / height
    width_to=int(width_to)
    height_to = round( width_to / aspect)
    img_formatted = img.resize((width_to, height_to), Image.ANTIALIAS);
    return img_formatted

def format_h (img, height_to):
    width, height = img.size
    aspect =round( width / height )
    height_to=int(height_to)
    width_to = round( height_to * aspect)
    img_formatted = img.resize((width_to, height_to), Image.ANTIALIAS);
    return img_formatted

def format_wh (img, width_to, height_to):
    width, height = img.size
    aspect = round(width / height)
    aspect_to = round( width_to / height_to)

    if  aspect>aspect_to:
        img_formatted = format_w (img, width_to)
        width_, height_ = img_formatted.size
        top =round( (height_ - height_to) / 2 )
        bottom =round( (height_ + height_to) / 2 )
        crop_rectangle = (0, top, width_to, bottom  )
        cropped_img = img_formatted.crop(crop_rectangle)

    if  aspect<=aspect_to:
        img_formatted = format_h (img, width_to)
        width_, height_ = img_formatted.size
        left = round((width_ - width_to) / 2)
        right = round((width_ + width_to) / 2)
        crop_rectangle = (left, 0, right, height_to)
        cropped_img = img_formatted.crop(crop_rectangle)

    return cropped_img


def go(media_paths, width_to, height_to):
    width_to = int(width_to)
    height_to = int (height_to)

    media_osn=media_paths['media_osn']
    media_dop= media_paths['media_dop']


    for  file in os.listdir(media_osn):
        file_path= Path(media_osn, file,  )
        img = Image.open(file_path)
        img_formatted=format_wh (img, width_to, height_to)

        # img_formatted.show()
        img_formatted.save(file_path)

    for file in os.listdir(media_dop):
        file_path = Path(media_dop, file, )
        img = Image.open(file_path)
        img_formatted = format_wh (img, width_to, height_to)

        # img_formatted.show()
        img_formatted.save(file_path)

    result = "Фото отформатированы по ширине и высоте"
    return result



















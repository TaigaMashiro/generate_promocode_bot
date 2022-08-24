from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
from moviepy.config import change_settings
from config import IM_PATH
import os


FONT_PATH = os.path.join(os.path.dirname(os.path.realpath('main.py')), 'data', 'font', "Montserrat-BlackItalic.ttf")
SAVE_PATH = os.path.join(os.path.dirname(os.path.realpath('main.py')), 'data', 'result')


# Если Windows то путь до IMAGEMAGICK
change_settings({"IMAGEMAGICK_BINARY": IM_PATH})


def create_image(image_path: str, coordinate: tuple, font_size: int, text: str, number: int, fill: str or int) -> str:
    """ Функция для создания изображения, которая возвращает в конце путь к созданному изображению """
    image = Image.open(image_path)
    drawer = ImageDraw.Draw(image)
    drawer.text(coordinate, text, font=ImageFont.truetype(FONT_PATH, font_size), fill=fill)
    image_name = f'{text}_{number}.png'
    image.save(os.path.join(SAVE_PATH, image_name))
    return os.path.join(SAVE_PATH, image_name)


def create_video(video_path: str, text: str, coordinate: list, font_size: int, duration: int) -> str:
    """ Функция для создания видео, которая возвращает в конце имя видеофайла """
    before_clip = VideoFileClip(video_path).subclip(coordinate[0], coordinate[1])
    clip = VideoFileClip(video_path).subclip(coordinate[2], coordinate[3])
    after_clip = VideoFileClip(video_path).subclip(coordinate[4], coordinate[5])
    clip = clip.volumex(1)

    input_text_on_clip = TextClip(text, font="Montserrat-BlackItalic.ttf", fontsize=55, color='red')
    input_text = input_text_on_clip.set_position(lambda t: ('center', font_size + t)).set_duration(duration)
    video = CompositeVideoClip([clip, input_text])
    full_video = concatenate_videoclips([before_clip, video, after_clip])
    full_video.write_videofile(text + ".mp4")
    return text

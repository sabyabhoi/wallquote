import argparse
import os
import glob
import random
import textwrap
import json
from PIL import Image, ImageDraw, ImageFont

class ImageModifier:
    def __init__(self):
        self.input_file = ""
        self.msg = "Do the hard work, even when you don\'t feel like it"
        self.output_file = "output.jpg"
        self.wallpaper_dir = ""

    def read_config_from_json(self, filepath):
        with open(filepath) as f:
            data = json.load(f)
            self.wallpaper_dir = data['wallpaper_dir']
            self.output_file = data['output_file']
            self.font = ImageFont.truetype(data['font'], 40)

    def exec_command(self):
        for f in [self.input_file, self.msg, self.output_file]:
            if len(f) == 0:
                raise ValueError("Either of inputfile, msg or outputfile params is \
                empty")
                return
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"{self.input_file} not found.")

        self.msg = '\n'.join(textwrap.wrap(self.msg, width=40))

        WIDTH, HEIGHT = 1920, 1080
        img = Image.open(self.input_file).resize((WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)
        x, y = WIDTH//2, HEIGHT//2
        draw.text((x - 5, y + 5), self.msg, (0, 0, 0), font=self.font, anchor='mm')
        draw.text((x, y), self.msg, fill=(255, 255, 255), font=self.font, anchor='mm')
        img.save(self.output_file)

    def get_random(self):
        imgs = glob.glob(self.wallpaper_dir + '*.*')
        self.input_file = random.choice(imgs)

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('inputfile')
        parser.add_argument('msg')
        parser.add_argument('outputfile')
        args = parser.parse_args()
        self.input_file = args.inputfile
        self.msg = args.msg
        self.output_file = args.outputfile

    def set_bg(self):
        self.get_random()
        self.exec_command()
        cmd = f'feh --bg-scale {self.output_file}'
        os.system(cmd)
    
if __name__ == '__main__':
    image_modifier = ImageModifier()
    image_modifier.read_config_from_json('config.json')
    image_modifier.set_bg()

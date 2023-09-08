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
            config = json.load(f)
            self.wallpaper_dir = config['wallpaper_dir']
            self.output_file = config['output_file']
            self.font = config['font']
            self.fontsize = config['fontsize']
            self.msg_file = config['msg_file']

    def exec_command(self):
        for f in [self.input_file, self.msg_file]:
            if not os.path.exists(f):
                raise FileNotFoundError(f"{f} not found")

        chosen = random.choice(list(open(self.msg_file)))
        self.msg = '\n'.join(textwrap.wrap(chosen, width=40))

        WIDTH, HEIGHT = 1920, 1080
        img = Image.open(self.input_file).resize((WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)
        x, y = WIDTH//2, HEIGHT//2
        fontObj = ImageFont.truetype(self.font, self.fontsize)
        draw.text((x + 5, y + 5), self.msg, (0, 0, 0), font=fontObj, anchor='mm')
        draw.text((x, y), self.msg, fill=(255, 255, 255), font=fontObj, anchor='mm')
        img = img.convert('RGB')
        img.save('/tmp/' + self.output_file)

    def get_random(self):
        imgs = glob.glob(self.wallpaper_dir + '*.png')
        self.input_file = random.choice(imgs)

    def set_bg(self):
        self.get_random()
        self.exec_command()
        cmd = f'feh --bg-scale /tmp/{self.output_file}'
        os.system(cmd)
    
if __name__ == '__main__':
    image_modifier = ImageModifier()
    image_modifier.read_config_from_json('/home/cognusboi/workspace/programming/python/wallpaper/config.json')
    image_modifier.set_bg()

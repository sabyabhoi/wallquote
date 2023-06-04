import argparse
import os
import glob
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont

class ImageModifier:
    def __init__(self):
        self.inputfile = ""
        self.msg = "Do the hard work, even when you don\'t feel like it"
        self.outputfile = "output.jpg"

    def exec_command(self):
        for f in [self.inputfile, self.msg, self.outputfile]:
            if len(f) == 0:
                raise ValueError("Either of inputfile, msg or outputfile params is \
                empty")
                return
        if not os.path.exists(self.inputfile):
            raise FileNotFoundError(f"{self.inputfile} not found.")

        self.msg = '\n'.join(textwrap.wrap(self.msg, width=40))

        font = ImageFont.truetype('/usr/share/fonts/TTF/RobotoMono-Bold.ttf', 40)

        img = Image.open(self.inputfile).resize((1920, 1080))
        draw = ImageDraw.Draw(img)
        x, y = 1920//2, 1080//2
        draw.text((x - 5, y + 5), self.msg, (0, 0, 0), font=font, anchor='mm')
        draw.text((x, y), self.msg, fill=(255, 255, 255), font=font, anchor='mm')
        img.show()

    def get_random(self, dir):
        imgs = glob.glob(dir + '*.jpg')
        self.inputfile = random.choice(imgs)

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('inputfile')
        parser.add_argument('msg')
        parser.add_argument('outputfile')
        args = parser.parse_args()
        self.inputfile = args.inputfile
        self.msg = args.msg
        self.outputfile = args.outputfile

    def set_bg(self):
        cmd = f'feh --bg-scale {self.outputfile}'
        os.system(cmd)
    
if __name__ == '__main__':
    image_modifier = ImageModifier()
    image_modifier.get_random('/home/cognusboi/workspace/userfiles/Media/Pictures/wallpapers/')
    image_modifier.exec_command()
#    image_modifier.set_bg()

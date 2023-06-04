import argparse
import os

class ImageModifier:
    def __init__(self):
        self.inputfile = "image.jpg"
        self.msg = "Hello sailor"
        self.outputfile = "output.jpg"

    def exec_command(self):
        font = '/home/cognusboi/.local/share/fonts/Spock/spockess_black.otf'

        for f in [self.inputfile, self.msg, self.outputfile]:
            if len(f) == 0:
                raise ValueError("Either of inputfile, msg or outputfile params is \
                empty")
                return
        if not os.path.exists(self.inputfile):
            raise FileNotFoundError(f"{self.inputfile} not found.")

        cmd = f'convert {self.inputfile} -gravity center -pointsize 200\
        -font {font}\
        -fill white -annotate +0+0 "{self.msg}" {self.outputfile}'
        os.system(cmd)
        

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('inputfile')
        parser.add_argument('msg')
        parser.add_argument('outputfile')
        args = parser.parse_args()
        self.inputfile = args.inputfile
        self.msg = args.msg
        self.outputfile = args.outputfile

    

if __name__ == '__main__':
    image_modifier = ImageModifier()
    image_modifier.exec_command()

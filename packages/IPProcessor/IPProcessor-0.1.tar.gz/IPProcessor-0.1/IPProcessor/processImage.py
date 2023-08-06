from PIL import Image, ImageOps, ImageDraw
import numpy as np
import math
import json

class ImageProcessor:
    """
    Process any image and replaces each color to it's more similar from a selected palette.
    
    Parameters:
    - Input : Input file.
    - Output : Output file.
    - Palette = 'low_grayscale' : Colour Palette, see get_palette for a list of available values.
    - Size = '' : Image Size, if no value is passed it will take it from the input file.
    - Inverted = False : Boolean that inverts image colors before processing.
    - Round Corners = False : Boolean that inserts.
    - Verbose = False : Boolean that specifies if print or not messages of the processing.

    Methods:
    - get_palettes() : Lists available colout palettes.
    - get_output() : Returns the file that has been produced.
    - set_[input|output|palette|size|inverted|rounded](new_value : string) : set any value from the Processor.
    - restart() : reset values so it can be reused.
    - start(input_file?: string, output_file?: string, colour_palette?: string, picture_size?: string, inverted?: bool, cropped?: bool, round_corners?: bool) : Process the preloaded image or take the values from the parameters to override.
    """
    def __init__(self, input_file : str = '', output_file : str = '', colour_palette : str = '', picture_size : str = '', inverted  : bool = False, round_corners : bool = False, verbose : bool = False):
        self.input = input_file
        self.output = output_file
        self.palette = colour_palette
        self.size = picture_size
        self.rounded = round_corners
        self.processed = False
        self.inverted = inverted
        self.verbose = verbose

    def __str__(self) -> str:
        if(self.processed):
            return f'The image has been written on {self.output}'
        elif(self.input == ''): 
            return 'Run Processor.start(<input_file>, <output_file>, <colour_palette>, <picture_size>) to process an image.'
        else:
            return f'Run Processor.start() to process the preloaded file {self.input}'
    
    def __repr__(self) -> str:
        return f'<Processor({self.input}, {self.output}, {self.palette}, {self.size}, {self.rounded}, {self.processed}, {self.inverted})>'

    def get_palettes(self):
        p_file = open('palettes.json')
        palettes = json.load(p_file)
        for x in list(palettes.keys()):
            print('- ', x)
        p_file.close()

    def set_input(self, new_input : str):
        if(self.verbose): print('Changing input value from ', self.input, ' to ', new_input)
        self.input = new_input

    def set_output(self, new_output : str):
        if(self.verbose): print('Changing output value from ', self.output, ' to ', new_output)
        self.output = new_output

    def set_palette(self, new_palette : str):
        if(self.verbose): print('Changing palette value from ', self.palette, ' to ', new_palette)
        self.palette = new_palette

    def set_size(self, new_size : str):
        if(self.verbose): print('Changing size value from ', self.size, ' to ', new_size)
        self.size = [int(x) for x in new_size.split('x')]

    def set_inverted(self, new_inverted : bool):
        if(self.verbose): print('Changing inverted value from ', self.inverted, ' to ', bool(new_inverted))
        self.size = bool(new_inverted)
        
    def set_rounded(self, new_rounded : bool):
        if(self.verbose): print('Changing inverted value from ', self.rounded, ' to ', bool(new_rounded))
        self.rounded = bool(new_rounded)
        
    def get_output(self):
        if(self.output != ''):
            try:
                o_file = open(self.output)
                return o_file
            except FileNotFoundError as e:
                if(self.verbose): print('No file has been produced. Run start to process a file.')
        elif(self.verbose):
            print('No file output has been specified.')
            

    def restart(self):
        self.input = ''
        self.output = ''
        self.palette = ''
        self.size = ''
        self.processed = False

    @staticmethod
    def add_corners(im, rad : int):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im

    def start(self, input_file : str = '', output_file : str = '', colour_palette : str = 'low_grayscale', picture_size : str = '', inverted : bool = False, cropped : bool = False, round_corners : bool = False):
        self.processed = False
        try:
            if(self.input == '' or self.output == ''):
                if(self.verbose): print("Input or Output were not specified at the moment of creation.")
                if(input_file == '' or output_file == ''):
                    raise Exception()
                else:
                    self.input = input_file
                    self.output = output_file
                    self.size = picture_size
                    self.palette = self.palette if self.palette != '' else colour_palette
                    self.inverted = self.inverted if self.inverted else inverted
                    self.rounded = self.rounded if self.rounded else round_corners
                    if(self.verbose): print(f"Taking values from method: {self.__repr__()},")

            p_file = open('palettes.json')
            palettes = json.load(p_file)

            if(self.size == ''):
                im = Image.open(self.input).convert('RGBA')
                input_width, input_height = im.size
                self.size = [input_width, input_height]
                if(self.verbose): print(f"Size was not specified. Using original size: {self.size}")
            else:
                im = Image.open(self.input).convert('RGB').resize(self.size)

            if self.inverted : 
                if(self.verbose): print("Inverting image...")
                im = ImageOps.invert(im)

            pixels = im.load()
            width, height = self.size

            new_image = np.zeros((width, height, 4), dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    if(self.verbose): print(f"Processing pixel({x}, {y})")
                    pixel_rgb = pixels[x,y]
                    results = []
                    r2, g2, b2, a2 = pixel_rgb
                    
                    if(a2 < 255):
                        new_image[x,y] = np.asarray((0, 0, 0, 0))
                    else:
                        for set in palettes[self.palette]:
                            r1, g1, b1 = set
                            distance = math.sqrt(math.pow(r2 - r1, 2) + math.pow(g2 - g1, 2) + math.pow(b2 - b1, 2))
                            results.append((set, distance))
                        results.sort(key=lambda e : e[1])
                        winner = results[0][0]
                        new_image[x,y] = np.asarray((winner[0], winner[1], winner[2], 255))

            nim = Image.fromarray(new_image)
            nim = nim.transpose(Image.Transpose.ROTATE_90)
            nim = ImageOps.flip(nim)
            if cropped:
                if(self.verbose): print("Cropping image...")
                nim = nim.crop((0 + cropped[0], 0 + cropped[1], width - cropped[2], height - cropped[3]))

            if self.rounded:
                if(self.verbose): print("Rounding image...")
                nim = self.add_corners(nim, 6)
                nim.save(self.output.replace('.jpg', '.png'), 'PNG')
            else:
                nim.save(self.output, 'PNG')
            
            if self.verbose: print('Image produced successfully.')

            p_file.close()
            self.processed = True
        except Exception as e:
            print(e)
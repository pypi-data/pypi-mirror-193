# Image Pixel Processor

Process any image and replaces each color to it's more similar from a selected palette.

Produces a PNG image.

## Dependencies

- Pillow
- NumPY

## Parameters:

- Input : Input file.
- Output : Output file.
- Palette = 'low_grayscale' : Colour Palette, see get_palette for a list of available values.
- Size = '' : Image Size, if no value is passed it will take it from the input file.
- Inverted = False : Boolean that inverts image colors before processing.
- Round Corners = False : Boolean that inserts.
- Verbose = False : Boolean that specifies if print or not messages of the processing.

## Methods:

- get_palettes() : Lists available colout palettes.
- get_output() : Returns the file that has been produced.
- set\_[input|output|palette|size|inverted|rounded](new_value : string) : set any value from the Processor.
- restart() : reset values so it can be reused.
- start(input_file?: string, output_file?: string, colour_palette?: string, picture_size?: string, inverted?: bool, cropped?: bool, round_corners?: bool) : Process the preloaded image or take the values from the parameters to override.

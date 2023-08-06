# epdlib v0.6

EpdLib provides functionality for creating and displaying scalable layouts that work with most of WaveShare's EPaper displays (EPD). The `Layout` module can also be used for generating flexible layouts for any screen-buffered display that does not require fast updates. 

EpdLib provides classes for interfacing with the screen (`Screen`), building layouts that will work at any resolution (`Layout`), and blocks that are used to assemble layouts (`Block`). EpdLib makes it trivial to build a project that will work on almost any WaveShare display without worrying about the resolution.

EpdLib supports all 1 bit displays*

## Changes

See the [ChangeLog](./changes.md) for details

### v0.6

* Add support for 8-Color WaveShare screens to Block, Screen and Layout
* All Blocks and Layouts now support "RGB" content
* Layouts and blocks can now be dynamically updated during runtime
* `Layout.layout` dictionaries must contain key `type` that matches the block type

### v0.5

* Add support for Block type "DrawBlock"
* Add support for adding borders to all Block types
* Add option to mirror output 
* `Screen()` handles kwargs 

### v0.4

* Add support for IT8951 panels with 8bit gray scale and partial refresh
    - Assigning EPD object to screen has changed from directy assignment to using a the string that corresponds to the name.

*****

## Dependencies

Python Modules:
* Pillow: System dependencies for Pillow:
    * libopenjp2-7
    * libtiff5
* RPi.GPIO
* spidev: ensure SPI is enabled on the pi
* waveshare-epd (Non IT8951 based panels): see [notes](#notes) below for installation instructions
    * this is for interacting with waveshare epaper displays and is not strictly needed to use the Block and Layout objects.
* IT8951 (IT8951 based panels): see [notes](#notes) below for installation instructions

*****

## Modules:

* [Block](#block-module) - image and text blocks that can be used to create a layout
* [Layout](#layout-module) - generate resolution agnostic layouts from Blocks
* [Screen](#screen-module) - simple interface for writing to WaveShare EPD devices

*****

## Block Module

`Block` objects are containers for text and images. `Block` objects are aware of their dimensions and can be made aware of their position within a larger layout.

*Class* `Block(area, hcenter=False, vcenter=False, rand=False, inverse=False, abs_coordinates=(0, 0), padding=0, border_config={})`

### Properties
        
Parent class for other types of blocks

### Args

 *  `area` (list/tuple): x and y integer values for dimensions of block area
 *  `hcenter` (bool): True: horizontally center contents [False]
 *  `vcenter` (bool): True: vertically center contents [False]
 *  `rand` (bool): True: randomly place contents in area [False]
 *  `inverse` (bool): True: invert pixel values [False]
 *  `abs_coordinates` (list/tuple): x, y integer coordinates of this block area
    within a larger image [(0, 0)]
 *  `padding` (int): number of pixels to pad around edge of contents [0]
 *  `fill` (int): 0-255 8 bit value for fill color for text/images [0 black]
 *  `bkground` (int): 0-255 8 bit value for background color [255 white]
 *  `mode` (str): '1': 1 bit color, 'L': 8 bit grayscale, 'RGB': (Red, Green, Blue) values ['1']
 *  `border_config`(dict): dictionary containing kwargs configuration for adding border to image see `help(add_border)`

#### Properties

 *  `image`: None - overridden in child classes'''

### Block Methods

#### `update(update)`

Place holder method for child classes used for updating the contents of the block.

### Block Functions

#### `add_border(img, fill, width, outline=None, outline_width=1, sides=['all'])`

Add a border around an image

##### Args

 * `img` (PIL.Image): image to add border to
 * `fill` (int): border fill color 0..255 8bit gray shade
 * `width` (int): number of pixels to use for border
 * `outline` (int): 0..255 8bit gray shade for outline of border region
 * `outline_width` (int): width in pixels of outline
 * `sides` (list of str): sides to add border: "all", "left", "right", "bottom", "top" 

Returns:
    PIL.Image

## Block.DrawBlock

Child class of `Block` that contains `pillow.ImageDraw` drawing objects. `DrawBlock` objects can contain ellipses, rounded_rectangles or rectangles. These are useful for creating horizontal and vertical rules and separators. DrawBlock objects can be aligned horizontally ('center', 'left', 'right' or vertically ('center', 'top', 'bottom') within the block area.

*Class* `Block.DrawBlock(area, *args, shape=None, abs_x=None, abs_y=None, scale_x=1, scale_y=1, halign='center', valign='center', draw_format={}, no_clip=True, **kwargs)`

`DrawBlock` objects that are fully initialized with `area` and `shape` will automatically generate an image. No further updates are necessary. When using `DrawBlock` in a `Layout` layout, it is not necessary to send an update when the block is refreshed unless the properties have been changed. The generated image will remain in memory until the program is terminated.

### Properties       

 * `area` (tuple of int): area of block in pixels
 * `shape` (str): shape to draw (see DrawBlock.list_shapes())
 * `abs_x` (int): absolute x dimension in pixels of drawing (overrides scale_x)
 * `abs_y` (int): absolute y dimension in pixels of drawing (overrides scale_y)
 * `scale_x` (float): percentage of total x area (0..1) (abs_x overrides)
 * `scale_y` (float): percentage of total y area (0..1) (abs_y overrides)
 * `halign` (str): horizontal alignment of drawing; 'center', 'left', 'right' 
 * `valign` (str): vertical alignment of drawing; 'center', 'top', 'bottom'
 * `draw_format` (dict): dict of kwargs for shape drawing function
 * `no_clip` (bool): when True fit shapes completely within area
 * `image` (PIL:Image): rendered shape
 
###  Methods

#### `list_shapes()`

Static method: list supported shapes that can be drawn

##### Args

* None

#### `draw_help()`

Static method: print the docstring for the currently set shape

##### Args

* None

#### `update(update=True)`

Update the image. This is **only** necessary if the object properties have been changed or the object was not created with a `shape` property.

##### Args

* `update` (bool) True forces update of image

#### `draw_image()` 

Update the image using the selected drawing function and `draw_format` property

#### Args

* None

#### Returns

* None
  

## Block.TextBlock
Child class of `Block` that contains formatted text. `TextBlock` objects can do basic formatting of strings. Text is always rendered as a 1 bit image (black on white or white on black). Text can be horizontally justified and centered and vertically centered within the area of the block. 

All properties of the parent class are inherited.

*Class* `Block.TextBlock(font, area, text='NONE', font_size=0, max_lines=1, maxchar=None, chardist=None)`

`TextBlock` objects will attempt to calculate the appropriate number of characters to render on each line given an area, font face and character distribution. Each font face renders characters at a different width and each TTF character uses a different X width (excluding fixed-width fonts). 

### Properties

* `font` (str): path to TTF font face - relative paths are acceptable
* `area` (2-tuple of int): area of block in pixles - required
* `text` (str): string to format 
    - Default: 'NONE'
* `font_size` (int): font size in points
    - Default: 0
* `max_lines` (int): maximum number of lines to use when wrapping text
    - Default: 1
* `maxchar` (int): maximum number of characters to fit on a line
    - if set to `None`, the text block will calculate this value based on the font face and specified `chardist`
    - Default: None
* `chardist` (dict): statistical character distribution for a supported language to use for a specified font
    - dictionary of letter and float representing fractional distribution (see `print_chardist`)
* `image` (PIL.Image): resultant image generated of formatted text
*  `align` (str): 'left', 'right', 'center' justify text (default: left)

### Functions

* `print_chardist(chardist=None)` - print supported character distributions
    - chardist (str): `chardist='USA_CHARDIST'` print the character distribution for USA English

### Methods

#### `update(update=None)`

Update the text string with a new string and sets `image` property

#### Args

* `update` (str): string to display

## Block.ImageBlock

Child class of `Block` that contains formated images. `ImageBlock` objects do basic formatting of color, centering and scaling. All `ImageBlock` images are 8 bit grayscale `Pillow.Image(mode='L')`. Images that are too large for the area are rescaled using the `Pillow.Image.thumbnail()` strategies to limit distortion. Images that are smaller than the set area will **not** be resized.

All properties of the parent class are inherited.

*Class* `Block.ImageBlock(area, image=None)`

### Properties

* `image` (:obj:PIL.Image or :obj:str) - `Pillow` image or path provided as a `str` to an image file; relative paths are acceptable
* `remove_alpha(bool)`: true: remove alpha chanel of PNG or similar files; see: https://stackoverflow.com/a/35859141/5530152

### Methods

#### `update(update=None)`

Update the image with a new image and sets `image` property

##### Args

* `update` (image) image to display

#### Returns

* Tru on success

#### `remove_transparency(im, bg_colour=(255, 255, 255))` 

Static method: remove transparency from PNG and similar images

##### Args

* `im` (PIL image) image to process
* `bg_color` (background) color to replace alpha/transparency

*****

## Layout Module

`Layout` objects support scaling images and dynamically scaling [TTF](https://en.wikipedia.org/wiki/TrueType) font-size for different screen sizes. 

Font sizes are set based on each individual font and scaled to fit within text blocks using the maximum number of lines specified in the layout. Text is line-broken using the python [textwrap logic](https://docs.python.org/3.7/library/textwrap.html).

epdlib `Layout` objects can be scaled to any (reasonable) resolution while maintaining internally consistent ratios.

**500x500 Layout**

![500x500 weather image](./docs/weather_5x5.png)

**300x200 Layout**
![300x200 weather_image](./docs/weather_3x2.png)

*Class* `Layout(resolution, layout=None, force_onebit=False, mode='1')`

### Properties

* `resolution` (2-tuple of int): resolution of the entire screen in pixels
* `blocks` (dict): dictionary containing of configured `Block` objects
* `layout` (dict): dictionary containing layout parameters for each block
    - sets blocks property
    - see example below in the [Quick-Start Recipes](#quick-start-recipes) section
* `image` (Pil.Image): concatination of all blocks into single image
* `force_onebit` (bool): force all blocks within a layout to `mode='1'`
* `mode` (str): PIL image mode to use for generating the image
    - supports `'1'` 1 Bit, `'L'` 8 bit Gray, `'RGB'`: 8 Color RGB 

### Methods

#### `concat()`

Join all blocks into a single image and sets `image` property

##### Args

* None

##### Returns

* `PIL.Image`

#### `update_block_props(block, props={}, force_recalc=False)`

Update the properties of a block. TextBlocks will always be recalculated to ensure the current font settings are still valid. NB! The contents must be updated using `update_contents` for the updated properties to be reflected in the `image` property.

##### Args

*  `block` (str): name of existing block
* `props` (dict): dictionary of properties to update in the block
* `force_recalc` (bool): force the recalculation fo all blocks. Use this if the positioning, size or resolution changes.

##### Returns

* None

#### `update_contents(updates=None)`

Update the contents of each block

##### Args

* `updates` (dict): dictionary in the format `{'text_section_A': 'text to use', 'image_section_B': '/path/to/img', 'pil_img_section': PIL.Image}`

*********

## Screen Module

`Screen` objects provide a method for waking and writing to a WaveShare E-Paper Display (EPD). `Screen` objects are aware of their resolution and when they were last updated (stored in monotonic time). 

*Class* `Screen(resolution=None, epd=None)`

### Properties

* `resolution` (list): X x Y pixels
* `clear_args` (dict): kwargs dict of any additional kwargs that are needed for clearing a display
* `buffer_no_image` (PIL:Image): "blank" image for clearing bi-color panels (empty for all others)
* `vcom (float): negative vcom voltage from panel ribon cable
* `HD` (bool): True for IT8951 panels
* `rotation` (int): rotation of screen (0, -90, 90, 180)
* `mirror` (bool): mirror the output 
* `update` (obj:Update): monotoic time aware update timer

**NOTE**

Screens with cable along long edge
``` text
Rotation = 0
  ┌───────────────┐
  │          (__) │
  │  `\------(oo) │
  │    ||    (__) │
  │    ||w--||    │
  └─────┬───┬─────┘
        │|||│

Rotation = 180
        │|||│
  ┌─────┴───┴─────┐
  │          (__) │
  │  `\------(oo) │
  │    ||    (__) │
  │    ||w--||    │
  └───────────────┘

```

Screens with cable along short edge
```text
Rotation = 0
  ┌───────────────┐
  │          (__) ├──
  │  `\------(oo) │--
  │    ||    (__) │--
  │    ||w--||    ├──
  └───────────────┘

Rotation = 180
  ┌───────────────┐
──┤          (__) │
--│  `\------(oo) │
--│    ||    (__) │
──┤    ||w--||    │
  └───────────────┘

```


### Screen Methods

#### `blank_image():` 

Return a blank PIL.Image in of `mode` type of `resolution` dimensions.

##### Args

* None


#### `clearEPD()`

Send the clear signal to the EPD to wipe all contents and set to "white" that is appropriate for configured EPD.

##### Args

* None

##### Returns

* None

#### `colors2palette(colors=constants.COLORS_7, num_colors=256)`

Static method to generate a palette that can be used in reducing an image to a fixed set of colors


#### `intiEPD()`

Initializes the EPD for writing (deprecated and no longer functional). This is now handled automatically by the class to ensure that SPI file handles are opened and closed properly. There is no need to init the EPD under normal circumstances.

For non HD (IT8951) displays, use `epd.init()` to manually init the screen. It is imperative to track `init()` calls and close the SPI file handles with `epd.sleep()`. Failure to do this will result in long-running jobs to fail due to running out of SPI file handles.

##### Args

* None

##### Returns

* None

#### `list_compatible_modules()`

Static method to print a list of all waveshare_epd panels that are compatible with epdlib

##### Args

* None

##### Returns

* None

####  `reduce_palette(image, palette, dither=False)`

Reduce an image to a fixed palette of colors. This method creates a posterized version of the original image forcing all colors to set colors. This is useful for matching the supported colors of an EPD.

##### Args

* `image`: `PIL.Image` image to be reduced
* `palette`: `list` of RGB color values - this is a flat list, not a list of lists or tuples
    - Use `colors2palette()` to generate an appropriate list
* `dither`: `bool` True: creates a dithered image, False creates color fields

##### Returns

* `PIL.Image`

##### Example

```Python
# create reduced palette images 
import Screen
from PIL import Image
# create screen object
s = Screen(epd='epd5in65f')
# load image
image = Image.Open('./images/portrait-pilot_SW0YN0Z5T0.jpg')
image.thumbnail(s.resolution)
# create color palette
color_palette = s.colors2palette()
# create image with solid color fields and reduced palette
posterized = s.reduce_palette(image=image, palette=color_palette, dither=False)
# create image with dithered color fields and reduced palette
dithered = s.reduce_palette(image=image, palette=color_palette, dither=True)
```
Sample Images

![Posterized Image](./images/portrait-pilot_posterized.png)
![Dithered Image](./images/portrait-pilot_dithered.png)

#### `writeEPD(image, sleep=True, partial=False)`

Write `image` to the EPD and resets the monotonic `update` timer property.

##### Args

* `image`:`PIL.Image` object that matches the resolution of the screen
* `sleep`: `bool` put the display to low power mode (deprecated and no longer has any function)
* `partial`: `bool` update only changed portions of the screen (faster, but only works with black and white pixels) (default: False) on HD screens

##### Returns 

* True on success

###### Example
```Python
from Screen import Screen
import waveshare_epd
myScreen = Screen()
myScreen.epd = "epd5in83"
myScreen.initEPD()
myScreen.writeEPD('./my_image.png')
```


## Screen.Update

Create a monotonically aware object that records the passage of time.

*Class* `Screen.Update()`

### Properties

* `age` (float): age in seconds since creation
* `now` (float): time in [CLOCK_MONOTONIC](https://linux.die.net/man/3/clock_gettime) time
* `last_updated` (float): time in seconds since last updated
* `update` (bool): True - trigger resets last_updated time

### Methods

* `update(update=True)` - reset last_updated timer to zero

### Example

```Python
import Screen
u = Update()
u.now
>>> 357147.118559987
u.age
>>> 37.449310125026386
u.last_updated
>>> 62.2587232599617
u.update = True
u.last_updated
>>> 0.00021347898291423917
```

## Screen.ScreenShot
Capture a rolling set of screenshots. When the total number of screenshots exceeds `n` the oldest is deleted. Images are stored as .png.

This is useful for debugging over time.

*Class* `Screen.ScreenShot(path='./', n=2, prefix=None)`

### Properties
* `total` (int): total number of screenshots to keep
* `prefix` (str): prefix to add to filenames
* `time` (str): time in format: %y-%m-%d_%H%M.%S - 2020-02-29_1456.39
* `img_array` (list): list of files stored in `path`

### Methods
* `delete(img)`: delete `img` file
* `save(img)`: save `img` to `path`
    - img: PIL.Image
```
import Screen
scrnShot = Screen.ScreenShot(path='/temp/', n=20)
spam = PIL.Image.new(mode='L', size=(100, 100), color=0)
scrnShot.save(spam)
```

## Quick-Start Recipes
### Quick Demo
The demo creates a very basic layout and displays some text in four orientations. This is an easy way to test your panel and confirm that it is working properly.

`python3 -m epdlib.Screen`

### Creating an Image from a Layout
The following recipe will produce the a layout for a 500x300 pixel display. This image can be passed directly to a WaveShare e-Paper display for writing.
![500x300 layout example](./docs/layout_example.png)

```Python
## Sample Layout ##
import epdlib

# create the layout object - adjust the resolution to match the display area
layout_obj = epdlib.Layout(resolution=(500, 300))

l = { # basic two row layout
    'tux_img': {                
            'type': 'ImageBlock',        # required as of v0.6
            'image': True,               # image block
            'padding': 10,               # pixels to padd around edge
            'width': .25,                # 1/4 of the entire width
            'height': 1/4,               # 1/4 of the entire height
            'abs_coordinates': (0, 0),   # this block is the key block that all other blocks will be defined in terms of
            'hcenter': True,             # horizontally center image
            'vcenter': True,             # vertically center image
            'relative': False,           # this block is not relative to any other. It has an ABSOLUTE position (0, 0)
            'mode': 'RGB',              # treat this image as an RGB image 
                                        # note this will be converted to 8bit gray or ('L')
                                        # 1 bit black/white ('1') if the screen does not support 
                                        # color output
        },
    'vertical_rule_1' :{
            'type': 'DrawBlock',         # required as of v0.6
            'shape': 'rounded_rectangle',# shape to draw
            'abs_x': 5,                  # absolute x dimension of shape in pixels
            'scale_y': .8,               # scale shape so it is 80% of available area
            'halign': 'center',          # horizontally center in area
            'valign': 'center',          # vertically center in area
            'draw_format': {'radius': 5, # any key word args (kwargs) needed for formatting the shpae
                            'outline': 128,
                            'width': 2},
            'height': 1/4,
            'width': .02,
            'abs_coordinates': (None, 0), # x value will be calculated from the 'tux_image' block, the y value is "0"
            'relative': ['tux_img', 'vertical_rule_1'] # use 'tux_image' X value, use 'vertical_rule_1' for Y value
    },
    'pangram_a': { 
            'type': 'TextBlock',          # required as ov v0.6
            'image': None,                # set to None if this is a text block
            'max_lines': 3,               # maximum lines of text to use when wrapping text
            'padding': 10,                # padding around all edges (in pixles)
            'width': .73,                 # proportion of the entire width
            'height': 1/4,                # proprtion of the entire height
            'abs_coordinates': (None, 0), # absolute coordinates within the final image (use None for those
                                          # coordinates that are relative to other blocks and will be calculated
            'hcenter': False,             # horizontal-center the text and the resulting image
            'vcenter': True,              # vertically-center the text within the block
            'relative': ['vertical_rule_1', 'pangram_a'], # blocks to which THIS block's coordinates are relative to
                                                        # -- in this case X: `weather_img` and Y: `temperature`
                                                        # the width of the block `weather` will be used to
                                                        # to calculate the X value of this block and the Y value
                                                        # specified within the `temperature` block will be used 
            'font': './fonts/Open_Sans/OpenSans-Regular.ttf', # TTF Font face to use; relative paths are OK
            'font_size': None,             # set this to None to automatically scale the font to the size of the block
            'mode': 'L'                    # set text blocks to "mode": L" to enable anti-aliasing on HD screens (automatically disabled on non HD)
    },
    'pangram_b': { 
                'type': 'TextBlock',
                'image': None,
                'max_lines': 3,
                'padding': 8,
                'width': 1,
                'height': 1/4,
                'abs_coordinates': (0, None),
                'hcenter': True,
                'vcenter': True,
                'relative': ['pangram_b', 'tux_img'],
                'font': './fonts/Open_Sans/OpenSans-Regular.ttf',
                'font_size': None,
                'inverse': False,
                'mode': 'L',
                'border_config': {'fill': 0, # add a border to the top and bottom of this text block
                                  'width': 3,
                                  'sides': ['top', 'bottom']}
    },
    'pangram_c': {
                'type': 'TextBlock',
                'image': None,
                'max_lines': 2,
                'padding': 0,
                'width': 1,
                'height': 1/4,
                'abs_coordinates': (0, None),
                'hcenter': True,
                'vcenter': True,
                'relative': ['pangram_c', 'pangram_b'],
                'font': './fonts/Open_Sans/OpenSans-BoldItalic.ttf',
                'font_size': None,
                'inverse': False,
                'mode': 'L'
    },    
    'text': {
                'type': 'TextBlock',
                'image': None,
                'max_lines': 4,
                'padding': 10,
                'width': 1,
                'height': 1/4,
                'abs_coordinates': (0, None),
                'hcenter': True,
                'vcenter': True,
                'relative': ['text', 'pangram_c'],
                'font': './fonts/Open_Sans/OpenSans-Regular.ttf',
                'font_size': None,
                'inverse': True
    }

}

# apply the layout instructions to the layout object
layout_obj.layout = l

# create a dictionary with the values that will be pushed to each block
# note that is is not necessary to update the DrawBlocks if they are fully configured
update = {
    'tux_img': './images/tux.png',      
    'pangram_a': 'The quick brown fox jumps over the lazy dog.',  
    'pangram_b': 'Pack my box with five jugs of liquor. This block has a top & bottom border',          
    'pangram_c': 'Jackdaws love my big sphinx of quartz.',                    
    'text': 'A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once. This text is not anti-aliased.'}


# update the layout with the data in the dictionary and send each item to the proper block
layout_obj.update_contents(update)

# join all the sub images into one complete image
myImg = layout_obj.concat()
# write the image out to a file
myImg.save('sample.jpg')

# update a the properties of a block
layout_obj.update_block_props(block-'tux_img', props={'inverse': True})

# after an update, the block needs to be updated again
update = {
    'tux_img': './images/tux.png'
    }

updateImg = layout_obj.concat()
updateImg.save('updateSAmple.jpg')
```



### Write an image to a Screen
The following code will create an interface for writing images to the EPD
*Requirements*
* Waveshare EPD module or IT8951 library (see [Notes](#Notes) below)

```Python
from epdlib import Screen
from PIL import Image
## non IT8951 screens
my_epd = "epd2in7" 
my_vcom = None
## IT8951 screens
# my_epd = "HD"
# my_vcom = -1.8

# create screen object
my_screen = Screen(epd=my_epd, vcom=my_vcom)

my_resolution = my_screen.resolution

# open image, convert to 1 bit and scale
my_img = Image.open('path/to/image.jpg')
my_img = my_img.convert("1")
my_img.thumbail(my_resolution)

# write image to screen
my_screen.writeEPD(my_img)

# clear screen
my_screen.clearEPD()
```

## Notes

### WaveShare non-IT8951 Screens

The waveshare-epd library is required for non-IT8951 screens and can be installed from the Git repo:

```Shell
pip install -e "git+https://github.com/waveshare/e-Paper.git#egg=waveshare_epd&subdirectory=RaspberryPi_JetsonNano/python"
```

### IT8951 basee Screens

[Greg D Meyer's IT8951 library](https://github.com/GregDMeyer/IT8951) is required and can be installed from the Git repo:

```Shell
pip install -e "git+https://github.com/GregDMeyer/IT8951#egg=IT8951"
```


getting ready for pypi:
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56



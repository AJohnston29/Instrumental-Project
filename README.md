# Conversion.py

Conversion.py is an image transformation library written in Python. The library currently supports two functions:

1. Convert an image to grayscale
2. Apply a blur filter to an RGB image

**Table of Contents:**

1. [Dependencies](#dependencies)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Additional Notes](#notes)
5. [How to Get Help](#how-to-get-help)
6. [The Author](#author)

## Dependencies

The following Python modules are required by Conversion.py:

* numpy
* scipy
* Image (Pillow)
* argparse

These dependencies can be installed using `pip`:

```
pip install pillow numpy scipy argparse
```

If python cannot find the pillow module, try:

```
sudo python -m pip install pillow numpy scipy argparse
```

## Usage

Conversion.py is a python script that must be invoked from the command line.

The user must specify an image and transformation as command line arguments, and the transformed image will be saved as an output in the same folder as the script, unless specified otherwise.

```
./conversion.py -i IMAGE -g -b PASSES -o FILEPATH

Applies the specified transformations to the input image. The input image will not be modified.

The output image will be saved in the same location as the input image. The filename will include the transformation that was applied.

* -i IMAGE or --image IMAGE - path to the image to transform.
* -b PASSES or --blur PASSES - Blur an RGB image, with 0-5 passes for desired intensity.
* -g or --grayscale - Convert an image from RGB to grayscale.
* -o FILEPATH or --output FILEPATH - Designate a specific filepath or name and extension type for the output file.
```

Note: The blur function can only take in an RGB image. In addition, while each pass will increase the intensity of the blur, it will significantly slow down the function. For this reason, the number of passes is limited to 5. 

## Examples

Two sample images are included in the `samples/` directory and will be used in the code snippets below.

The following will convert `Racoon.jpg` to grayscale and will output in the directory with conversion.py as `Racoon_gray.jpg`:

```
./conversion.py -i samples/Racoon.jpg -g
```

The following will convert `Racoon.jpg` to grayscale and output back in the `samples/` directory as `RG.png`:

```
./conversion.py -i samples/Racoon.jpg -g -o samples/RG.png
```

The following will apply a blur filter with 3 passes to `flower.jpg` and will output in the directory with conversion.py:

```
./conversion.py -i samples/flower.jpg -b 3
```

The following will apply both grayscale and blur (with 5 passes) filters to `flower.jpg` and will output into `samples/` as: `FGB.jpg`

```
./conversion.py - samples/flower.jpg -g -b 5 -o samples/FGB.jpg
```

## How to Get Help

Have a question? Run into a problem? Feel free to [send me an email](anthondj@usc.edu) or file a GitHub issue and I will respond within one business day.

## The Author

This script was created by Anthony Johnston.

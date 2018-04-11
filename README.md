# Conversion.py

Conversion.py is an image transformation library written in Python. The library currently supports two functions:

1. Convert an image to grayscale
2. Apply a blur filter to an image

**Table of Contents:**

1. [Dependencies](#dependencies)
2. [Usage](#usage)
3. [Examples](#examples)
4. [How to Get Help](#how-to-get-help)
5. [The Author](#author)

## Dependencies

The following Python modules are required by Conversion.py:

* numpy
* scipy
* Image (Pillow)

These dependencies can be installed using `pip`:

```
pip install pillow numpy scipy
```

If python cannot find the pillow module, try:

```
sudo python -m pip install pillow numpy scipy
```

## Usage

Conversion.py is a python script that must be invoked from the command line.

The user must specify an image and transformation as system arguments, and the transformed image will be saved as an output in the same folder.

```
./conversion.py <image> <transformation 1>

Applies the specified transformations to the input image. The input image will not be modified.

The output image will be saved in the same location as the input image. The filename will include the transformation that was applied.

* image - path to the image to transform.
* transformations - can be one of three:
	* blur - apply a blur filter to the image
	* grayscale - convert image from RGB to grayscale
	* both - apply both blur and grayscale filters
```

## Examples

Two sample images are included in the `samples/` directory and will be used in the code snippets below.

The following will convert `Racoon.jpg` to grayscale:

```
./conversion.py samples/Racoon.jpg grayscale
```

The following will apply a blur filter to `flower.py`:

```
./conversion.py samples/flower.py blur
```

The following will apply both grayscale and blur filters to `flower.py`:

```
./conversion.py samples/flower.py both
```

## How to Get Help

Have a question? Run into a problem? Feel free to [send me an email](anthondj@usc.edu) and I will respond within one business day.

## The Author

This script was created by Anthony Johnston.

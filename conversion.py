#!/usr/bin/python
#Script created by Anthony Johnston
import os
import sys
import argparse
from scipy import misc
import numpy as np
from PIL import Image

#RGB to Grayscale Conversion Function
def GrayScale(filename):

	#Defines the weighted average formula for luminosity
	def LuminosityMethod(pixel):
		return 0.21*(pixel[0])+0.72*(pixel[1])+ 0.07*(pixel[2])

	#Parse through every pixel in the image and run it through the formula
	gray = np.zeros(filename.shape[0:-1])
	for row in range(len(filename)):
		for col in range(len(filename[row])):
			gray[row][col] = LuminosityMethod(filename[row][col])

	#Pass grayscaled image back to main
	return gray


def Blur(filename, passes):
	imgarray = np.asarray(filename)
	
	#Pixel radius of blur
	radius = 2

	#Sets window length of blur in respect to individual pixels
	#In this case, length will be set to 5
	wlen = (radius*2)+1
	#Defines height and width of image array

	height = imgarray.shape[0] #Rows (Y-Variable)
	width = imgarray.shape[1] #Columns (X-Variable)

	def ApplyBlur(imgarray):
		#Creates two temporary arrays for image, based on dimensions
		tempA = np.zeros((height, width, 3), np.uint8)
		tempB = np.zeros((height, width, 3), np.uint8)

		#Blur Horizontally, row by row
		for row in range(height):
			#RGB color values for a white pixel blur
			R = 0
			G = 0
			B = 0

			#Find blurred value for first pixel in the row
			for rads in range(-radius, radius+1):
				if (rads) >= 0 and (rads) <= width-1:
					R += imgarray[row, rads][0]/wlen
					G += imgarray[row, rads][1]/wlen
					B += imgarray[row, rads][2]/wlen
			tempA[row,0] = [R,G,B]

			#Find blurred value for the rest of the pixels in every row
			#The blur value depends on an unweighted mean and a sliding window
			#The sliding window adds incoming pixels and subtracts outgoing pixels
			#incoming pixel -> pixel to right
			#outgoing pixel -> pixel to left
			for col in range(1, width):
				if (col-radius-1) >= 0:
					R -= imgarray[row, col-radius-1][0]/wlen
					G -= imgarray[row, col-radius-1][1]/wlen
					B -= imgarray[row, col-radius-1][2]/wlen
				if (col+radius <=width-1):
					R += imgarray[row, col+radius][0]/wlen
					G += imgarray[row, col+radius][1]/wlen
					B += imgarray[row, col+radius][2]/wlen

				#Puts final mean value into pixel in Temp  A
				tempA[row, col] = [R,G,B]

		#Time to repeat the exact same process
		#But Verically, column by column
		for col in range(width):
			R = 0
			G = 0
			B = 0

			for rads in range(-radius, radius+1):
				if (rads) >= 0 and (rads) <= height-1:
					R += tempA[rads, col][0]/wlen
					G += tempA[rads, col][1]/wlen
					B += tempA[rads, col][2]/wlen
			tempB[0, col] = [R,G,B]

			for row in range(1,height):
				if (row-radius-1) >= 0:
					R -= tempA[row-radius-1,col][0]/wlen
					G -= tempA[row-radius-1,col][1]/wlen
					B -= tempA[row-radius-1,col][2]/wlen
				if (row+radius)<=height-1:
					R += tempA[row+radius, col][0]/wlen
					G += tempA[row+radius, col][1]/wlen
					B += tempA[row+radius, col][2]/wlen

				tempB[row,col] = [R,G,B]

		return tempB

	#Time to step through the array multiple times
	#For each pass across the entire array, the amount of blur will increase
	#For this case, it will pass through 3 times
	#Another temp array to hold values from each pass
	tempC = imgarray
	for k in range(passes):
		#Limits # of passes to 6, for speed 
		if k < 6:
			tempC = ApplyBlur(tempC)

	#Get image from array
	blurredimg = Image.fromarray(np.uint8(tempC))
	#Pass blurred image back to main
	return blurredimg

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('-i', '--image', type=str, help="Filepath or Name of Image to transform")
	parser.add_argument('-g', '--grayscale', action='store_true', help="Converts an image to GrayScale")
	parser.add_argument('-b','--blur', type=int, help="Blurs an RGB Image on a scale of 0-5")
	parser.add_argument('-o', '--output', type=str, help="Filepath or Name + Extension type of Output file")

	
	if len(sys.argv) < 2:
		parser.print_help(sys.stderr)
		sys.exit(1)

	args = parser.parse_args()

	filename = misc.imread(args.image)
	
	output = os.path.basename(args.image).split(".")[0]

	#Checks for blur flag and performs blur
	if args.blur: 
		print "Applying Blur to %r" % args.image
		if len(filename.shape) < 3:
			print "Error: Grayscale image or scalar provided. RGB Image Needed."
			sys.exit(1)
		else:
			filename = Blur(filename, args.blur)
			print "Done."
			if not args.output:
				output = output + "_blur"
	#Checks for grayscale flag and performs grayscale
	if args.grayscale:
		print "Applying Grayscale to %r" % args.image
		filename = GrayScale(np.asarray(filename))
		print "Done."
		if not args.output:
			output = output + "_gray"

	if args.output:
			output = "%s" % args.output
			misc.imsave(output, filename)


	if not args.output: 
		misc.imsave(output + ".jpg", filename)

	
#Main Execution
if __name__ == "__main__":
	main()


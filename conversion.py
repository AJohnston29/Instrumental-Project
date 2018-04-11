#!/usr/bin/python
#Script created by Anthony Johnston

import sys
from scipy import misc
import numpy as np
from PIL import Image

#RGB to Grayscale Conversion Function
def GrayScale(filename):
	def LuminosityMethod(pixel):
		return 0.21*(pixel[0])+0.72*(pixel[1])+ 0.07*(pixel[2])

	gray = np.zeros(filename.shape[0:-1])
	for row in range(len(filename)):
		for col in range(len(filename[row])):
			gray[row][col] = LuminosityMethod(filename[row][col])

	return gray

	#The line has the same affect as multiple nested for loops
	#The line multiplies every pixel in the file array in a row*col manner
	#with 0.299, 0.587, and 0.114, which is a weighted average
	#The result is a grayscale conversion

def Blur(filename):
	imgarray = np.asarray(filename)

	#Pixel radius of blur
	radius = 2

	#Sets window length of blur in respect to individual pixels
	#In this case, length will be set to 5
	wlen = (radius*2)+1
	#Defines height and width of image array

	height = imgarray.shape[0] #Rows (Y-Variable)
	width = imgarray.shape[1] #Columns (X-Variable)

	def blur_(imgarray):
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
	passes = 3
	#Another temp array to hold values from each pass
	tempC = imgarray
	for k in range(passes):
		tempC = blurIt(tempC)

	#Get image from array
	blurredimg = Image.fromarray(np.uint8(tempC))
	#Pass blurred image back to main
	return blurredimg

#Main Execution
if __name__ == "__main__":
	#Library takes in an image based on user input
	if len(sys.argv) < 2:
		print "Error: Define filename and transformation"
	else:
		filename = misc.imread(sys.argv[1])


		#Program checks for which transformation to complete

		#Checks for too few arguments
		if len(sys.argv) < 3:
			print "Too few arguments: Define transformation"

		#If filename + 1 extra argument is given, check which transformation
		elif len(sys.argv) == 3:
			#Checks if third argument is grayscale, performs grayscale
			if sys.argv[2] == "grayscale":
				gray = GrayScale(filename)
				print "Done."
				output = sys.argv[1].split(".")[0] + "_gray.jpg"
				misc.imsave(output, gray)
			#Checks if third argument is blur, performs blur
			elif sys.argv[2] == "blur":
				blur = Blur(filename)
				print "Done."
				output = sys.argv[1].split(".")[0] + "_blur.jpg"
				misc.imsave(output, blur)
			#Checks if third argument is both, will perform both transformations
			elif sys.argv[2] == "both":
				step1 = Blur(filename)
				step2 = GrayScale(np.asarray(step1))
				print "Done."
				output = sys.argv[1].split(".")[0] + "_both.jpg"
				misc.imsave(output, step2)
		#Checks for too many arguments
		elif len(sys.argv) > 3:
			print "Too many arguments"


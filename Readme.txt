----Conversion.py Usage---
***Created by Anthony Johnston*** 

----- Description ------
The program includes two functions: 
1.) Convert an image to grayscale
2.) Blur an image

The user can specify an image and transformation as system arguments, and the transformed image will be saved as an output in the same folder. 

----- How to Use ------
1.) Open terminal
2.) Navigate to the directory that contains the script.
3.) Execute the program with the following system arguments:
	python conversion.py <image> <transformation> 

	*For Image: Provide an image name

	*For Transformation: Choose from the following 3 transformations
		*grayscale - this will convert the chosen image to a 				             grayscale color scheme.

		*blur - this will blur the chosen image.

		*both - this will both blur the chosen image, and then      			  			convert it to grayscale.

----- Usage Examples ------
For the examples below, see the pictures included in the folder for the expected output of each function. 

Example 1:
----------

Original Image: Racoon.jpg



Input: python conversion.py Racoon.jpg grayscale

Output: Racoon_gray.jpg


Input: python conversion.py Racoon.jpg blur

Output: Racoon_blur.jpg


Input: python conversion.py Racoon.jpg both

Output: Racoon_both.jpg


------
Example 2
------
Original Image: flower.jpeg


Input: python conversion.py flower.jpg grayscale

Output: flower_gray.jpg


Input: python conversion.py flower.jpg blur

Output: flower_blur.jpg


Input: python conversion.py flower.jpg both

Output: flower_both.jpg


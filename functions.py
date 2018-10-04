import numpy as np
import sys

#define a function that returns a value 
def expo(x):
	return np.exp(x)	#return the np e^x function
	
#define a subroutine that does not define a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function e^float(i)
		
#define a main function
def main():
	n = 10	#provide a default function for n
	
	# check if command line argument is provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument is provided. use it for n
		
	show_expo(n)	#call the expo sub routine
	
#run the main function
if __name__ == "__main__":
	main()
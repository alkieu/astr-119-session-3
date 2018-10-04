import numpy as np	#import numpy library

#integers

i = 10			#integer
print(type(i))	#print out data type, i

a_i = np.zeros(i,dtype=int) #declare and array of ints
print(type(a_i))			#will return ndarray
print(type(a_i[0]))			#will return int64

#floats

x = 119.0		#floating point number
print(type(x))	#print out data type x

y = 1.19e2		#float 119 in sci notation
print(type(y))	#print out data type y

z = np.zeros(i,dtype=float)	#declare an array of floats
print(type(z))				#will retur nd array
print(type(z[0]))			#will return float64	
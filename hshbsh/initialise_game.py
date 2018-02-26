#import slice_lib as sl
import numpy as np

# pizza = array of array n X n
# min_tomato = l
# max_size = h
# size_init_slice = we fix this, is an array (width, height) for the init slices

def initialise_owner(pizza, min_tomato, max_size, size_init_slice = [2,2] ):

	nrow, ncol = pizza.shape
	ID_slices = 1
	owner = np.zeros(pizza.shape, int)

	init_slice = np.zeros(size_init_slice, int)

	number_slice_x = int( nrow/size_init_slice[0] )
	number_slice_y = int( ncol/size_init_slice[1] )

	for i in range(number_slice_x):
		for j in range(number_slice_y):
			start_i = i*size_init_slice[0]
			start_j = j*size_init_slice[1]
			owner[start_i:start_i+size_init_slice[0],start_j:start_j+size_init_slice[1]] = ID_slices
			ID_slices += 1

	owner.resize( (nrow, ncol) )

	return owner

#def initialise_slice

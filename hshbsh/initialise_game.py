import slice_lib as sl
import numpy as np

# initialising the owner
#
# pizza = array of array n X n
# min_tomato = l
# max_size = h
# size_init_slice = we fix this, is an array (width, height) for the init slices

def initialise_owner(pizza, min_tomato, max_size, size_init_slice = [2,2] ):

	nrow, ncol = pizza.shape
	ID_slices = 1
	owner = np.zeros(pizza.shape, int)
	slice_info = []

	init_slice = np.zeros(size_init_slice, int)

	number_slice_x = int( nrow/size_init_slice[0] )
	number_slice_y = int( ncol/size_init_slice[1] )

	for i in range(number_slice_x):
		for j in range(number_slice_y):
			start_i = i*size_init_slice[0]
			start_j = j*size_init_slice[1]
			owner[start_i:start_i+size_init_slice[0],start_j:start_j+size_init_slice[1]] = ID_slices
			slice_info.append([ID_slices, start_i, start_i+size_init_slice[0]-1, start_j, start_j+size_init_slice[1]-1])
			ID_slices += 1

	owner.resize( (nrow, ncol) )

	return owner, slice_info

# initialising the slice
#
# pizza = array of array n X n
# owner = array of array n X n
# slices = something?

def initialise_slice(pizza, owner, slice_info, slices):

	slice_dictionary = {}

	for identity, ri, rf, ci, cf in slice_info:
		slice_dictionary[identity] = sl.Slice(pizza, owner, slices, identity, ri, rf, ci, cf)

	return slice_dictionary

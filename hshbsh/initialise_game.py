import slice_lib as sl
import numpy as np

# pizza = array of array n X n
# min_tomato = l
# max_size = h
# size_init_slice = we fix this, is an array (width, height) for the init slices

def initialise_owner(pizza, min_tomato, max_size, size_init_slice = [2,2] ):

	nrow, ncol = pizza.shape()
	ID_slices = 1
	owner_row = np.empty()
	owner = np.empty()

	init_slice = np.zeros(size_init_slice, int)

	number_slice_x = int( nrow/size_init_slice[0] )
	number_slice_y = int( ncol/size_init_slice[1] )

	for i in range(number_slice_x):
		for j in range(number_slice_y):
			init_slice.fill(ID_slices)
			owner_row = np.concatenate( (owner_row, init_slice), axis = 1 )
			ID_slice += 1
		owner = np.concatenate( (owner, owner_row), axis = 0)

	print(owner)



from Network import Network
import random
import numpy as np


class Environment:
	def mutate(network: Network, probability: float):
        # Mutate the weights
		mutate = random.random()
		# If chosen mutate a single weight
		if mutate < probability:
			rand_num = random.random(0, 3)
			if rand_num == 0:
				# Choose a random weight and mutate it using numpy
				x = random.randint(0, network.add_weights.size[0] - 1)
				y = random.randint(0, network.add_weights.size[1] - 1)
				z = random.randint(0, network.add_weights.size[2] - 1)
				network.add_weights[x, y, z] = np.random.rand()
			elif rand_num == 1:
				# Choose a random weight and mutate it using numpy
				x = random.randint(0, network.subtract_weights.size[0] - 1)
				y = random.randint(0, network.subtract_weights.size[1] - 1)
				z = random.randint(0, network.subtract_weights.size[2] - 1)
				network.subtract_weights[x, y, z] = np.random.rand()
			elif rand_num == 2:
				# Choose a random weight and mutate it using numpy
				x = random.randint(0, network.multiply_weights.size[0] - 1)
				y = random.randint(0, network.multiply_weights.size[1] - 1)
				z = random.randint(0, network.multiply_weights.size[2] - 1)
				network.multiply_weights[x, y, z] = np.random.rand()
			elif rand_num == 3:
				# Choose a random weight and mutate it using numpy
				x = random.randint(0, network.divide_weights.size[0] - 1)
				y = random.randint(0, network.divide_weights.size[1] - 1)
				z = random.randint(0, network.divide_weights.size[2] - 1)
				network.divide_weights[x, y, z] = np.random.rand()
			else:
				print("Huston we have a problem")
    
	def crossover(network1: Network, network2: Network):
		# Create mask and inverted mask
		mask = np.random.randint(0, 1, size=network1.add_weights.size)
		mask_inverted = np.invert(mask)
  
		# Get weights of the first network
		add_weights_1 = np.multiply(network1.add_weights, mask)
		subtract_weights_1 = np.multiply(network1.subtract_weights, mask)
		multiply_weights_1 = np.multiply(network1.multiply_weights, mask)
		divide_weights_1 = np.multiply(network1.divide_weights, mask)

		# Get weights of the first network with the inverted mask
		add_weights_1_inverted = np.multiply(network1.add_weights, mask_inverted)
		subtract_weights_1_inverted = np.multiply(network1.subtract_weights, mask_inverted)
		multiply_weights_1_inverted = np.multiply(network1.multiply_weights, mask_inverted)
		divide_weights_1_inverted = np.multiply(network1.divide_weights, mask_inverted)

		# Get weights of the second network
		add_weights_2 = np.multiply(network2.add_weights, mask)
		subtract_weights_2 = np.multiply(network2.subtract_weights, mask)
		multiply_weights_2 = np.multiply(network2.multiply_weights, mask)
		divide_weights_2 = np.multiply(network2.divide_weights, mask)
	
		# Get weights of the second network with the inverted mask
		add_weights_2_inverted = np.multiply(network2.add_weights, mask_inverted)
		subtract_weights_2_inverted = np.multiply(network2.subtract_weights, mask_inverted)
		multiply_weights_2_inverted = np.multiply(network2.multiply_weights, mask_inverted)
		divide_weights_2_inverted = np.multiply(network2.divide_weights, mask_inverted)
  
		# Create new network for network 1
		network1.add_weights = np.add(add_weights_1, add_weights_2_inverted)
		network1.subtract_weights = np.add(subtract_weights_1, subtract_weights_2_inverted)
		network1.multiply_weights = np.add(multiply_weights_1, multiply_weights_2_inverted)
		network1.divide_weights = np.add(divide_weights_1, divide_weights_2_inverted)

		# Create new network for network 2
		network2.add_weights = np.add(add_weights_2, add_weights_1_inverted)
		network2.subtract_weights = np.add(subtract_weights_2, subtract_weights_1_inverted)
		network2.multiply_weights = np.add(multiply_weights_2, multiply_weights_1_inverted)
		network2.divide_weights = np.add(divide_weights_2, divide_weights_1_inverted)
	
	def run(network: Network, input_image: np.array):
		# Go though each layer and calculate the output
		for layer in range(network.depth):
			# Get the weights for the current layer
			add_weights = network.add_weights[layer]
			subtract_weights = network.subtract_weights[layer]
			multiply_weights = network.multiply_weights[layer]
			divide_weights = network.divide_weights[layer]
			# Calculate the output for the current layer
			input_image = np.add(np.subtract(np.divide(np.multiply(input_image, multiply_weights), divide_weights), subtract_weights), add_weights)

		# Add of all of the outputs
		return np.sum(input_image)
		 

		

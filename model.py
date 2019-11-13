import matplotlib.pyplot as plt
import numpy as np
import random
from operator import methodcaller

class Simulator:

	def __init__(self, model):

		# model is the model to simulate
		# data is the data to plot

		self.__model = model
		self.__data = None

	def __plot(self, show, path, title):

		# This function is for ploting.

		plt.title(title)
		l = len(self.__data[0])
		for i in range(len(show)):
			if show[i]:
				plt.plot(range(l), self.__data[i], label = self.__model.getStateName()[i])
		plt.ylabel("population")
		plt.xlabel(r"time/$10^{-4}$")
		plt.legend()
		plt.savefig(path)
		plt.clf()

	def simulation(self, n, graph = False, show = [1, 1, 1], path = None, title = "SIR model graph"):
		
		# This function is for call the model's simulation method and plot.
		# n is the num of round to simulate
		# graph is to plot or not
		# show is a list allowing only 0 or 1 in it, means to show the 
		# corresponding curve or not

		state = self.__model.state
		num_state = len(state)
		
		if not isinstance(show, list) or len(show) != num_state or len([elt for elt in show if elt not in range(2)]) > 0:
			raise Exception("invalid show!", show)
		if graph and not path:
			raise Exception("empty path!", path)
		if n <= 0:
			raise Exception("invalid n!", n)

		if not graph:
			self.__model.simulation_with_no_process(n)	
		else:
			self.__data = self.__model.simulation(n)
			self.__plot(show, path, title)

class SIRModel:

	def __init__(self, l1, l2, state = None, state_name = None):

		# l1 and l2 is two rates
		# state is the initial amount in each state. At least 3 states
		# state_name must have the same length with state

		if not state:
			self.state = [0, 0, 0]
		else:
			self.setStateAsList(state)
		if not state_name:
			if not state or len(state) == 3:
				self.__state_name = ["suspected", "infected", "recover"]
			else:
				self.__state_name = ["state" + str(elt) for elt in range(1, len(state) + 1)]
		else:
			if len(self.state) != len(state_name):
				raise Exception("invalid state name!")
			self.__state_name = state_name
		if l1 < 0:
			raise Exception("invalid l1!")
		if l2 < 0:
			raise Exception("invalid l2!")
		self.__lambda = [l1, l2]
		self.initial_state = self.state

	def restartState(self, total_number = 0, I = 0):

		# restart the state

		self.state = self.initial_state

	def setStateAsList(self, state):

		# set state 

		if isinstance(state, np.ndarray):
			state = list(state)
		if not isinstance(state, list) or len([elt for elt in state if elt < 0]) > 0:
			raise Exception("invalid input!", state)
		self.state = list(state)

	def event_1(self):

		# we can modify the action for each event here! 
		# the event method must start with "event_"

		if self.state[0] > 0:
			self.state[0] -= 1
			self.state[1] += 1

	def event_2(self):
		if self.state[1] > 0:
			self.state[1] -= 1
			self.state[2] += 1

	def getStateName(self):
		return self.__state_name

	def getTime_1(self):

		# we can modify the waiting time variable output here! concerning about 
		# the variable not following expo distribution, I use the variable instead 
		# of shape parameter as the output.
		# the rate method must start with "getTime_"

		s = self.__lambda[0] * self.state[0]
		return random.expovariate(s) if s else float('inf')

	def getTime_2(self):
		s = self.__lambda[1] * self.state[1]
		return random.expovariate(s) if s else float('inf')

	def __valid_method(self):

		# this function is to gather all the rate method and event method 
		# and validate them.

		rate_method = list(filter(lambda m: m.startswith("getTime_") and callable(getattr(self, m)), dir(self)))
		event_method = list(filter(lambda m: m.startswith("event_") and callable(getattr(self, m)), dir(self)))

		try:
			rate_method = sorted(rate_method, key = lambda x: int(x.split("_")[1]))
			event_method = sorted(event_method, key = lambda x: int(x.split("_")[1]))
		except Exception as e:
			raise Exception("invalid rate method and event method!", rate_method, event_method)

		if len(rate_method) != len(event_method):
			raise Exception("invalid rate method and event method!", rate_method, event_method)

		for i in range(len(rate_method)):
			r_index = int(rate_method[i].split("_")[1])
			e_index = int(event_method[i].split("_")[1])
			if r_index != e_index:
				raise Exception("invalid rate method and event method!", rate_method, event_method)

		return rate_method, event_method

	def simulation_with_no_process(self, n):

		# This function is to simulate with no process
		# if u only want the result. use this method

		rate_methods, event_methods = self.__valid_method()
		total_t = 0

		while True:
			if total_t > n:
				break

			t = []
			for rate_method in rate_methods:
				t.append(methodcaller(rate_method)(self))
			t_min = min(t)
			total_t += t_min

			if t_min == float('inf'):
				break

			for i in range(len(t)):
				if t_min == t[i]:
					methodcaller(event_methods[i])(self)

	def simulation(self, n):

		# if u want the process, use this method
		# this method will output the process data for plot

		delta_t = 1e-4
		num_state = len(self.state)
		data = [[] for _ in range(num_state)]

		for i in range(num_state):
			data[i] = [self.state[i]]

		rate_methods, event_methods = self.__valid_method()

		while True:
			if len(data[0]) > n:
				break

			t = []
			for rate_method in rate_methods:
				t.append(methodcaller(rate_method)(self))
			t_min = min(t)

			if t_min == float('inf'):
				break

			l = round(t_min / delta_t)

			for i in range(num_state):
				data[i] += [data[i][-1] for _ in range(l)]

			for i in range(len(t)):
				if t_min == t[i]:
					methodcaller(event_methods[i])(self)

			for i in range(num_state):
				data[i][-1] = self.state[i]

		return data

class BacteriaTransformationModel(SIRModel):

	def __init__(self, l1, l2, l3, l4, l_death=0.1,l5=0.0005, state = None, state_name = None):
		super().__init__(l1, l2, state, state_name)
		self.population_stress = l5
		self.__lambda = [l1, l2, l3, l4, l_death]

	def getTime_3(self):

		# new model can inherit SIRModel and create new rate method like that

		s = self.__lambda[2] * self.state[1]
		return random.expovariate(s) if s else float('inf')

	def event_3(self):

		# new model can inherit SIRModel and create new event method like that

		if self.state[1] > 0:
			self.state[1] -= 1
			self.state[0] += 1

	def getTime_4(self):
		s = (self.__lambda[3] - self.population_stress * self.state[0]) * self.state[0]
		return random.expovariate(s) if s > 0 else float('inf')

	def event_4(self):
		self.state[0] += 1

	def getTime_5(self):
		s = self.__lambda[4] * self.state[0]
		return random.expovariate(s) if s else float('inf')

	def event_5(self):
		if self.state[0] > 0:
			self.state[0] -= 1
			self.state[2] += 1

	def getTime_6(self):
		s = -(self.__lambda[3] - self.population_stress * self.state[0]) * self.state[0]
		return random.expovariate(s) if s > 0 else float('inf')

	def event_6(self):
		if self.state[0] > 0:
			self.state[0] -= 1

if __name__ == '__main__':

	model1 = SIRModel(l1 = 1.0, l2 = 0.2, state = [10000, 200, 0])
	simulator1 = Simulator(model = model1)
	simulator1.simulation(n = 20000, graph = True, path = "SIRModel1.png", title = r"SIRModel, $\lambda_1 = 1.0, \lambda_2 = 0.2$")

	model2 = BacteriaTransformationModel(l1 = 2.0, l2 = 0.02, l3 = 0.1, l4 = 0.4, state = [10000, 200, 0], state_name = ["normal", "VBNC", "dead"])
	simulator2 = Simulator(model = model2)
	simulator2.simulation(n = 20000, graph = True, path = "BacteriaModel1.png", title = r"BacteriaModel, $\lambda_1 = 2.0, \lambda_2 = 0.02, \lambda_3 = 0.1, \lambda_4 = 0.4$")

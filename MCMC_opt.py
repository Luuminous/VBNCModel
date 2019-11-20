# apply MCMC to optimize the schema
import numpy as np
import time
from model import SIRModel,Simulator,BacteriaTransformationModel, Simulator_2_model
import matplotlib.pyplot as plt
import random

# Global setting for parameters
# friendly state
l1_f = 0. # C->V
l2_f = 0.	# V->D
l3_f = 0.2   # V->C
l4_f = 0.5 # amplication
l5_f = 0.00005
l_death_f = 0.1
# harsh state
l1_h = 1.0
l2_h = 0.
l3_h = 0.
l4_h = 0.5
l5_h = 0.00005
l_death_h = 1.
cur_s = [12000, 0, 0]

t_f_even = 300000 # time for equalibrium 

model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

model_h = BacteriaTransformationModel(l1_h, l2_h, l3_h, l4_h, l_death_h, l5_h, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

# get the expected time for eliminate over 99%
def get_expected_time(schema,simulator,n_trail=5):
	t = []
	for i in range(n_trail):
		simulator.set_time(schema)
		_,t1 = simulator.get_result_99percent()
		t.append(t1)
	return np.array(t).mean()



def test_get_expected_time():
	simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 10000,\
	time2 = 30000, iteration = 100)
	#schema
	S1 = [15000, 30000]
	S2 = [5000, 30000]

	start_time = time.time()
	print("exp for s1: ",get_expected_time(S1,simulator))
	print("time passed: ",time.time()-start_time)

	start_time = time.time()
	print("exp for s2: ",get_expected_time(S2,simulator))
	print("time passed: ",time.time()-start_time)

# test_get_expected_time()


# TODO: add an parameter: maximum time, over this time, return directly this maximum value

# doing MCMC here
def MCMC_opt(max_trail = 5000):
	def get_a_neighbor(S,nrange=0.1): # get +-0.1 of the input n, return an int
		s1,s2 = S
		b1 = int(s1*nrange)
		b2 = int(s2*nrange)
		return [s1+random.randint(-b1,b1),s2+random.randint(-b2,b2)]

	cur_S = [5000, 30000]
	ret_S_lst = []
	simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 10000,\
	time2 = 30000, iteration = 100)
	cur_exp_time = get_expected_time(cur_S,simulator)

	for i in range(max_trail):
		print("iter={0}, S={1}, exptime={2}".format(i,cur_S,cur_exp_time))
		ret_S_lst.append(cur_S)
		next_S = get_a_neighbor(cur_S)
		next_exp_time = get_expected_time(cur_S,simulator)
		r = random.random()
		r1 = float(next_exp_time)/float(cur_exp_time)
		if r<r1:
			cur_S = next_S
			cur_exp_time = next_exp_time
	return ret_S_lst

MCMC_opt()






#

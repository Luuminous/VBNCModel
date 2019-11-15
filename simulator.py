from model import SIRModel,Simulator,BacteriaTransformationModel, Simulator_2_model
init_state = state = [10000, 200, 0]
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

t_f_even = 300000 # time for equalibrium 


cur_s = [12000, 0, 0]
# for iter in range(10):
# 	model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
# 	 state = cur_s, state_name = ["normal", "VBNC", "dead"])
# 	simulator_f = Simulator(model = model_f)
# 	simulator_f.simulation(n = t_f_even*0.1, graph = True, path = "friendly{0}.png".format(iter), title = "BacteriaModel, \
# 		l1 = {0}, l2 = {1}, l3 = {2}, l4 = {3}, l5 = {4}, l_death={5}"\
# 		.format(l1_f, l2_f, l3_f, l4_f, l5_f,l_death_f))

# 	cur_s = model_f.state
# 	print(cur_s)
# 	model_h = BacteriaTransformationModel(l1_h, l2_h, l3_h, l4_h, l_death_h, l5_h, \
# 	 state = cur_s, state_name = ["normal", "VBNC", "dead"])
# 	simulator_f = Simulator(model = model_h)
# 	simulator_f.simulation(n = t_f_even*0.1, graph = True, path = "harsh{0}.png".format(iter), title = "BacteriaModel, \
# 		l1 = {0}, l2 = {1}, l3 = {2}, l4 = {3}, l5 = {4}, l_death={5}"\
# 		.format(l1_h, l2_h, l3_h, l4_h, l5_h,l_death_h))

# 	cur_s = model_h.state
# 	print(cur_s)

# print("final")
# simulator_f = Simulator(model = model_h)
# simulator_f.simulation(n = t_f_even, graph = True, path = "harsh{0}.png".format(iter), title = "BacteriaModel, \
# l1 = {0}, l2 = {1}, l3 = {2}, l4 = {3}, l5 = {4}, l_death={5}"\
# 		.format(l1_h, l2_h, l3_h, l4_h, l5_h,l_death_h))

# cur_s = model_h.state
# print(cur_s)

model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

model_h = BacteriaTransformationModel(l1_h, l2_h, l3_h, l4_h, l_death_h, l5_h, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

# simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 10000, time2 = 30000, iteration = 40)
# simulator.simulation(graph = True, path = "f-h-iter-v2.png", title = "friendly-harsh-iteration-v2")
simulator = Simlulator(model = model_f)
simulator.simulation(n = 30000, graph = False)
print(model_f.state)

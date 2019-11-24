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

simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 100, time2 = 250, iteration = 10000)
simulator.simulation(graph = True, path = "1.png", show = [1, 1, 0], title = "t1=100 t2=250")
# print("stop when reach 1%")
# print(simulator.get_result_99percent())
# simulator.set_time([15000, 30000])
# print(simulator.get_result_99percent())
# simulator.set_time([5000, 30000])
# print(simulator.get_result_99percent())

simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 5000, time2 = 25000, iteration = 100)
simulator.simulation(graph = True, path = "2.png", show = [1, 1, 0], title = "t1=5000 t2=25000")
# print("stop when the difference in each turn less than 0.1%")
# simulator.set_time([10000, 30000])
# print(simulator.get_result_threshold())
# simulator.set_time([15000, 30000])
# print(simulator.get_result_threshold())
# simulator.set_time([5000, 30000])
# print(simulator.get_result_threshold())

# simulator = Simulator(model = model_f)
# simulator.simulation(n = 50000, graph = True, path = "0.55.png", title = "test")
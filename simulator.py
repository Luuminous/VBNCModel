from model import SIRModel,Simulator,BacteriaTransformationModel
init_state = state = [10000, 200, 0]
# friendly state
l1_f = 0. # C->V
l2_f = 0.	# V->D
l3_f = 0.2   # V->C
l4_f = 0.5 # amplication
l5_f = 0.0005
l_death_f = 0.1
# harsh state
l1_h = 1.0
l2_h = 0.
l3_h = 0.
l4_h = 0.5
l5_h = 0.0005
l_death_h = 1.

t_f_even = 30000 # time for equalibrium 
model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
 state = [0, 10000, 0], state_name = ["normal", "VBNC", "dead"])
simulator_f = Simulator(model = model_f)
simulator_f.simulation(n = t_f_even, graph = True, path = "friendly.png", title = "BacteriaModel, \
	l1 = {0}, l2 = {1}, l3 = {2}, l4 = {3}, l5 = {4}, l_death={5}"\
	.format(l1_f, l2_f, l3_f, l4_f, l5_f,l_death_f))

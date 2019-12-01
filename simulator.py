from model import SIRModel,Simulator,BacteriaTransformationModel, Simulator_2_model
import matplotlib.pyplot as plt

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

model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

model_h = BacteriaTransformationModel(l1_h, l2_h, l3_h, l4_h, l_death_h, l5_h, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

simulator = Simulator(model = model_h)
simulator.simulation(n = 50000, graph = True, show = [1, 1, 0], path = "only_harsh.png", title = "bacteria amount change with harsh environment")

# simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 109, time2 = 336)
# data1 = simulator.simulation_raw_data_99_percent()
# print("stop when reach 1%")
# print(simulator.get_result_99percent())
# simulator.set_time([15000, 30000])
# print(simulator.get_result_99percent())
# simulator.set_time([5000, 30000])
# print(simulator.get_result_99percent())

# simulator.set_time([9000, 26000])
# data2 = simulator.simulation_raw_data_99_percent()
# print("stop when the difference in each turn less than 0.1%")
# simulator.set_time([10000, 30000])
# print(simulator.get_result_threshold())
# simulator.set_time([15000, 30000])
# print(simulator.get_result_threshold())
# simulator.set_time([5000, 30000])
# print(simulator.get_result_threshold())

# simulator.set_time([10000, 30000])
# data3 = simulator.simulation_raw_data_99_percent()

# simulator = Simulator(model = model_f)
# simulator.simulation(n = 50000, graph = True, path = "0.55.png", title = "test")

# min_l = min([len(data1), len(data2), len(data3)])
# data1 = data1[:min_l]
# data2 = data2[:min_l]
# data3 = data3[:min_l]

# plt.title("bacteria amount changing with 3 different treatments")
# plt.ylabel("bacteria amount")
# plt.xlabel("pseudo time")
# plt.plot(range(len(data1)), data1, label = r"$t_f$ = 109, $t_h$ = 336")
# plt.plot(range(len(data2)), data2, label = r"$t_f$ = 9000, $t_h$ = 26000")
# plt.plot(range(len(data3)), data3, label = r"$t_f$ = 10000, $t_h$ = 30000")
# plt.legend()
# plt.savefig("simulation_result.png")
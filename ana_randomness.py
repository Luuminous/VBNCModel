# quantify the randomness 
import time
from model import SIRModel,Simulator,BacteriaTransformationModel, Simulator_2_model
import matplotlib.pyplot as plt
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

simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = 10000, time2 = 30000, iteration = 100)



N_trail = 50

#schema
S1 = [109, 336]
S2 = [7000, 15000]
S3 = [9000, 26000]

t_lst_1 = []
t_lst_2 = []
t_lst_3 = []
start_time = time.time()
for i in range(N_trail):
	simulator.set_time(S1)
	_,t1 = simulator.get_result_99percent()
	simulator.set_time(S2)
	_,t2 = simulator.get_result_99percent()
	simulator.set_time(S3)
	_,t3 = simulator.get_result_99percent()
	t_lst_1.append(t1)
	t_lst_2.append(t2)
	t_lst_3.append(t3)
elapsed_time = time.time() - start_time
print("finished simulation for {0} trails".format(N_trail))
print("total time: ",elapsed_time)

# draw box plot
plt.title("randomness analysis: total trail="+str(N_trail))
plt.ylabel("pseudo time")
plt.boxplot([t_lst_1,t_lst_2,t_lst_3])
plt.xticks([1, 2, 3], ["schema: "+str(S1), "schema: "+str(S2), "schema: "+str(S3)])
plt.savefig("ana_random_alter.png")




#


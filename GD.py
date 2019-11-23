from model import SIRModel,Simulator,BacteriaTransformationModel, Simulator_2_model
import sys

# friendly state
l1_f = 0. # C->V
l2_f = 0.	# V->D
l3_f = 0.2   # V->C
l4_f = 0.5  # amplication
l5_f = 0.00005  # population stress
l_death_f = 0.1  # C->D
# harsh state
l1_h = 1.0
l2_h = 0.
l3_h = 0.
l4_h = 0.5
l5_h = 0.00005
l_death_h = 1.0

cur_s = [12000, 0, 0]
t1 = int(sys.argv[1])
t2 = int(sys.argv[2])

model_f = BacteriaTransformationModel(l1_f, l2_f, l3_f, l4_f, l_death_f, l5_f, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

model_h = BacteriaTransformationModel(l1_h, l2_h, l3_h, l4_h, l_death_h, l5_h, \
	state = cur_s, state_name = ["normal", "VBNC", "dead"])

alpha = 0.01
discount = 0.9

def some_function(t1, t2):
	return t1 ** 2 + t2 ** 2

def average_time(t1, t2):
	simulator = Simulator_2_model(model1 = model_f, model2 = model_h, time1 = t1, time2 = t2, iteration = 100)
	ans = 0
	for _ in range(7):
		_, t = simulator.get_result_99percent()
		ans += t
	return ans / 7

def gradient(t1, t2, fix, f):
	f1 = f(t1, t2)
	if fix == 't1':
		f2 =  f(t1, t2 + 100)
		return (f2 - f1) / 100
	if fix == 't2':
		f2 =  f(t1 + 100, t2)
		return (f2 - f1) / 100

def findMax(t1, t2, f):
	pre_g1, pre_g2 = 0, 0
	path = str(t1) + "_" + str(t2) + ".txt"
	t = open(path, 'w')
	for i in range(5000):
		print(path, i)
		t1_future = t1 - alpha * discount * pre_g1
		t2_future = t2 - alpha * discount * pre_g2
		g1 = gradient(t1_future, t2_future, 't2', f)
		g2 = gradient(t1_future, t2_future, 't1', f)
		pre_g1 = pre_g1 * discount + g1
		pre_g2 = pre_g2 * discount + g2
		t.write('t1 = %.3f t2 = %.3f gradient = %f, %f\n' %(t1, t2, g1, g2))
		t1 -= alpha * pre_g1
		t2 -= alpha * pre_g2
	t.close()

findMax(t1, t2, average_time)
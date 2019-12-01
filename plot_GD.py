import matplotlib.pyplot as plt
import sys, os

f_li = []
point_li = []

for root, paths, files in os.walk("."):
	for file in files:
		temp = file.split(".")
		if temp[-1] == "txt":
			f_li.append(open(file))
			t1 = int(temp[0].split("_")[0])
			t2 = int(temp[0].split("_")[1])
			point_li.append((t1, t2))

x = []
y = []

for f in f_li:
	temp_x = []
	temp_y = []
	for line in f.readlines():
		temp = line.strip().split()
		if len(temp) < 5:
			break
		temp_x.append(float(temp[2]))
		temp_y.append(float(temp[5]))
	x.append(temp_x)
	y.append(temp_y)

color = ['red', 'orange', 'greenyellow', 'aquamarine', 'deepskyblue', 'violet']

plt.title("Nesterov gradient descent path graph")
for i in range(len(x)):
	plt.plot(x[i], y[i], color = color[i % 6], alpha = 0.5)
	plt.scatter(point_li[i][0], point_li[i][1], color = color[i % 6], marker = 'H')
plt.ylabel(r"$t_h$")
plt.xlabel(r"$t_f$")
plt.savefig("GD_path.png")
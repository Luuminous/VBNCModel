import matplotlib.pyplot as plt
import sys, os

f_li = []

for root, paths, files in os.walk("."):
	for file in files:
		temp = file.split(".")
		if temp[-1] == "txt":
			f_li.append(open(file))

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

plt.title("Nesterov gradient descent path graph")
for i in range(len(x)):
	for j in range(len(y)):
		plt.plot(x[i], y[i])
plt.savefig("GD_path.png")
import matplotlib.pyplot as plt

f = open('5000_30000.txt', 'r')
x = []
y = []

for line in f.readlines():
	temp = line.strip().split()
	if len(temp) < 5:
		break
	x.append(float(temp[2]))
	y.append(float(temp[5]))

plt.title("Nesterov gradient descent path graph")
plt.plot(x, y, color = "green")
plt.savefig("GD_path.png")
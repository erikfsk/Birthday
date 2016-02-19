from matplotlib.pyplot import *

def bursdag(x):
	summen = 1
	for k in range(int(x)):
		summen = summen * ((365-k)/365.0)
	return 100-(summen*100)

sannsynlighet = []
for i in range(0,136):
	sannsynlighet.append(bursdag(i))

for i in range(0,len(sannsynlighet)):
	print i,sannsynlighet[i]

sannsynlighet_10 = []
x_sannsynlighet_10 = []
for i in range(0,len(sannsynlighet),10):
	sannsynlighet_10.append(sannsynlighet[i])
	x_sannsynlighet_10.append(i)

grid("on")
plot(sannsynlighet)
plot(x_sannsynlighet_10,sannsynlighet_10,"ro")
title("Sannsynligheten for at noen har bursdag samme dag")
xlabel("Antall personer")
ylabel("%")

show()
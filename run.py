from __future__ import division
import numpy as np
from mlp_predict import NeuralNetwork


digits = raw_input ("Input path (without quotes)>>")
try:
	with open(digits) as f:
		ip=f.read().splitlines()
		for x in range(0,5):
			ip[x]=int(ip[x],2)
		iput=[i/sum(ip) for i in ip]
except:
	print "Error: Check your input path (probably it doesn't exist)"
	exit()
predictions = []
for ii in range(0,9):
	digits = "inputs/"+str(ii)+".txt"
	with open(digits) as f:
		ip=f.read().splitlines()
		for x in range(0,5):
			ip[x]=int(ip[x],2)
		data=[i/sum(ip) for i in ip]

	nn = NeuralNetwork([5,3,1],'tanh')
	o1 = nn.predict(data)
	o2 = nn.predict(iput)
	o = abs(o1-o2)
	predictions.append(o)
op=np.argmin(predictions)
print "Predicted value is ",op

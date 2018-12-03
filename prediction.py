# python 2.7 pip
# machine learning, neural networks
# classification, prediction
# features horas de estudo + horas de sono --> nota

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(2,1)

ds.addSample((0.8, 0.5), (0.8))
ds.addSample((0.5, 0.3), (0.4))


nn = buildNetwork(ds.indim, 4, ds.outdim, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in xrange(2000):
	print(trainer.train())
while True:
	dormiu = float(raw_input('dormiu\n'))
	estudou = float(raw_input('estudou\n'))

	z = nn.activate((dormiu, estudou))[0] * 10.0
	print('precisao de nota: ', str(z))


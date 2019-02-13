# a pytorch MLP

import numpy as np
import torch


from dataHelpers import getMNIST, getMNIST_test, getLoaders


# load the data:
tr, blank = getLoaders(getMNIST(), 0.01, batch_size=100) #only using a small fraction of MNIST for each epoch
ts, blank = getLoaders(getMNIST_test(), 1, batch_size=10000)




# initialize the weight and bias tensors. Set requires_grad=True during initialization
sizes = [784, 100, 10]
W0 = torch.tensor( np.random.randn(sizes[0], sizes[1]) / ( sizes[0]**0.5), requires_grad=True, dtype= torch.float32 )
W1 = torch.tensor( np.random.randn(sizes[1], sizes[2]) / ( sizes[1]**0.5), requires_grad=True, dtype= torch.float32 )

b0 = torch.tensor(0., requires_grad=True)
b1 = torch.tensor(0., requires_grad=True)

# relu nonlinearity
f = lambda x: torch.max( x, 0*x)

# readout, loss, and accuracy functions
readout = torch.nn.LogSoftmax(dim=1)
Loss = torch.nn.NLLLoss( reduction='mean' ) # BCELoss( reduction='mean' )



# functions for running the network
def forward( xin):
    '''Runs the network forward to produce log-likelihoods of each of the labels'''
    xin = xin.view(-1, 784) # reshapes the input data
    x1 = f( xin @ W0 + b0 )
    x2 = readout(  x1 @ W1 + b1 )

    return x2



# evaluation for testing:
def accuracy(data, targets):
    ''' determines the accuracy of the outputs'''
    preds = torch.argmax( forward(data), dim=1 )
    yesno = ( preds == targets )
    return sum( yesno.float() ) / float( len(targets) )





# train:
for epoch in range(30):

    testin, testTar = iter(ts).next()
    testin = testin.view(-1, 784)

    print( '===Epoch ' + str(epoch) + ':', accuracy(testin, testTar), '======')


    for (xin, targets) in tr:
        outs = forward(xin)

        L = Loss(outs, targets )
        L.backward()

        lrate = 1E-1

        with torch.no_grad(): # prevents the computation graph from being changed by our addition of the gradients
            W0 -= lrate * W0.grad
            W1 -= lrate * W1.grad

            b0 -= lrate * b0.grad
            b1 -= lrate * b1.grad

            # zero out the gradients
            W0.grad.zero_()
            W1.grad.zero_()
            b0.zero_()
            b1.zero_()











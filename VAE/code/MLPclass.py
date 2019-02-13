# a pytroch MLP

import numpy as np
import torch



class MLP(object):
    '''Multilayer perceptron'''
    def __init__(self):
        # initialize the weight and bias tensors. Set requires_grad=True during initialization
        sizes = [784, 100, 10]
        self.W0 = torch.tensor( np.random.randn(sizes[0], sizes[1]) / ( sizes[0]**0.5), requires_grad=True, dtype= torch.float32 )
        self.W1 = torch.tensor( np.random.randn(sizes[1], sizes[2]) / ( sizes[1]**0.5), requires_grad=True, dtype= torch.float32 )

        self.b0 = torch.tensor(0., requires_grad=True)
        self.b1 = torch.tensor(0., requires_grad=True)

        # relu nonlinearity
        self.f = lambda x: torch.max( x, 0*x)

        # readout, loss, and accuracy functions
        self.readout = torch.nn.LogSoftmax(dim=1)
        self.Loss = torch.nn.NLLLoss( reduction='mean' ) # BCELoss( reduction='mean' )



    # functions for running the network
    def forward(self, xin):
        '''Runs the network forward to produce log-likelihoods of each of the labels'''
        xin = xin.view(-1, 784) # reshapes the input data
        x1 = self.f( xin @ self.W0 + self.b0 )
        x2 = self.readout(  x1 @ self.W1 + self.b1 )

        return x2


    def trainEpoch(self, dataLoader, lrate=0.1):
        '''runs once through the input data set'''
        for (xin, targets) in dataLoader:
            outs = self.forward(xin)

            L = self.Loss(outs, targets )
            L.backward()

            with torch.no_grad(): # prevents the computation graph from being changed by our addition of the gradients
                self.W0 -= lrate * self.W0.grad
                self.W1 -= lrate * self.W1.grad

                self.b0 -= lrate * self.b0.grad
                self.b1 -= lrate * self.b1.grad

                # zero out the gradients
                self.W0.grad.zero_()
                self.W1.grad.zero_()
                self.b0.zero_()
                self.b1.zero_()



def accuracy(nnet, data, targets):
    ''' determines the accuracy of the outputs'''
    preds = torch.argmax( nnet.forward(data), dim=1 )
    yesno = ( preds == targets )
    return sum( yesno.float() ) / float( len(targets) )



def train(nnet, dataLoader, testLoader, epochs=40):
    for i in range(epochs):
        testin, testTar = iter(testLoader).next()
        testin = testin.view(-1, 784)

        print( '===Epoch ' + str(i) + ':', accuracy(nnet, testin, testTar), '======')

        nnet.trainEpoch(dataLoader)







from dataHelpers import getMNIST, getMNIST_test, getLoaders

if __name__ == "__main__":
    # load the data:
    tr, blank = getLoaders(getMNIST(), 0.01, batch_size=100) #only using a small fraction of MNIST for each epoch
    ts, blank = getLoaders(getMNIST_test(), 1, batch_size=10000)

    mlp = MLP()
    train( mlp, tr, ts)





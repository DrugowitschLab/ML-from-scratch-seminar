# A series of steps to go from a multilayer perceptron to a VAE:


## 1: Vanilla auto-encoder
- add a symmetric set of readout layers
- make the readout noninearity a sigmoid
- make the loss function the BCELoss


## 2: VAE 
- split the forward pass into encode, sample, and decode subroutines
    - encoding mean and logvariance of the sampling distribution seems to be standard

- define the full loss function
    - this should be: crossEntropy - 0.5 * ( 1+ logvar - mu^2 - var ).sum()
    - note the minus!

- torch.randn_like will fit the shape of the passed tensor

- can use a single sample from z for training


### Some hacks that seem to prevent instability of the gradients
- remove bias terms on the encoder mean, and the encoder logvariance
- initialize readout weights for mean and sigma to be distributed uniformly rather than 


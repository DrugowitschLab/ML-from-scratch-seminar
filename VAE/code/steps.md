# A series of steps to go from a multilayer perceptron to a VAE:


## 1: Vanilla auto-encoder
- add a symmetric set of readout layers
- make the readout noninearity a sigmoid
- make the loss function the BCELoaa


## 2: VAE 
- split the forward pass into encode, sample, and decode subroutines
- define the full loss function
- torch.randn_like will fit the shape of the passed tensor
- can use a single sample from z

import torch
import numpy as np
import matplotlib.pyplot as plt


def showIm(data, ind=0):
    plt.imshow( data.view(-1, 28,28)[ind,:,:].detach().numpy(), cmap='gray')
    plt.show()


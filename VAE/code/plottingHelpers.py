import torch
import numpy as np
import matplotlib.pyplot as plt


def showIm(data, ind=0):
    plt.imshow( data.view(-1, 28,28)[ind,:,:].detach().numpy(), cmap='gray')
    plt.show()



#with torch.no_grad():
    #x = np.linspace(-4,4,21)
    #X = np.array(np.meshgrid(x,x)).T.reshape(-1,2)
    #sample = model.decode(torch.tensor(X.astype(float32)).to(device)).cpu()
    #from torchvision.utils import save_image
    #save_image(sample.view(-1, 1, 28, 28), 'results/grid.png', nrow=21)
    
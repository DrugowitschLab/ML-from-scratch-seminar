# utilities for loading data from MNIST

import torch, torchvision
import numpy as np


def getMNIST(directory='./MNIST'):
    ''' Fetches MNIST dataset to the specified directory'''
    MNIST = torchvision.datasets.MNIST(directory, train=True, download=True, transform=torchvision.transforms.ToTensor())
    MNIST.labels = MNIST.train_labels
    return MNIST



def getMNIST_test(directory='./MNIST'):
    ''' Fetches MNIST dataset to the specified directory'''
    MNIST = torchvision.datasets.MNIST(directory, train=False, download=True, transform=torchvision.transforms.ToTensor())
    MNIST.labels = MNIST.test_labels
    return MNIST



def getMNIST_rot(directory='./MNIST_rot'):
    '''Fetches rotated MNIST dataset'''
    MNIST = torchvision.datasets.MNIST(directory, train=True, download=True, transform=torchvision.transforms.Compose([
        torchvision.transforms.RandomRotation(180), torchvision.transforms.ToTensor()]) )
    MNIST.labels = MNIST.train_labels
    return MNIST



def getMNIST_sub(directory='./MNIST_sub'):
    '''Fetches subsampled MNIST dataset'''
    MNIST = torchvision.datasets.MNIST(directory, train=True, download=True, transform=torchvision.transforms.Compose([
        transforms.Resize((14,14)), torchvision.transforms.ToTensor()] ) )
    MNIST.labels = MNIST.train_labels
    return MNIST



def getLoaders(dataset, fracTr, classes=[], **kwargs):
    '''
    Returns a "training" and "testing" sampler for the dataset, possibly restricted to specific classes
    fracTr is the fraction of the data in the first loader.
    classes is the subset of labels that we are using

    '''

    lTr =  int( fracTr*dataset.labels.shape[0] )
    lTs = dataset.labels.shape[0] - lTr
    train, test = torch.utils.data.dataset.random_split( dataset, [lTr, lTs])


    toSample = torch.tensor( range(dataset.labels.shape[0]) )

    if classes:
        toSample = torch.nonzero( sum([ dataset.labels == tgt for tgt in classes] ) ).squeeze()


    indsTr = torch.tensor( np.intersect1d( toSample, train.indices ) )
    indsTs = torch.tensor( np.intersect1d( toSample, test.indices ) )


    trSample = torch.utils.data.SubsetRandomSampler(indsTr)
    tsSample = torch.utils.data.SubsetRandomSampler(indsTs)


    loaderTr = torch.utils.data.DataLoader(dataset, sampler=trSample ,**kwargs)
    loaderTs = torch.utils.data.DataLoader(dataset, sampler=tsSample ,**kwargs)

    return loaderTr, loaderTs











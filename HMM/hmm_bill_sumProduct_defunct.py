#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm as normal

np.random.seed(12345)

# ML from scratch
class hmm:
    def __init__(self,n,A,p,mu,sig):
        self.n = n
        self._A = []
        self._p = []
        self._mu = []
        self._sig = []
        self.A = np.array(A)
        self.p = np.array(p)
        self.mu = np.array(mu)
        self.sig = np.array(sig)
        self.h = [None]
        self.x = [None]
        self.steps = [None]
        
    @property
    def mu(self):
        return self._mu[-1]
    @mu.setter
    def mu(self, val):
        self._mu.append(val)

    @property
    def sig(self):
        return self._sig[-1]
    @sig.setter
    def sig(self, val):
        self._sig.append(val)

    @property
    def A(self):
        return self._A[-1]
    @A.setter
    def A(self, val):
        self._A.append(val)

    @property
    def p(self):
        return self._p[-1]
    @p.setter
    def p(self, val):
        self._p.append(val)


    def sample(self,steps):
        self.steps = steps
        self.h = np.random.choice(self.n, size=steps, p=self.p)
        self.x = np.random.normal(loc=self.mu[self.h[0]],scale=self.sig[self.h[0]],size=steps)
        for i in range(steps-1):
            self.h[i+1] = np.random.choice(self.n,size=1,p=self.A[:][self.h[i]])
            self.x[i+1] = np.random.normal(loc=self.mu[self.h[i+1]],scale=self.sig[self.h[i+1]],size=1)
        return self.h, self.x
    
    def fit(self,x_obs,iter_max):
        # initialized your marginals for hidden state
        self.steps = len(x_obs)
        self.h_marginal = np.zeros(self.steps)
        delta_curr = np.zeros(1)
        iter_curr = 0
        while iter_curr<iter_max:
        # E-step:
            self.h_marginal = self._E_step()
        # M-step
            self._M_step(x_obs)
            
            #delta_curr = None # likelihood difference
            iter_curr+=1
        return
    
    def _forward(self):
        alpha = np.zeros((self.n,self.steps))
        for t in range(self.steps):
            for i in range(self.n):
                px = normal.pdf(X[t], loc=self.mu[i], scale=self.sig[i])
                if t == 0:
                    alpha[i,t] = px * p[i]
                else:
                    alpha[i,t] = A[i,:] @ alpha[:,t-1] * px
        return alpha
    
    def _backward(self):
        beta = np.ones((self.n,self.steps))
        for t in reversed(range(self.steps)):
            for i in range(self.n):
                if t == self.steps - 1:
                    beta[i,t] = 1.
                else:
                    px = np.array([normal.pdf(X[t+1], loc=self.mu[j], scale=self.sig[j]) for j in range(self.n)])
                    beta[i,t] = (px * beta[:,t+1]) @ A[:,i] 
        return beta
    
    def _M_step(self, x_obs):
        hm = self._E_step()
        self.mu = (hm * x_obs).sum(1) / hm.sum(1)
        self.sig = np.sqrt( (hm * ( x_obs - self.mu[:,None] )**2).sum(1) / hm.sum(1)  )
        return
    
    def _E_step(self):
        self.h_marginal = self._forward() * self._backward()
        self.h_marginal /= self.h_marginal.sum(0)
        return self.h_marginal


A = np.array([[0.95,0.05],[0.05,0.95]])
p = [0.1,0.9]
mu = [0., 1.]
sig = [0.1,0.1]
myhmm = hmm(2,A,p,mu,sig)


# scamble
myhmm.mu = np.array([-0.1, 1.1])
#myhmm.sig = np.array([0.1, 0.1])

H,X = myhmm.sample(100)
plt.plot(X)
plt.plot(H)
hm = myhmm._E_step()
plt.plot(hm.argmax(0)+0.1, 'r', lw=1)
plt.show()





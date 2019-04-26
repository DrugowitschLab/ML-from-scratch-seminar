#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm as normal

np.random.seed(92345)

# ML from scratch
class HMM:
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
        self._mu.append(np.copy(val))

    @property
    def sig(self):
        return self._sig[-1]
    @sig.setter
    def sig(self, val):
        self._sig.append(np.copy(val))

    @property
    def A(self):
        return self._A[-1]
    @A.setter
    def A(self, val):
        self._A.append(np.copy(val))

    @property
    def p(self):
        return self._p[-1]
    @p.setter
    def p(self, val):
        self._p.append(np.copy(val))


    def sample_data(self,steps):
        self.steps = steps
        self.h = np.random.choice(self.n, size=steps, p=self.p)
        self.x = np.random.normal(loc=self.mu[self.h[0]],scale=self.sig[self.h[0]],size=steps)
        for i in range(steps-1):
            self.h[i+1] = np.random.choice(self.n,size=1,p=self.A[:,self.h[i]])
            self.x[i+1] = np.random.normal(loc=self.mu[self.h[i+1]],scale=self.sig[self.h[i+1]],size=1)
        # THIS IS THE CURRENT SAMPLE OF THE HIDDENS
        self.H = np.zeros((self.n, self.steps))
        for t in range(steps):
            self.H[self.h[t], t] = 1
        return self.h, self.x

    def resample_one_latent(self, t, xt):
        px = np.array([ normal.pdf(xt, loc=self.mu[i], scale=self.sig[i]) for i in range(self.n) ])
        phh = ((self.A @ self.H[:,t-1]) if t > 0 else 1) * ((self.A.T @ self.H[:,t+1]) if t < self.steps-1 else 1)
        ph = phh * px
        ph /= ph.sum()
        #print(ph)
        self.H[:,t] = np.random.multinomial(1, ph)


    def resample_all(self, x_obs, reps=1):
        ts = np.arange(self.steps)
        for r in range(reps):
            np.random.shuffle(ts)
            for t in ts:
                self.resample_one_latent(t, x_obs[t])

    def M_step(self, x_obs, eta=0.001):
        # mu
        grad_mu = np.sum(self.H * (x_obs - self.mu[:,None])/self.sig[:,None]**2, axis=1)
        # sig^2
        grad_var = np.sum(self.H * ( (x_obs - self.mu[:,None])**2/self.sig[:,None]**2 - 1)/2/self.sig[:,None]**2, axis=1)
        # A
        grad_A = np.zeros(self.A.shape)
        for t in range(self.steps-1):
            i,j = self.H[:,t+1].argmax(), self.H[:,t].argmax()
            grad_A[i,j] += 1
        grad_A /= grad_A.sum(0)
        grad_A -= self.A
        # Apply updates
        self.mu = self.mu + eta * grad_mu
        self.sig = np.sqrt(self.sig**2 + eta/10 * grad_var)
        self.A = (self.A + 1000*eta * grad_A) / (self.A + 1000*eta * grad_A).sum(0)

    


# GROUND TRUTH PARAMETERS
A = np.array([[0.9,0.05],
              [0.1,0.95]])
p = [0.1,0.9]
mu = [0., 1.]
sig = [0.45,0.55]

# Generate HMM and data
hmm = HMM(2,A,p,mu,sig)
H,X = hmm.sample_data(1000)

# scamble the system
hmm.H[:] = np.random.multinomial(1, [1/hmm.n]*hmm.n, hmm.steps).T
hmm.mu = 0.3, 0.5
hmm.sig = 0.7, 0.7
hmm.A = np.array([[0.8,0.1],
                  [0.2,0.9]])


# Learn
R = 100
for r in range(R):
    print(".", end="", flush=True)
    hmm.resample_all(X, reps=5)            # sample-based E step
    hmm.M_step(X, eta=0.0004)

hmm._A = np.array(hmm._A)
# plot learning progress
plt.figure(); plt.plot(X, '0.7', lw=0.5); plt.plot(H, 'b', lw=1); plt.xlabel("Time"); plt.ylabel("H, X")
plt.plot(hmm.H.argmax(0), 'r:', lw=2)
plt.figure(); plt.plot(hmm._mu[1:]); plt.hlines(hmm._mu[0], 0, R); plt.xlabel("Reps"); plt.ylabel("mu") 
plt.figure(); plt.plot(hmm._sig[1:]); plt.hlines(hmm._sig[0], 0, R); plt.xlabel("Reps"); plt.ylabel("sig") 
plt.figure(); plt.plot(hmm._A[1:].reshape(R+1,-1)); plt.hlines(hmm._A[0].flatten(), 0, R); plt.xlabel("Reps"); plt.ylabel("A") 

plt.show()

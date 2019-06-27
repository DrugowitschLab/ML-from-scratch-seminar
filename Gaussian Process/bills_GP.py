import autograd.numpy as np
import pylab as pl
np.random.seed(2837)


N = 21
f_true = lambda x: np.sin(x)
sig_obs = 0.2
X = np.linspace(-2*np.pi, 2*np.pi, N)
Y = f_true(X) + np.random.normal(0, sig_obs, len(X))

eta = 0.01
theta0 = 0.3, 0.3

X_pred = np.linspace(-np.pi, np.pi, 2*N) + 0.2

#l = 2.
k = lambda x1,x2 : 1.**2 * np.exp(-(x1-x2)**2 / l**2)
#k = lambda x1,x2 : 0.5**2 * np.exp( -np.sin(x1-x2) / l**2 )
def build_k(*theta):
    k = lambda x1,x2 : theta[0]**2 * np.exp(-(x1-x2)**2 / theta[1]**2)
    return k

class GP(object):
    def __init__(self, k, sig2_obs=0.1**2):
        self.X_obs = None
        self.Y_obs = None
        self.k = k
        self.sig2_obs = sig2_obs
        
    def build_Sig(self, k, X1, X2):
        #Sig = np.zeros((len(X1),len(X2)))
        Sig = k(X1[:,None], X2)
        #for i,j in np.ndindex(*Sig.shape):
            #Sig[i,j] = k(X1[i], X2[j])
        return Sig

    def set_obs_data(self, X, Y):
        self.N = len(X)
        self.X_obs = np.array(X)
        self.Y_obs = np.array(Y)
        self.Sig_obs = self.build_Sig(self.k, X, X) + self.sig2_obs * np.eye(self.N)
        return self.Sig_obs

    def set_predict_points(self, X):
        self.M = len(X)
        self.X_pred = np.array(X)
        self.Sig_pred_internal = self.build_Sig(self.k, X, X)
        self.Sig_cross = self.build_Sig(self.k, X, self.X_obs)
        self.M = self.Sig_cross @ np.linalg.inv(self.Sig_obs)
        self.mu_pred = self.M @ self.Y_obs
        self.Sig_pred = self.Sig_pred_internal - self.M @ self.Sig_cross.T

    def sample_prediction(self):
        self.Y_pred = np.random.multivariate_normal(self.mu_pred, self.Sig_pred)
        return self.Y_pred

    def ll_obs_data(self, theta):
        k = build_k(*theta)
        X, Y = self.X_obs, self.Y_obs
        Sig = self.build_Sig(k, X, X) + self.sig2_obs * np.eye(self.N)
        ll = -0.5 * Y.T @ np.linalg.inv(Sig) @ Y - 0.5 * np.log(np.linalg.det(Sig))
        return ll


def train(f_ll, theta0, eta, T):
    from autograd import grad
    f_grad = lambda theta: - grad(f_ll)(theta)
    theta = np.array(theta0)
    print(" > t=0, theta=%s" % str(theta))
    for t in range(1, T+1):
        theta -= eta * f_grad(theta)
        print(" > t=%d, theta=%s" % (t, str(theta)))
    return theta

# BEFORE LEARNING
k = build_k(*theta0)
gp = GP(k, sig2_obs=sig_obs**2)
Sig_obs = gp.set_obs_data(X, Y)  
gp.set_predict_points(X_pred)

# PLOT TRAINING DATA AND PRE-LEARNING PREDICTION
pl.figure(1)
pl.plot(X, Y, 'bo', label="Data")
pl.plot(gp.X_pred, gp.mu_pred, 'b', lw=0.5)

#y = gp.sample_prediction()
#pl.plot(gp.X_pred, y, "or", ms=1.)
#y = gp.sample_prediction()
#pl.plot(gp.X_pred, y, "og", ms=1.)

# PLOT PRE-LEARNING COV MATRIX
pl.figure(2)
pl.imshow(Sig_obs)
pl.colorbar()

# TRAIN
theta = train(gp.ll_obs_data, theta0, eta, T=100)

# PLOT POST-LEARNING PREDICTION
pl.figure(1)
k2 = build_k(*theta)
gp2 = GP(k2, sig2_obs=sig_obs**2)
Sig_obs2 = gp2.set_obs_data(X, Y)  
gp2.set_predict_points(X_pred)
pl.plot(gp2.X_pred, gp2.mu_pred, 'g', lw=1.)

# PLOT POST-LEARNING COV MATRIX
pl.figure(3)
pl.imshow(Sig_obs2)
pl.colorbar()


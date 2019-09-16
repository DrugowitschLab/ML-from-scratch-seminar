import numpy as np
import pylab as pl
from scipy.special import expit as sigma
anorm = lambda T: np.abs(np.random.normal(0,1,T))

# # #  PARAM
seed = 12342        # random seed
T = 200             # data size
Eps = 2500               # epochs
SAVEEVERY = None

eta_d = 0.25 / T /4    # learning rate: dis.
eta_g = 0.25 / T /4    # learning rate: gen.

# md0, mg0 = 200., 0.0
md0, mg0 = 0., 10.  # VERY INTERESTING LEARNING DYNAMICS with G2

# Two very simple networks with one parameter each
D = lambda m: lambda x,y: sigma(y - m*x)
G1 = lambda m: lambda z: np.array([z, m*z])
G2 = lambda m: lambda z: np.array([z, 4*m*(z-m/2*z**2)])
G = G2

# Real data
Xreal = (lambda z: np.array([z, z**2]))(anorm(T))

# # # \Param

np.random.seed(seed)


def plot_discriminator(md, mappable=None):
    x = np.arange(0, 3.51, 0.1)
    y = np.arange(-3, 9.01, 0.1)
    xx, yy = np.meshgrid(x, y)
    d = D(md)(xx, yy)
    if mappable:
        mappable.set_data(d)
    else:
        kwargs = dict(cmap=pl.cm.RdYlGn, interpolation="bilinear", vmin=0, vmax=1, aspect="auto", origin="lower", alpha=0.3)
        ax = pl.gca()
        mappable = ax.imshow(d, extent=(-0.05, 3.55, -3.05, 9.05), **kwargs)
    return mappable

# Plotting at beginning
class Fig(object):
    def __init__(self):
        self.fig = pl.figure(figsize=(4,4))
        self.scr = pl.scatter(*Xreal, s=1, c='green')
        self.Z = anorm(T)
        self.scf = pl.scatter(*G(mg0)(self.Z), s=1, c='red')
        self.mappable = plot_discriminator(md0)
        self.ax = pl.gca()
        self.epoch = self.ax.text(0.05, 0.95, "Epoch", ha="left", va="baseline", transform=self.ax.transAxes)
        pl.xlabel("x"); pl.ylabel("y")
        pl.subplots_adjust(0.1, 0.1,0.98, 0.98)
        pl.draw()

    def update(self, md, mg, ep):
        self.scf.set_offsets( G(mg)(self.Z).T )
        plot_discriminator(md, mappable=self.mappable)
        self.epoch.set_text("Epoch: %5d" % ep)
        pl.draw()

fig = Fig()

# # #  Learning rulez
delta_md_real = lambda X,D: (D-1) * X   # X : inputs; D : discriminator outputs
delta_md_fake = lambda X,D: D * X       # X : inputs; D : discriminator outputs
delta_mg ={G1 : lambda m,Z,D: D * Z,       # Z : generating seeds; D : discriminator outputs
           G2 : lambda m,Z,D: D * 4*(Z-m*Z**2)}[G]

# # #  Training
Md = np.zeros(Eps + 1)
Mg = np.zeros(Eps + 1)
Md[0], Mg[0] = md0, mg0

for ep in range(Eps):
    if SAVEEVERY and ep % SAVEEVERY == 0:
        fig.update(Md[ep], Mg[ep], ep)
        fig.fig.savefig("fig/%05d.png" % (ep//max(1, SAVEEVERY)), dpi=150)
    # Train the discriminator
    Dreal = D(Md[ep])(*Xreal)           # Classify the real data
    Xfake = G(Mg[ep])(anorm(T))      # Generate fake images
    Dfake = D(Md[ep])(*Xfake)           # Classify the fake images
    dmd = eta_d/2 * ( delta_md_real(Xreal[0], Dreal).sum() + delta_md_fake(Xfake[0], Dfake).sum() )
    Md[ep+1] = Md[ep] + dmd
    # Train the generator
    Z = anorm(T)                     # This time we store the latent samples
    Dfake = D(Md[ep+1])(*G(Mg[ep])(Z))  # Classify via the updated D
    dmg = eta_g * delta_mg(Mg[ep], Z, Dfake).sum()
    Mg[ep+1] = Mg[ep] + dmg

# Plotting at end
fig.update(Md[Eps], Mg[Eps], Eps)
if SAVEEVERY:
    fig.fig.savefig("fig/%05d.png" % (Eps//SAVEEVERY), dpi=150)


fig2 = pl.figure(figsize=(4,3))
pl.plot(Md, 'g', label="Discriminator parameter")
pl.plot(Mg, 'r', label="Generator parameter")
pl.legend()
pl.xlabel("Epochs"); pl.ylabel("Parameter value")
pl.subplots_adjust(0.13, 0.13, 0.98, 0.98)

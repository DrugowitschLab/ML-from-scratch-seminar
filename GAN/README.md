# ML from scratch: GAN session

## Recommended readings

- A really nice overview: https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f
- Practical tips and tricks: https://github.com/soumith/ganhacks


## Session I structure (this is more for Shih-Yi and Johannes)

_[Johannes]_
- GAN idea, super high level, and "horse --> zebra.gif" example,
- Classical view of deep learning (MLPs) as _supervised training_ of a _discriminative model_.
- Recall advantages of generative models:
  * learning unlabeled data,
  * well-controlled, interpretable, explanatory probabilistic model,
  * naturally support Bayesian inference
  * inference on incomplete data,
  * robustness,
  * generalization.
- Recall difficulties of generative models:
  * typically, either inference is hard (e.g., inverting generative FF network), or
  * gradient-based learning is hard (e.g., deep Boltzmann machines),
  * further, discriminative networks often perform better (if their requirements are met).

- One solution: variational architecture with an encoder and a decoder network --> VAE.
- Today: also two feed-forward networks, but with a different interaction between them.

_[Shih-Yi]_
- Introduce and explain:
  * Network architecture(s),
  * Idea of their interaction,
  * Goodfellow algorithm,
  * GAN hacks
- Casting GANs as an MLP-based form of _unsupervised training_ of a _generative model_ over p(image, label)
  * closed-form objective function,
  * They play a two-player min-max game,
  * contrast to the above classical view.
- The dicriminator "implicitely" identifies a good loss function for the generative network.
- Even though being generative, GANs do not naturally support inference (but see Donahue, 2017: BiGAN)

_[Johannes]_
- Show minimal GAN example videos
- Reading the blog post and maybe Goodfellow paper

_[Shih-Yi]_
- Introduction to Tensorflow (today and tomorrow)

**Please install tensorflow (version 1.13.1) on your laptop.**



## Session II

### Goal

1. Learning datasets:
  *  two synthetic datasets: ring and ring-with-center
  * (Optional) MNIST with few digits
2. Questions to explore (for either of the above):
  * What latent representation has been learned (= which z get mapped to which x)?
  * What architecture properties determine good learning (e.g., wide vs. deep; number of latent sources)?
  * How does a poor discriminator affect learning of the generator?
  * How does a poor generator affect learning of the discriminator?
  * Is there a minimal, had-crafted network that could solve the task? And could this solution be learned by a GAN?

### Software
* We recommend using Tensorflow or PyTorch


# Diffusion generative models
### [Binxu Wang](https://scholar.harvard.edu/binxuw) and John Vastola

This session is on diffusion generative models, an approach to generating samples from distributions; it differs substantially from other approaches, like generative adversarial networks (GANs) and variational auto-encoders (VAEs). Notably, it was one of the core ingredients of OpenAI's recent [DALL·E 2](https://openai.com/dall-e-2/) system for converting natural language descriptions to detailed images.

Diffusion generative models use the following idea. Samples from some distribution (e.g. of images) are gradually corrupted with more and more noise until they become unrecognizable static—this is the 'diffusion'. We then learn to *reverse* this mapping, so that we can turn unrecognizable static into a sample from our distribution of interest. Because it's easy to sample unrecognizable static, the mapping allows us to easily sample from our target distribution.

We will focus on the absolute basics of diffusion generative modeling, and restrict ourselves mostly to toy examples involving analytically tractable distributions.

**Helpful blog posts**:

https://yang-song.github.io/blog/2021/score/

https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

**Relevant papers**:

[2021 Song et al.] [Score-Based Generative Modeling through Stochastic Differential Equations](https://openreview.net/forum?id=PxTIG12RRHS)


**Links to notebooks**:

Day 1: 

Day 2: 

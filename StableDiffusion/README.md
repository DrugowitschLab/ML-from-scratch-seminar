# Stable Diffusion
### [Binxu Wang](https://scholar.harvard.edu/binxuw) and [John Vastola](https://twitter.com/johnjvastola)

<p align="center">
<img src="https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/StableDiffusion/images/astro.png?raw=true" alt="drawing" width="200"/>
<img src="https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/StableDiffusion/images/ballerina_chasing_cat.png?raw=true" alt="drawing" width="200"/>
<img src="https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/StableDiffusion/images/lovely_cat.png?raw=true" alt="drawing" width="200"/>
<img src="https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/StableDiffusion/images/turtle3.png?raw=true" alt="drawing" width="200"/>
</p>

This session follows up on last time's discussion of [diffusion generative models](https://github.com/DrugowitschLab/ML-from-scratch-seminar/tree/master/DiffusionGenerativeModels). Models like [Stable Diffusion](https://stability.ai/blog/stable-diffusion-announcement) and [DALL·E 2](https://openai.com/dall-e-2/) have recently achieved spectacular successes in tasks like generating images from text. But going from the basic ideas of diffusion generative modeling to something that works as well as Stable Diffusion requires incorporating a number of extra moving parts. Our goal in this session is to talk about those, and to try to build something similar to Stable Diffusion ourselves.

These extra components include:
* a model for linking images and text (like [CLIP](https://github.com/openai/CLIP));
* a neural network architecture that incorporates the usual inductive biases we associate with images (i.e. a [U-Net](https://en.wikipedia.org/wiki/U-Net));
* an *attention* mechanism, which helps guide the image generation process and create more self-consistent results;
* a mechanism for *compressing* images, so that diffusion happens in a more tractable latent space rather than pixel space.

See the original paper by [Rombach et al.](https://ommer-lab.com/research/latent-diffusion-models/) (which directly led to Stable Diffusion) for more details.

## Links to notebooks

Day 1 

- diffusion playground: 

Day 2: 

- coding exercises: 
- coding solutions: 


## Helpful links and blog posts

Diffusion models in general
- What are Diffusion Models? | https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
- Generative Modeling by Estimating Gradients of the Data Distribution | https://yang-song.github.io/blog/2021/score/

Stable Diffusion
- The Illustrated Stable Diffusion | https://jalammar.github.io/illustrated-stable-diffusion/
- Annotated and simplified code for Stable Diffusion | https://nn.labml.ai/diffusion/stable_diffusion/model/unet.html

Attention and Transformers
- The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer/

## Relevant papers

[2022 Rombach et al.] [High-Resolution Image Synthesis With Latent Diffusion Models](https://arxiv.org/abs/2112.10752)

[2021 Song et al.] [Score-Based Generative Modeling through Stochastic Differential Equations](https://openreview.net/forum?id=PxTIG12RRHS)


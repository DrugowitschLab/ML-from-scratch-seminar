# Transformers
### [Binxu Wang](https://scholar.harvard.edu/binxuw) 

This session is on [**transformers**](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), a particular machine learning architecture that has been found to be extremely good at [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing), among other tasks. Transformers are the backbone of chatbots like [ChatGPT](https://openai.com/blog/chatgpt), and they have been [*so* successful](https://www.quantamagazine.org/will-transformers-take-over-artificial-intelligence-20220310/) that [people are at least taking seriously](https://cbmm.mit.edu/news-events/events/discussion-panel-transformers-vs-humans-ultimate-battle-general-intelligence) the possibility that they could provide the foundation for something approximating general intelligence. 

Transformers involve a specific repeated building block based on the idea of [QKV attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)) (query-key-value). Theoretically, it is not totally clear why the basic motif transformers use works so well; in addition to natural language processing, transformers can [model music](https://arxiv.org/abs/1809.04281), [perform the same image recognition tasks as convolutional neural networks](https://arxiv.org/abs/2108.08810), and even serve as [one possible architecture for diffusion models](https://arxiv.org/abs/2212.09748).

In this session, we will present the basic architecture, and work through a number of applications and examples together.

**NOTE:** see Binxu's repo here for the code/slides: https://github.com/Animadversio/TransformerFromScratch 

[Tutorial website](https://scholar.harvard.edu/binxuw/classes/machine-learning-scratch/materials/transformers) 

[Lecture slides (PDF)](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/binxuw/files/mlfs_tutorial_nlp_transformer_ssl_updated.pdf)

**Helpful blog posts**:

- Intro to transformers | [https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/)

**Relevant papers**:

[2027 Vaswani et al.] [Attention is All you Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)


**Links to notebooks**:

* Fundamentals
  * [Understanding Attention & Transformer](https://colab.research.google.com/drive/1ZuhA6khlWm57WGZ8i38JH-gc5aJrvpvs?usp=sharing) (no GPU required)
     * [Tutorial on Einstein summation rules](https://colab.research.google.com/drive/1mizzN7iRlS2Du5TJvv7Wz7ecKOnpHzrQ?usp=sharing)
  * [Language modelling with transformer](https://colab.research.google.com/drive/1zZYzAopL__LW4glruSF9lnZYlEmSVI8j?usp=sharing) (CPU or GPU)
* Beyond Language 
  * **All the following notebooks include training transformer, shall be run with GPU runtime or the training takes too long.**
  * [Learn to do arithmetics by sequence modelling.](https://colab.research.google.com/drive/1vO71-o-8-3IrOe44Ha0nsHmUsEGVSC37?usp=sharing) (Simple, GPU Training ~ 10 min)
  * [Image generation by sequence modelling.](https://colab.research.google.com/drive/1UHlEbepqdvk68cYV1fvkmWl2TBKXfm8E?usp=sharing) (Simple, GPU Training ~ 10 ~ 20 min)
  * ~~[Audio signal classification](https://colab.research.google.com/drive/1O4XHOJyOu3_lyaPHAKJM_XTztrAb7VFP?usp=sharing) (Medium, GPU Training ~  20 min)~~ (WARNING: currently, there is a dependency install error, don't run on Colab.) 
  * [Image classification](https://colab.research.google.com/drive/1JDQQlLMGzo675AfrtkFn1kbuADtVemJz?usp=sharing) (Medium, GPU Training ~  30 min)
  * [Music generation by sequence modelling.](https://colab.research.google.com/drive/14zpzLpR4UBIzEQmeaXlMv_mDFYIv3Vht?usp=sharing) (Difficult, GPU Training takes hrs)
* Large Language Model
  * [OpenAI API and Chat with PDF](https://colab.research.google.com/drive/19mYEyavBhOnAbEQJQuztXAxWxyYbsQzi?usp=sharing) (Simple, no GPU needed, ~5mins)

![](media/ChatPDF_Schematics.png)

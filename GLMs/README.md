# Generalized linear models
### [John Vastola](https://johnvastola.com) and [Kiah Hardcastle](https://www.kiahhardcastle.info/home)

<p align="center">
<img src="https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/GLMs/header_pic.png?raw=true" alt="Hardcastle et al. 2017 tuning curves" width="550"/>
</p>

In neuroscience, statistical models are essential for making sense of the complex link between neural activity and things in the world (e.g., animal behavior). Among the most useful statistical models are linear ones, because (i) they are simple, and (ii) they are interpretable. [Generalized linear models](https://en.wikipedia.org/wiki/Generalized_linear_model) (GLMs), not to be confused with [general linear models](https://en.wikipedia.org/wiki/General_linear_model), are a slight complexification of the idea of linear models, and are widely applied in neuroscience. In this session, our goal is to cover the basic theory and a simple application to real neural data. 

-------------------

## Learn the basics!

**Lecture notes:** [link](https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/GLMs/glm-notes.pdf)

**Slides:** link

## Test your skills!
Note: please use the Colab links if you don't want to worry about having your own Python environment properly configured. On the other hand, this exercise only uses standard packages (numpy, scipy, matplotlib, pickle, time).

**Student exercise notebook**: [link](https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/GLMs/mlfs_GLM_student.ipynb)

**Student exercise notebook (Colab)**: [link](https://colab.research.google.com/drive/1vex-K9HGA-xKMSxN4tatH_B5jmoqnWYh)

**Student exercise notebook, hard mode**: [link](https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/GLMs/mlfs_GLM_student_HARDMODE.ipynb)    (note: this is for users who really want to do things 'from scratch')

## Check your work!

**Student notebook solutions:** [link](https://github.com/DrugowitschLab/ML-from-scratch-seminar/blob/master/GLMs/mlfs_GLM_student_solutions.ipynb)

**Student notebook solutions (Colab):** [link](https://colab.research.google.com/drive/1SuzLXGuUjQDviSlsnCZrqYSOqhyegxF_)

----------

## Additional resources

See [here](https://github.com/sytseng/GLM_Tensorflow_2) for an extremely helpful GLM repo by [Shih-Yi Tseng](https://github.com/sytseng) that includes both high-quality code and GLM-related tutorials.

**Helpful tutorials**:

[2016 SFN tutorial on GLMs by Jesse Kaminsky and Jonathan Pillow](https://github.com/pillowlab/GLMspiketraintutorial_python)

[Neuromatch Academy GLM tutorial, part 1](https://compneuro.neuromatch.io/tutorials/W1D3_GeneralizedLinearModels/student/W1D3_Tutorial1.html)

[Neuromatch Academy GLM tutorial, part 2](https://compneuro.neuromatch.io/tutorials/W1D3_GeneralizedLinearModels/student/W1D3_Tutorial2.html)


**Relevant papers, foundational**:

[1972 Nelder and Wedderburn] [Generalized Linear Models](https://www.jstor.org/stable/2344614), statistics paper that first introduced GLMs

[2005 Truccolo et al.] [A point process framework for relating neural spiking activity to spiking history, neural ensemble, and extrinsic covariate effects](https://pubmed.ncbi.nlm.nih.gov/15356183/), first major application of GLMs to neuroscience

[2008 Pillow et al.] [Spatio-temporal correlations and visual signalling in a complete neuronal population](https://www.nature.com/articles/nature07140), early application to macaque retina

**Relevant papers, modern applications of GLMs**

[2014 Park et al.] [Encoding and decoding in parietal cortex during sensorimotor decision-making](https://www.nature.com/articles/nn.3800), application to data from macaque lateral intraparietal area

[2017 Hardcastle et al.] [A Multiplexed, Heterogeneous, and Adaptive Code for Navigation in Medial Entorhinal Cortex](https://doi.org/10.1016/j.neuron.2017.03.025), application to data from mouse medial entorhinal cortex

[2022 Tseng and Chettih et al.] [Shared and specialized coding across posterior cortical areas for dynamic navigation decisions](https://doi.org/10.1016/j.neuron.2022.05.012), application to data from mouse posterior cortex


**Relevant papers, misc.**

[2017 Weber and Pillow] [Capturing the Dynamical Repertoire of Single Neurons with Generalized Linear Models](https://direct.mit.edu/neco/article-abstract/29/12/3260/8316/Capturing-the-Dynamical-Repertoire-of-Single), helpful discussion of relationship between neuroscience GLMs and biophysical neuron models

[2018 Zoltowski and Pillow] [Scaling the Poisson GLM to massive neural datasets through polynomial approximations](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3fab5890d8113d0b5a4178201dc842ad-Abstract.html), recent-ish paper scaling GLM fitting to large data sets


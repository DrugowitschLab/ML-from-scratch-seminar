# ML-from-scratch-seminar
This repository is part of the _Machine Learning from Scratch_ seminar in the Department of Neurobiology at Harvard Medical School.
In this seminar, a group of interested graduate students and postdocs develop minimal Python implementations of popular ML models. The primary goal is to exemplify the learning dynamics, strengths and limitations of the algorithms while keeping the involved computations "tractable".

Each topic is covered over two evenings. The first evening is theory-focused (how/why does this idea work?), while the second is a group coding session (can you hack together a basic implementation?). Food is provided.

The seminar was originally started and lovingly maintained by [Johannes Bill](https://billscientific.github.io/). 
The current organizer is [John Vastola](https://johnvastola.com). 

## List of past sessions

|     Dates                  |   Time   |     Chairs           |     Topic                       |
|:---------------------------|:---------|:--------------------:|:--------------------------------|
| Jan 30, 2019               | 5-7 p.m. | Johannes             | Kick-off meeting                |
| Feb 12-13 (Tue/Wed)        | 5-8 p.m. | Luke & Johannes      | Variational auto-encoders       |
| Apr 23+25 (Tue/Thu)        | 5-8 p.m. | Chong & Alex         | Hidden Markov Models            |
| Jun 26-27 (Wed/Thu)        | 5-8 p.m. | Selmaan              | Gaussian processes              |
| Sep 25-26 (Wed/Thu)        | 5-8 p.m. | Shih-Yi & Johannes   | Generative Adversarial Networks |
| Nov 20-21 (Wed/Thu)        | 5-8 p.m. | Seul Ah & Win        | Intro to Reinforcement Learning |
| Feb 12+19, 2020 (Wed/Wed)  | 5-8 p.m. | Anna K.              | Kalman & particle filters       |
| Apr 29+30, 2020 (Wed/Thu)  | 4-7 p.m. | Emma & Jeff          | Deep Reinforcement Learning     |
| COVID BREAK                | (⚈̥̥̥̥̥́⌢⚈̥̥̥̥̥̀)    |                      |                                 |
| Dec 15+16, 2021 (Wed/Thu)  | 5-8 p.m. | Alex & Johannes      | Bayesian Neural Nets & BBVI     |
| Mar  7+10, 2022 (Mon/Thu)  | 5-8 p.m. | John & Zach          | Actor Critic Methods for RL     |
| Jun 21+22, 2022 (Tue/Wed)  | 5-8 p.m. | Binxu & John         | Diffusion Generative Models     |
| Nov 1+2, 2022 (Tue/Wed)    | 5-8 p.m. | Binxu & John         | Stable Diffusion                |
| Apr 18+19, 2023 (Tue/Wed)  | 6-8:30 p.m. | Binxu          | Transformers                    |
| Feb 20+22, 2024 (Tue/Thu)  | 5-8 p.m. | John & Kiah   | [Generalized linear models](https://github.com/DrugowitschLab/ML-from-scratch-seminar/tree/master/GLMs) |


## Format of the seminar

Each session is chaired by 1 or 2 people.
Per session we discuss one machine learning model.
Each session consists of two sub-sessions on two late afternoons / evenings, e.g., Wed and Thu at 5 p.m.

**Day 1.** On the first day, the session chairs provide a brief (ideally 1 hour or less) introduction to the topic using white boards or slides.
The goal is for participants to get a sense of the theory behind the machine learning concept in question.

**Day 2.** On the second day, participants code important parts of the model themselves, usually inside an interactive Python 3 notebook. 
The coding task, which should be designed by the session chairs, should strike a balance between giving participants a sense of how the model works and being feasible within a few hours of coding. 
Ideally, ``*ML from scratch*'' means that we want to understand every computation; implementations need not be flexible or generic, but instead can be good enough for one or two toy tasks.

Ideally, everyone brings her/his own laptop.
Training time should not exceed 5 minutes on a standard desktop computer (w/o using GPUs).

People are invited to participate without committing to hosting a session. Regulars, however, may want to consider hosting at some point.

## Role of the session chair(s)
Each session is prepared by one or two session chairs.
The chairs have the following responsibilities:
  - Give an short introduction on the first day,
  - provide an instructive coding task for the second day (hosted here:  https://github.com/DrugowitschLab/ML-from-scratch-seminar),
  - provide the readings,
  - help others on theory and implementation questions,
  - announce any non-standard software requirements beforehand, so people can install them at home.

For the code, auto-diff packages and other little helpers are okay: the session chairs decide on what is the right balance between "from-scratch" and "black-box". Btw, a seemingly unlimited source of examples and code snippets can be found in the [``ML-From-Scratch'' repository of Erik Linder-Norén](https://github.com/eriklindernoren/ML-From-Scratch). (Fun fact: using the same name here is a coincidence!)

After the session, please share the material (notes, readings, reference implementations,...) in a new sub-directory on github. Contact John to get repo write access.

## Role of the organizer

The organizer (John Vastola) is also a participant, i.e., serves as a session chair from time to time.
Apart from that, the organizer helps scheduling the sessions, offers advice to the session chairs on the theory and when planning coding tasks, maintains the platform for document and code sharing, and takes care of ordering dinner.



## Some suggestions for future topics:

- Switching Linear Dynamical Systems
- LSTM/GRU
- ODE nets 
- Hierarchical Dirichlet Processes
- Natural Gradient Descent
- Graph Neural Networks
- Meta-learning (A neat small paper: https://paperswithcode.com/method/maml )
- Vector-symbolic architectures and their link to cognitive neuroscience (Some sources: https://arxiv.org/pdf/cs/0412059.pdf, https://arxiv.org/pdf/2001.11797.pdf, https://www.hd-computing.com/, https://bioengineeringcommunity.nature.com/posts/the-best-of-both-worlds-deep-learning-meets-vector-symbolic-ai )



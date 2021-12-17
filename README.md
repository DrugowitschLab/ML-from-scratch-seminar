# ML-from-scratch-seminar
This repository is part of the _Machine Learning from Scratch_ seminar in the Department of Neurobiology at Harvard Medical School.
In this seminar, a group of interested graduate students and postdocs develop minimal Python implementations of popular ML models. The primary goal is to exemplify the learning dynamics, strengths and limitations of the algorithms while keeping the involved computations "tractable".


## Outline of the format

Each session is chaired by 1 or 2 people.
Per session we discuss one machine learning model.
Each session consists of two sub-sessions on two late afternoons / evenings, e.g., Wed and Thu at 5 p.m.
We convene roughly every two months for a session.
The ideal group size is ~10 people.
Usually, we will meet in GB 422 (10 person capacity) or WAB 236 (larger room).

On day one, a brief (20-30min) introduction on the topic is given by the session chairs, using white boards or slides.
At the end of the introduction, readings on the theory are shared  which are studied by the class together over dinner.
(Post-Covid note: For the time being, dinner can only be eaten outside on the Quad.)
The collective reading session is a ``service'', not an obligation: Feel free to study the theory at home.
Readings could be provided as a PDF or simply as one or two URLs.
Some presenters have decided to use the reading session as a training opportunity for giving a full lecture on the white board.
You are, of course, very welcome to do so, but please be reminded that this is not expected.
In any case: Please keep the provided material concise and manageable for a 90 min reading session!
The day-one sub-session should not exceed 2 1/2 hours in total (incl. dinner).

On day two, we implement a minimal version of the model  using Python 3 and mainly standard libraries.
We aim for a conceptually clear realization of one particularly relevant model incarnation.
``*ML from scratch*'' means that we want to understand every computation.
Thus, we do not aim for an efficient implementation nor for generic / flexible solutions.
The implementation should just be good enough for application to one or two toy tasks.
These tasks (and the involved data sets) should be chosen such that distinguishing properties of the model
become apparent — ideally, highlighting also limitations of the model or algorithm.
The model implementation and its application to example tasks should be doable within ~3 hours.

Ideally, everyone brings her/his own laptop.
Packages for symbolic differentiation and prepared functions for data loading and data visualization can be used.
Training time should not exceed 5 minutes on a standard desktop computer (w/o using GPUs).

People are invited to participate without committing to hosting a session. Regular participants, however, may want to consider chairing at some point.

## Role of the session chair(s)
Each session is prepared by one or two session chairs.
The chairs have the following responsibilities:
  - Give an short introduction on the first day,
  - provide the readings,
  - help others on theory and implementation questions,
  - have an at least somewhat working reference implementation (can be copy-and-paste from a web blog),
  - announce any non-standard software requirements beforehand, so people can install them at home,
  - share data sets and auxiliary functions on our github repository: https://github.com/DrugowitschLab/ML-from-scratch-seminar,
  - identify instructive example tasks (= data sets + what to try out with them) for the coding session.

The last point will require the most preparation time as these examples are at the heart of the seminar.
Please, plan ahead and dedicate enough time to this point.

For the code, auto-diff packages and other little helpers are okay: the session chairs decide on what is the right balance between "from-scratch" and "black-box". Btw, a seemingly unlimited source of examples and code snippets can be found in the [``ML-From-Scratch'' repository of Erik Linder-Norén](https://github.com/eriklindernoren/ML-From-Scratch). (Ironically, I found this repository when googling for 'ml from scratch' after writing this document.)

When preparing the theory part on day one, in contrast, you can save time by relying heavily on existing web blogs, lecture slides, and other sources.
The primary goal of day one is *not* a comprehensive understanding of the theory. This would be too ambitious for a 2 hour meeting.
Rather we want to arrive at the specific equations which constitute the algorithm and need to be implemented.
Clearly highlighting these equations will facilitate everyone's implementation on day two.

After the session, please share the material (notes, readings, reference implementations,...) in a new sub-directory on github.
Our github repository has public read access and grants full write permissions to every participant.
To get write permissions, send your github username to Johannes (johannes _ bill AT hms DOT harvard DOT edu).

## Role of the organizer

The organizer (Johannes) is also a participant, i.e., serves as a session chair from time to time.
Apart from that, the organizer helps scheduling the sessions, offers advice to the session chairs on the theory and when planning coding tasks, maintains the platform for document and code sharing, and takes care of ordering dinner.


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
| Feb, 2022                  |          | John + ???           | T.B.A.                          |
|                            |          |                      |                                 |

## Some suggestions for future topics:

- Switching Linear Dynamical Systems
- LSTM/GRU
- ODE nets 
- Hierarchical Dirichlet Processes
- Natural Gradient Descent
- Graph Neural Networks



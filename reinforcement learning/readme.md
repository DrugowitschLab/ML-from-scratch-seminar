# Reinforcement learning

## Setting up a reinforcement learning evironment

It is recommended to use [anaconda](https://docs.conda.io/en/latest/miniconda.html) to manage python environments. Follow the installation instructions to use anaconda.

Create a new evironment: `conda create -n rl python=3.7`

Make sure you change your conda environment to the new `rl` environment you created above: `conda activate rl`

Then install Open AI's [gym package](http://gym.openai.com/docs/): `pip install gym`

Install jupyter to use notebooks: `pip install jupyter`

Other packages that are used:
```bash
pip install numpy seaborn matplotlib
```

Clone this reinforcement learning repository: `git clone https://github.com/wingillis/reinforcement-learning.git`. Make note of the location you saved this repository, because you will use this location in our notebooks.


## This session's topics

We will cover the the basics of reinforcement learning, including the following topics:

- value functions
- policies
- dynamic programming
- temporal difference learning

We will try to make it to some widely used and well-known control solutions for RL: SARSA and Q-learning.

A summary of each of these topics and be found in the repository you downloaded above, also [linked here](https://github.com/wingillis/reinforcement-learning#table-of-contents). Check out the first 5 entries in the repo's table of contents.


## Useful blog posts

- [this medium post describing a basic introduction to RL](https://towardsdatascience.com/introduction-to-reinforcement-learning-markov-decision-process-44c533ebf8da)
- [the follow-up post diving deeper into the Bellman equations](https://towardsdatascience.com/reinforcement-learning-markov-decision-process-part-2-96837c936ec3)
- [a nice summary of Q-learning, SARSA, TD learning, and others, complete with python code](https://towardsdatascience.com/reinforcement-learning-temporal-difference-sarsa-q-learning-expected-sarsa-on-python-9fecfda7467e)

## The videos shown in the lecture

- [RL agent complexity 1](https://openai.com/blog/emergent-tool-use/)
- [RL agent complexity 2](https://youtu.be/OBcjhp4KSgQ)
- [when rewards go wrong](https://www.youtube.com/watch?v=tlOIHko8ySg)

## Learning more on your own

- [David Silver's youtube lecture series](https://youtu.be/2pWv7GOvuf0) is a great place to get an in-depth understanding of RL
- [Sutton and Barto's reinforcement learning textbook](http://incompleteideas.net/book/bookdraft2018jan1.pdf) is widely used as a resource for RL


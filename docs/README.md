A dashboard is a useful tool to present data for reporting and exploration.
The added value is that a dashboard can be interactive. Python has several
frameworks to easily create dashboards, and you will learn about their
relative strengths and weaknesses based on some real-world use cases.


## Learning outcomes

When you complete this training you will

  * be able to create simple dashboards for reporting purposes;
  * be able to create simple web applications;
  * learn how to deploy dashboards on GitHub;
  * learn how to deploy web applications on streamlit.io;
  * learn how to deploy a web application on Amazon EC2;
  * know which libraries and frameworks to choose depending
    on your project requirements.


## Schedule

Total duration: 2 hours.

  | Subject                                     | Duration |
  |---------------------------------------------|----------|
  | introduction and motivation                 |  5 min.  |
  | panel                                       | 40 min.  |
  | deploying on GitHub                         | 10 min.  |
  | streamlit                                   | 40 min.  |
  | deploying on streamlit.io                   | 10 min.  |
  | Amazon EC2                                  | 10 min.  |
  | wrap up                                     |  5 min.  |


## Training materials

Slides are available in the
 [GitHub repository](https://github.com/gjbex/Python-dashboards),
as well as example code and hands-on material. The repository contains the
PowerPoint slide deck, examples for Panel, Streamlit, Dash, Gradio, and
ipywidgets, and hands-on starter material.


## Target audience

This training is for you if you need to use Python to build simple dashboards
or lightweight data applications.


## Prerequisites

You will need experience programming in Python. This is not a training that
starts from scratch. Familiarity with pandas is not required, but would be
beneficial.

If you plan to do Python programming in a Linux or HPC environment you should
be familiar with these as well.

More concretely, participants should already be comfortable with the following:

* running Python code in Jupyter notebooks or from the command line;
* variables, numbers, strings, booleans, and basic containers such as lists
  and dictionaries;
* `if`/`else` statements, `for` loops, and writing simple functions;
* importing modules and reading short Python scripts or notebook cells;
* basic NumPy usage such as creating arrays and applying simple vectorized
  operations;
* basic plotting with matplotlib, for example creating a line plot and setting
  labels;
* making small changes to example code and rerunning it.

You do not need prior experience with dashboard frameworks such as Panel,
Streamlit, Dash, Gradio, or ipywidgets. Those are part of the training itself.

### Quick self-assessment

If you can do most of the tasks below without looking up basic Python syntax,
you are likely ready for this training.

* write a function that computes values for a curve and plots them;
* create a NumPy array with evenly spaced values and apply a mathematical
  function to it;
* make a simple matplotlib plot and explain what the axes represent;
* read a short notebook cell that imports data or libraries, computes values,
  and plots a result;
* change a parameter in an example script or notebook and run it again;
* use a loop or function to organize a small piece of Python code;
* read a short traceback and identify roughly where the problem occurred.

If several of these items still feel difficult, the training will probably move
too fast. In that case, it is better to first refresh basic Python and simple
plotting with NumPy and matplotlib.

### Software and access requirements

To follow hands-on on your own system, you need a Python environment that can
run JupyterLab and the dashboard frameworks used in the examples.

More concretely, you need:

* a laptop or desktop with internet access;
* a Python environment with JupyterLab, Panel, Streamlit, Dash, Gradio,
  ipywidgets, NumPy, pandas, matplotlib, Altair, and related packages;
* the top-level `environment.yml` file if you want to create the portable conda
  environment;
* the `python_dashboards_linux64_conda_specs.txt` file if you need the recorded
  Linux conda package specification;
* a browser that can open local dashboard applications;
* access to Google Colaboratory if you prefer not to install software locally.

Some examples start local web applications with commands such as `panel serve`
or `streamlit run`. If you run these on a remote system, make sure you know how
to use port forwarding or the web-access mechanism provided by that system.

For the deployment parts of the training, you may also need accounts or access
for the relevant services, such as GitHub, Streamlit Community Cloud, or Amazon
EC2. These are not required for simply reading the examples.


## Level of the Material

For participants who already have basic Python programming experience, the
material in this training is approximately

* Introductory: 35 %
* Intermediate: 50 %
* Advanced: 15 %

These percentages describe the level of the dashboard and deployment topics
covered in the training, not the required entry level in Python itself.


## Trainer(s)

  * Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be))

---
theme:
  path: ../../.presenterm/theme.yaml
  override:
    footer:
      style: template
      right: "{current_slide} / {total_slides}"
options:
  list_item_newlines: 2
---


Deploying Applications
======================

To follow along, clone the course repo:

```bash
git clone https://github.com/dsc-courses/dsc190-tools-2026-sp.git
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Deploying Applications</span>**

Deploying
=========

- Let's say you have built a <span class="term">**data application**</span>.
    - E.g., a model, a visualization, etc.
- It runs on your machine in a Python notebook.
- How do you <span class="term">**deploy**</span> the app so that it can be used by others?

One Approach
============

- We have seen that *marimo* notebooks are easy to share.
- But often we want something more polished, easier to use.


---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Streamlit</span>**

Streamlit
=========

- **streamlit** is a Python library for building *web applications*.
- <span class="good">**Pro:**</span> very easy to go from Python code to a web app.
- <span class="bad">**Con:**</span> requires running a streamlit server to host the app.

Installation
============

Install with uv:

```bash
uv add streamlit
```

Streamlit
=========

- Streamlit provides functions for:
    - displaying text, images, plots, etc.
    - taking user input (e.g., text boxes, sliders, etc.)
- You define the layout of the app using Python code.
- Streamlit takes care of rendering the app in a web browser.


A First App
===========


```python
import streamlit as st

# display some text
st.title("Number Doubler")
st.write("Enter a number and I'll double it for you.")

# ask for input
number = st.number_input("Enter a number", value=0)

# this is just standard Python
doubled = number * 2

# display the result
st.write(f"{number} doubled is {doubled}.")
```

Running the App
===============

- Assume the previous was saved as "app.py".
- Run the app with:
```bash
streamlit run app.py
```

Note
====

- This starts a continually-running **server** that hosts the app.
- All of the computations are done in *Python*.
- If the server is stopped, the app will no longer work.

Demo 01
=======

- Run the app in Demo 01 and see what happens when the server is killed.


Example
=======

- **Goal**: predict risk for cardiovascular disease given age, sex, chest pain type, number of blood vessels colored by fluoroscopy, cholesterol level.
- You've trained a **decision tree** model using sklearn in a notebook.
- How can you share your model with doctors so that they can predict risk for their patients?

Idea
====

- We will use *pickle* to save the model to a file, and then load the model in a streamlit app to make predictions.

Demo 02
=======

Demo 02 contains code that trains a decision tree with sklearn and *pickles* the
model to a file: model.pkl.

Demo 03
=======

Demo 03 contains code for a streamlit app that loads the pickled model and uses
it to make predictions based on user input.

Deploying the App
=================

- Right now, this app is only running *locally*.
    - It isn't visible to others.
- To *deploy* the app, we need to host it on a streamlit server.
- There are some free options (with limitations):
    - Streamlit Community Cloud: https://streamlit.io/cloud
    - Hugging Face Spaces: https://huggingface.co/spaces

Deploying to Streamlit Community Cloud
======================================

0. Create a Streamlit Community Cloud account.
    - You can log in with your existing GitHub account.
1. Push app to a public GitHub repo.
2. Set up a new app on Streamlit Community Cloud and link it to your GitHub repo.

Limitations of Streamlit Community Cloud
=========================================

- Apps sleep after ~1 hour of inactivity; visitors must wait for restart.
- Shared CPU/memory.
- Limited number of deployed apps per workspace.

The Need for a Server
=====================

- Streamlit requires running a server to host the app.
- This costs *someone* money.
- While free options exist, they have limitations.
- Even paid options may not *scale* well.


---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Static Apps</span>**

Web App Architectures
=====================

- A *web app* is an application that runs in a web browser.
- Any non-trivial web app needs some way to execute code to respond to user input.
- There are two approaches:
    - **Server-side**: the code is executed on the server, and the results are sent to the client as HTML.
    - **Client-side**: the code is executed on the client's machine (in their browser) using JavaScript.

Static Apps
===========

- With streamlit, all computations are done *server-side* in Python.
    - This is a *centralized* architecture.
    - If there are 1 million users, the server must handle all 1 million requests.
- Alternatively, we could run the computations *client-side*, on the user's machine.
    - I.e., in their browser using *JavaScript*.
    - This is a *decentralized* architecture.
- Because this does not require executing code dynamically on the server,
    this is called a **static app**.
    - <span class="good">**Pro:**</span> it is much cheaper to host.
    - <span class="bad">**Con:**</span> it is not as straightforward, especially if the app is complex.

How?
====

- We trained our model using *sklearn*, a Python app.
- Don't we need sklearn to run the model?
<!-- pause -->
- No!
    - The model is just a mathematical function that takes in some numbers and
      outputs a prediction.
    - Once the model is trained, it can be implemented in any programming language, including JavaScript.


How?
====

- There exist tools for exporting sklearn models to common formats that can be used within JavaScript.
    - E.g., ONNX (Open Neural Network Exchange).
- But our model is a simple decision tree, which is easy to implement from scratch in JavaScript.
- *Especially* using coding agents.

Demo 04
=======

Using a coding agent, "port" the decision tree model from Python to a static JS
web app. 

Then, deploy using GitHub Pages.

Limitations
===========

- This approach requires us to "translate" the model from Python to JavaScript.
- By itself, almost any model can be implemented in JavaScript.
- But the *data preprocessing* steps may be more complex and difficult to implement in JavaScript.

- Next time: *dockerized* apps.

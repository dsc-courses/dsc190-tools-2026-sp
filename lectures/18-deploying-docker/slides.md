---
theme:
  path: ../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---


Deploying Dockerized Apps
=========================

To follow along, clone the course repo:

```bash
git clone https://github.com/dsc-courses/dsc190-tools-2026-sp.git
```

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

Demo 02
=======

Using a coding agent, "port" the decision tree model from Python to a static JS
web app. 

Then, deploy using GitHub Pages.

Limitations
===========

- This approach requires us to "translate" the model from Python to JavaScript.
- By itself, almost any model can be implemented in JavaScript.
- But the *data preprocessing* steps may be more complex and difficult to implement in JavaScript.


---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Serving an API</span>**

Deploying for Machine Use
=========================

- The previous approaches have been focused on deploying apps for *human* use.
- Often, we want to deploy a model so that it can be used by other *programs*.
- One approach: give them the code/model parameters.
    - <span class="bad">**Bad:**</span> exposes implementation details, may leak
    secrets
- Another approach: create an *API*.

What is an API?
===============

- An API (Application Programming Interface) is a standard way for programs to interact with each other.
- A *web API* is an API that is accessed over the web using HTTP requests.
    - Since every programming language can make HTTP requests, allows programs written in different languages to interact.
- Example: the Pokemon API (https://pokeapi.co/).

Creating APIs in Python
=======================

- *FastAPI* is a popular Python framework for creating web APIs.
- Install with:

```bash
uv add fastapi
```

Example: A first API
====================

- Suppose we've developed a Python library for computing the area of different shapes.
- We want to make this available via an API.

Example: A first API
====================

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/circle")
def circle(radius: float):
    return {"shape": "circle", "area": 3.1415 * radius**2}


@app.get("/rectangle")
def rectangle(width: float, height: float):
    return {"shape": "rectangle", "area": width * height}


@app.get("/triangle")
def triangle(base: float, height: float):
    return {"shape": "triangle", "area": 0.5 * base * height}
```

Example: A first API
====================

- Assuming this is saved as `app.py`, run (in development mode) with:

```bash
fastapi dev app.py
```

- Run in production mode with:

```bash
fastapi run app.py
```

Hosting a Model with FastAPI
============================

- We can use FastAPI to host our model as an API.
- See Demo 04.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Deploying with Docker</span>**

Deploying with Docker
=====================

- Our FastAPI app requires a server (just like our streamlit app).
- Unfortunately, there isn't (yet) a similar service like Streamlit Community Cloud.
    - FastAPI is creating one!
- Instead, we can deploy to a cloud provider by providing a Docker image.

Deploying with Docker
=====================

- Many cloud providers will host Docker images.
    - AWS, Google Cloud, Azure, Fly.io, etc.
- A *very* general approach.
    - Works for any language, framework, etc.
- We will start by building a Docker image for our FastAPI app.

Demo 05
=======

Demo 05 contains a Dockerfile for our FastAPI app. Build the image and run it
locally.

Deploying
=========

- We will deploy to Hugging Face Spaces.
- The process:
0. Register your public SSH key.
1. Create a new space and clone it.
2. Add a Dockerfile that builds your FastAPI app.
3. Push to Hugging Face.

Demo
====

Publish the app to Hugging Face Spaces.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">The End</span>**

The End
=======

- That's all for DSC 190 - Tools of the Trade.
    - Except for the final project...
- I will still have office hours on Friday, but at Noon (instead of 1pm).
- I hope the class was useful -- let me know!
- Keep in touch, have a good summer / life.

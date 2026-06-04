Final Project
=============

**Due**: Wednesday, June 10 (Late Deadline: Thursday, June 11)

We have spent this quarter learning the most-used "tools of the trade" in data
science: things like the *shell*, *git*, *DVC*, etc. Sometimes, however, the
most *useful* tools are the ones you make for yourself.

In this final project, you will write a tool that solves a problem in your life
(as a data scientist, student, or otherwise). The hope is that you will find
the tool useful beyond this project, and will continue to use and improve it in
the future. For that reason, the project is fairly open-ended, and will only
need to meet the requirements below.

To build the tool, it's recommended that you use your AI coding agent of
choice. In fact, one of the strongest applications of AI is in building the
simple-but-niche tools that previously would have gone unbuilt due to lack of
time.

Example Ideas
-------------

Here are some ideas to give you a sense for the kind of tools you could build
for this project:

1. **DSC Materials Search Engine**: A command-line tool for searching
   https://dsc-courses.github.io for specific topics. Useful for quickly
   finding relevant lectures, assignments, and readings when you're trying to
   review a topic or find a resource.

2. **UCSD Schedulizer**: A command-line tool that takes next quarter's class
   schedule as text and generates a file that can be imported into Google
   Calendar (or similar).

3. **Run Logger**. A command-line tool that you can use to log your runs.
   Record whatever you think is useful -- maybe the distance, time, route,
   weather, etc. Writes the data to a text file in your home directory.


Requirements
------------

To get full credit, your project should:

- Solve a non-trivial problem. No idea is too big or too small -- as long as
  it's something you find useful. However, the problem shouldn't be *trivial*.
  For example, your tool can't simply print the current time and still earn
  full credit. As long as you are attempting to create a genuinely useful tool,
  you should be in good shape. If you are unsure whether your idea is
  sufficiently non-trivial, feel free to ask on Campuswire or during office
  hours.
- Be hosted in a public GitHub repository. Your repository should have an
  organic commit history (it should not just be a single commit with the final
  code).
- Be written as a Python command-line tool.
- Be managed with `uv`, and should be installable with `uv add
  "git+https://github.com/<your-username>/<your-repo>.git`
- Be documented with a `README.md` of the following format, with the sections
  surrounded by `< >` replaced with your content.

```
# <Project Name>

<A short description of the tool and what problem it solves. Two or three
sentences should be enough.>

## Usage

<Instructions for how to use the tool. Give example commands, and explain what
they do.>

```

While you may of course use any of the tools we discussed in class (e.g.,
pytest and mypy), they are not *required* for this project. You can also use
any tool *not* discussed in class.

What to Submit
--------------

You will submit a single plain-text file named `repo_url.txt` to Gradescope.
The first line of this file should be the URL of your public GitHub repository,
for example:

```
https://github.com/your-username/your-repo
```

Grading
-------

Your project will be both manually and automatically graded. The autograder
will check that your public GitHub repo exists, that it has an organic commit
history and a `README.md` with the required sections, and that the tool can be
installed with `uv add "git+<your-url>"` and its command found and run. The
manual grading will check that the tool meets the above requirements and that
it solves a non-trivial problem.

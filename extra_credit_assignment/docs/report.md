# CMPU2032 - Programming & Algorithms 2 (2025/26) <br/> <p style="font-size:16pt; font-style: italic">Extra Credit Report</p>

<br/><br/>

**Student Name:** *Dwight Egerton*

**Student ID:** *D24127624*

**Release Date:** *16 April 2026*

**Submission Date:** *3 May 2026 @ 23:59*

<br/><br/>

---

## Overview

This is an extra credit assignment; although it is graded out of 10 marks, the overall course total remains capped at 100, so the maximum achievable overall mark will still be 100.

* **Task: Create a Python program using SQLite3**

    - Perform basic CRUD operations for a employee management system.

    - Buold an interfact to demonstrates these operations.


## Table of Contents

1. [Explanation of the data structures used](#explanation-of-the-data-structures-used)
2. [Description of sorting algorithms implemented](#description-of-sorting-algorithms-implemented)
3. [Test cases](#test-cases)
4. [Explanation of the design pattern selected](#explanation-of-the-design-pattern-selected)
5. [Sample outputs of the program](#sample-outputs-of-the-program)
6. [Setup and Execution](#setup-and-execution)

<div style="page-break-before:always"></div>

---

## Extra Credit Report

TBC




<div style="page-break-before:always"></div>

---

## Setup and Execution

### Create Virtual Environment

To ensure this project does not impact any other parts of your system, a virtual environment should be setup.
The assumption is that you have Python (version 3.11 or later) installed on your computer.
This can simple be done by executing the following commands: -

* Windows ...
```cmd
python -m venv .venv
.venv\Scripts\activate
```

* Mac, Linux or WSL ...
```bash
python3 -m venv .venv
source .venv/bin/activate
```

This can be done in other ways, for example: through your IDE or with tools like `pipx`.
Please refer to the respective documentation for any other approach you wish to follow.

### Install dependencies

This project uses `Poetry` for dependency management, building, running and testing.
Run the commands below to install `Poetry` into your Python virtual-environment as-well-as all the required project dependencies: -

```bash
pip3 install poetry
poetry install
```

<div style="page-break-before:always"></div>

---

### Launching the `Employee Management System` Application

To run the command-line interface: -

```bash
poerty run main
```

### Executing all Application Code Unit-Tests

To run the unit tests: -

```bash
poetry run tests
```


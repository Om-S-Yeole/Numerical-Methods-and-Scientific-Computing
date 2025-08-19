# Numerical Methods & Scientific Computing: A Production-Grade Python Library
### Course Project – MA5892
#### JUL-NOV 2025

---
**Author** : Om Satish Yeole   [![Static Badge](https://img.shields.io/badge/Linkedin-blue)](https://www.linkedin.com/in/om-yeole)

**Course Instructor** : Dr. Priyanka Shukla   [![Static Badge](https://img.shields.io/badge/Website-blue)](https://math.iitm.ac.in/innerfaculty.php?fname=Priyanka%20Shukla)

---

# A quick setup tour

### 1. Python Installation
You will need python version 3.12 or greater. Install it from [here](https://www.python.org/).

To check if python correctly installed, run this script in the terminal.
```bash
python --version
```

### 2. Clone the repository

Clone the repository and change the directory.

```bash
git clone https://github.com/Om-S-Yeole/Numerical-Methods-and-Scientific-Computing.git
```
```bash
cd Numerical-Methods-and-Scientific-Computing
```

### 3. Create a virtual environment

Create a python virtual environment. Here, we will be naming our virtual environment as "myenv".

```bash
python -m venv myenv
```

Activate the virtual environment

**For Windows**
```bash
myenv\Scripts\Activate
```
**For Mac and Linux**
```bash
source myenv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

Hurray! You are ready to start.

---

# Usage Guide: Numerical Integration via CLI, FastAPI Backend, and Streamlit UI

## 1. Command Line Interface (CLI)

You can use the CLI to compute numerical integration for a variety of functions and methods.

**Run the CLI:**
```bash
python cli/integrate.py <method> <function> <a> <b> [--grid_pts GP] [--n N] [--m M] [--req_time]
```
- `<method>`: trapezoidal, midpoint, simpson, romberg
- `<function>`: mathematical function as a string, e.g. "sin(x)", "x**2 + 3*x"
- `<a>`, `<b>`: lower and upper bounds
- `--grid_pts`: number of grid points (not for romberg)
- `--n`, `--m`: only for romberg method
- `--req_time`: display computation time

**Example:**
```bash
python cli/integrate.py trapezoidal "x**2" 0 1 --grid_pts 100 --req_time
python cli/integrate.py romberg "sin(x)" 0 3.14 --n 8 --m 5 --req_time
```

## 2. FastAPI Backend API

The backend exposes a REST API for integration calculation.

**Start the backend server:**
```bash
uvicorn app.main:app --reload
```

**API Endpoint:**
- POST `/api/v1/integrate`

**Request JSON (trapezoidal, midpoint, simpson):**
```json
{
  "method": "trapezoidal",
  "f": "x**2",
  "a": 0,
  "b": 1,
  "grid_pts": 100,
  "req_time": true
}
```
**Request JSON (romberg):**
```json
{
  "method": "romberg",
  "f": "sin(x)",
  "a": 0,
  "b": 3.14,
  "n": 5,
  "m": 5,
  "req_time": true
}
```
**Response:**
```json
{
  "integral": <float>,
  "req_time": <float>
}
```

## 3. Streamlit UI Frontend

The Streamlit UI provides a user-friendly interface for integration calculation.

**Start the frontend:**
```bash
python -m streamlit run .\ui\home.py
```

- Select the method, enter the function, bounds, and parameters.
- The UI will make API calls to the backend and display results.

**Note:** Ensure the backend is running before starting the frontend.

---

# How to Set Up and Use Backend & Frontend Together

1. **Start the FastAPI backend:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at `http://localhost:8000`.

2. **Start the Streamlit frontend:**
   ```bash
   python -m streamlit run .\ui\home.py
   ```
   The frontend will be available at `http://localhost:8501`.

3. **Use the frontend:**
   - Enter the function, select the method, and provide parameters.
   - The frontend will send requests to the backend and display the integration result and computation time.

---

# Numerical Integration Methods Available

The library currently supports the following numerical integration methods:

- **Trapezoidal Rule**
  - `trapezoidal(f, a, b, grid_pts=50)`
  - Approximates the integral by dividing the interval into grid points and applying the trapezoidal formula.

- **Midpoint Rule**
  - `midpoint(f, a, b, grid_pts=50)`
  - Approximates the integral using the midpoint of each subinterval.

- **Simpson's Rule**
  - `simpson(f, a, b, grid_pts=50)` (grid_pts must be even)
  - Approximates the integral using parabolic arcs over pairs of intervals.

- **Romberg Integration**
  - `romberg(f, a, b, n, m)`
  - Uses Richardson extrapolation on the trapezoidal rule for high-accuracy integration.

All methods accept functions of one variable (as a string or Python callable), bounds `a` and `b`, and method-specific parameters. Each returns the computed integral and optionally the computation time.

---

# API & CLI Supported Methods
- trapezoidal
- midpoint
- simpson
- romberg

---

# Testing

Unit tests for all methods and validators are provided in the `nmsc/methods/tests` and `nmsc/_utils/tests` folders. Run tests with:
```bash
pytest
```

---

# Contributing & Issues

Feel free to open issues or pull requests for improvements, bug fixes, or new features.

---

# Why Choose This Library?

**Numerical Methods & Scientific Computing** is a modern, production-grade Python library for numerical integration, built with a robust, modular, and extensible architecture. Here’s why it stands out:

- **Tech Stack:**
  - Python 3.12+
  - FastAPI (backend REST API)
  - Streamlit (frontend UI)
  - Pytest (unit testing)
  - Pydantic (validation)
  - Numpy, Scipy, Sympy (scientific computing)

- **Features:**
  - All major numerical integration methods: Trapezoidal, Midpoint, Simpson, Romberg
  - Fully tested with comprehensive unit tests for every method and validator
  - Modular codebase for easy extension and maintenance
  - Robust input validation using Pydantic and custom validators
  - CLI, REST API, and Streamlit UI for flexible usage
  - Clean separation of backend and frontend for scalable deployment
  - Handles symbolic math expressions and converts them to numerical functions
  - Designed for both educational and production use

- **Reliability:**
  - Every method is validated and tested for edge cases
  - Clear error messages and input checks to prevent misuse
  - Results include optional computation time for benchmarking

Whether you’re a student, researcher, or developer, this library provides a seamless experience for numerical integration in Python.
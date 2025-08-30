"""
24_modules_and_pip.py

This script demonstrates three different ways of working with modules in Python:

1. Built-in modules
   - Pre-installed with Python.
   - Example: using the math module to calculate the square root.

2. Custom modules
   - User-created Python files that can be imported.
   - Example: importing my_module.py which defines a custom greeting function.

3. Pip-installed packages
   - Third-party libraries installed via pip.
   - Example: using pyfiglet to generate ASCII art text.

Steps:
- Import the math module and compute the square root of a number.
- Import and call a function from a custom module (demo_module.py).
- Install pyfiglet using:  py -m pip install pyfiglet
- Use pyfiglet to display stylized ASCII text.

Purpose:
This exercise highlights how Python’s modular system allows developers to:
- Reuse existing code
- Organize projects efficiently
- Extend functionality through external libraries
"""

# 1️⃣ Built-in module example
import math
print("Square root of 16 using built-in math module:", math.sqrt(16))

# 2️⃣ Custom module example
from demo_module import greet
print(greet("Nef"))

# 3️⃣ Pip-installed package example
# I installed pyfiglet first thru command prompt: py -m pip install pyfiglet
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Python Demo")
print(ascii_banner)

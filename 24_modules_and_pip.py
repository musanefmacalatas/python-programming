# main.py

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

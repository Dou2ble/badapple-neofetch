import os
from os import system as run

from globals import *
from pathlib import Path

ascii_dir = Path("ascii").absolute()
asciis = os.listdir(ascii_dir)

for a in asciis:
    a_path = str(ascii_dir) + "/" + a
    print("neofetch --source " + str(a_path))
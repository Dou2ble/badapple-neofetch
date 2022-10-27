
import os
from os import system as run
from pathlib import Path

frames_path = Path("frames").absolute()
ascii_path = Path("ascii").absolute()
frames = os.listdir(frames_path)

for f in frames:
    run(f"jp2a --height=19 -v --background=dark --output={ascii_path}/{f}.txt {frames_path}/{f}")

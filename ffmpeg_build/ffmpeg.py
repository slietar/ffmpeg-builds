import os
from pathlib import Path


os.execl(Path(__file__) / "bin" / "ffmpeg", "ffmpeg")

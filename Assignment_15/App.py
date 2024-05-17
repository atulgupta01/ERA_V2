import gradio as gr
from detect import run

import argparse
import os
import platform
import sys
from pathlib import Path

import torch

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLO root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from detect import run


def inference(input_img):
    return run(source = input_img)
    
    
demo = gr.Interface(
    inference,
    inputs = [
        gr.Image(width=256, height = 256, label = "Input Image")
    ],
    outputs = [
        gr.Image(width=256, height = 256, label = "Output Image")
    ],
    title = "Yolo V9 trained on custom data set (Class = Tiger)",
    description = "A simple gradio application to test the Tiger Class for Yolo V9"
)

demo.launch(share=False)
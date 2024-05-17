import argparse
import os
import platform
import sys
from pathlib import Path
import numpy as np

import torch
from torchvision import transforms
from torch import Tensor

from models.common import DetectMultiBackend
from utils.dataloaders import LoadImages
from utils.general import (LOGGER, Profile, non_max_suppression, scale_boxes)
from utils.plots import Annotator, colors
from utils.torch_utils import select_device, smart_inference_mode
from utils.augmentations import letterbox


@smart_inference_mode()
def run(
        source = "Image-1.jpg",
        weights = "best.pt",
        data= 'customdata/data.yaml',
        imgsz=(640, 640),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        classes=None,  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        line_thickness=3  # bounding box thickness (pixels)
):
        
    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device)
    names = model.names

    print(names)
    
    # Dataloader
    bs = 1  # batch_size
    print("Original Image", source.shape, type(source))
    orig_image, ratio, (dw, dh) = letterbox(source)
    print("before transform", orig_image.shape, type(orig_image))
    transform = transforms.ToTensor()
    image = transform(orig_image)
    print("after transform, transformed image", image.shape, type(image))
    print("after transform, original image", orig_image.shape, type(orig_image))
    image = image.unsqueeze(0)
    print("after unsqueeze", image.shape, type(image))
    
    pred = model(image)
    
    if not isinstance(pred, Tensor):
        pred = pred[0][1] if isinstance(pred[0], list) else pred[0]
    
    pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

    names = model.names
    # Process predictions
    for i, det in enumerate(pred):  # per image
        annotator = Annotator(source, line_width=line_thickness, example=str(names))
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(image.shape[2:], det[:, :4], source.shape).round()

            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                label = f'{names[c]} {conf:.2f}'
                annotator.box_label(xyxy, label, color=colors(c, True))

        # Stream results
        return annotator.result()
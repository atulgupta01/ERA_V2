# YOLO V3

## Steps followed

1. Clone the directory from this github link - https://github.com/theschoolofai/YoloV3/
2. Remove Images and Label
3. Copy new Images and Labels from local computer
4. Replace the changed files -
	- utils/utils.py
	- utils/datasets.py
	- data\customdata\custom.data
	- data\customdata\custom.names
	- data\customdata\test.txt
	- data\customdata\train.txt
5. Create folder for weights
6. Copy the weights files
7. Execute training - python train.py --data data/customdata/custom.data --batch 20 --cache --cfg cfg/yolov3-custom.cfg --epochs 100 --nosave
8. Remove all the files from output folder
9. Execute detect.py - python detect.py --cfg cfg/yolov3-custom.cfg --weights weights/last.pt
10. Download the output folder - zip -r /content/output.zip /content/YoloV3/output

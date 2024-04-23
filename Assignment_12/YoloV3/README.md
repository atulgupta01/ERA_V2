# YOLO V3

## Steps followed

1. Clone the directory from this github link - https://github.com/theschoolofai/YoloV3/
2. Remove Images and Label
3. Copy new Images and Labels from local computer
4. Replace the changed files -
	- utils\utils.py (corrected error for np.int)
	- utils\datasets.py (corrected error for np.int and cuda)
	- data\customdata\custom.data
	- data\customdata\custom.names
	- data\customdata\test.txt
	- data\customdata\train.txt
5. Create folder for weights
6. Copy the weights files
7. Train the model -
**python train.py --data data/customdata/custom.data --batch 20 --cache --cfg cfg/yolov3-custom.cfg --epochs 100 --nosave**
9. Remove all the files from output folder
10. Test the model
**detect.py - python detect.py --cfg cfg/yolov3-custom.cfg --weights weights/last.pt**
12. Download the output folder - **zip -r /content/output.zip /content/YoloV3/output**

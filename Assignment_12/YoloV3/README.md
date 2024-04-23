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
10. Test the model - 
**detect.py - python detect.py --cfg cfg/yolov3-custom.cfg --weights weights/last.pt**
12. Download the output folder - **zip -r /content/output.zip /content/YoloV3/output**

# Details of Training and Testing

1. Used 100 images of "Tiger" for training the network.
2. Images had mix of following
   - Big Tiger Images i.e. close ups or Large Boxes
   - Small Tiger Images i.e. small boxes
   - Images from the back only
   - Multiple tigers in same images
   - Cubs and Tigers in same Image
   - Other animals with Tigers in Images
   - Humans and vehicles in background
4. Divided training and testing set 90-10
5. Trained the network for 100 epochs and received very good mAP@0.5 - 82%
6. Tested for all the images (i.e. training as well as testing)

# Important

- See here all the output images - https://github.com/atulgupta01/ERA_V2/tree/main/Assignment_12/output
- See here all the images used for training and testing and labels - https://github.com/atulgupta01/ERA_V2/tree/main/Assignment_12/YoloV3/data/customdata
- See here for the training log and detect log - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/Assignment_12.ipynb

# Images correctly predicted

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-10.jpg" alt="Resnet 18" width="150" height="150">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-103.jpg" alt="Resnet 18" width="150" height="150"> <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-104.jpg" alt="Resnet 18" width="150" height="150">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-80.jpg" alt="Resnet 18" width="150" height="150">

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-65.jpg" alt="Resnet 18" width="150" height="150">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-62.jpg" alt="Resnet 18" width="150" height="150">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-72.jpg" alt="Resnet 18" width="150" height="150">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-103.jpg" alt="Resnet 18" width="150" height="150">
	
# Images incorrectly predicted

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-13.jpg" alt="Resnet 18" width="200" height="200">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_12/output/Image-63.jpg" alt="Resnet 18" width="200" height="200">

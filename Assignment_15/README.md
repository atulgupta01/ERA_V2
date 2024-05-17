## Assignment 15

**Application Link** - https://huggingface.co/spaces/samatul/ERA_V2_S15

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/gradio_image.jpg" alt="Gradio App" width="600" height="350">

**Following files are changed in hugging face to create the app** - 
1. https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/App.py - **new** file
2. https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/detect.py - **modified** to suit current requirements
3. Other files are referenced from the original directory but no modifications - specifically in folders **model** and **util**
4. Reference to the **custom dataset** (used in assignment 12) - https://github.com/atulgupta01/ERA_V2/tree/main/Assignment_12/YoloV3/data/customdata

**Notebook used for training on the colab** - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/Assignment_15_colab.ipynb

**Notebook used for training on the EC2 Instance** - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/Assignment_15_EC2.ipynb

**Training on EC2 Image** (Trained for 40 epochs)

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2-Training.jpg" alt="EC2 Training" width="600" height="400">


### Results from the EC2 Run - https://github.com/atulgupta01/ERA_V2/tree/main/Assignment_15/EC2%20Run

**Confusion Matrix**

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/confusion_matrix.png" alt="Confusion Matrix" width="600" height="500">

**Results**

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/results.png" alt="Results" width="600" height="300">

**Training Batch Output**

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/train_batch0.jpg" alt="Training Batch" width="400" height="300">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/train_batch1.jpg" alt="Training Batch" width="400" height="300">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/train_batch2.jpg" alt="Training Batch" width="400" height="300">

**Validation Batch Output**

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/val_batch0_pred.jpg" alt="Validation Batch" width="400" height="300">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/val_batch1_pred.jpg" alt="Validation Batch" width="400" height="300">  <img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_15/EC2%20Run/val_batch2_pred.jpg" alt="Validation Batch" width="400" height="300">



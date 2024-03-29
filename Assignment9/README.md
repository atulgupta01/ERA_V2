## As part of the assignment-9, following files are submitted

1. Assignment9.ipynb - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment9/Assignment_9.ipynb
  * The file contains all the code for execution, training, and validation of the model
2. model.py - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment9/model.py
  * The file contains the model
3. util.py - https://github.com/atulgupta01/ERA_V2/blob/main/Assignment9/util.py
  * File contains the train transform, test transform, and data download utilities

## Important points
- Accuracy did not cross 70%. I trained for 100 epochs and then it crossed 70%. Current code has only 20 epochs and 66% accuracy on validation dataset
- Model has less than 200 K params
- Depthwise Separable Convolution - used
- Dilated Convolution - used
- albumentation - horizontal flip - used
- albumentation - shiftScaleRotate - used
- albumentation - coarseDropout - used

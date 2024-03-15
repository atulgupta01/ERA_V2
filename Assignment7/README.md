## Experiment1

### Targets: Copy the model from assignment 6 and train for 15 epochs and see the accuracy
### Results: 
* Num of Parameters - 13700
* Best Training Accuracy - 98.89
* Best Test Accuracy - 99.20

### Analysis:
* This model has high number of parameters. Hence need different model
* Dropout is 25% and Batch Normalization is after relu. This needs correction
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-1.ipynb
  * Model - Net1 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment2

### Targets: 
* Reduce the parameters to less than 8000
* Remove Dropout and Batch normalization
### Results: 
* Num of Parameters - 7950
* Best Training Accuracy - 98.69
* Best Test Accuracy - 99.59

### Analysis:
* This model has optimal number of parameters. But need to improve the model accuracy
* Not having dropout and batch normalization is impacting the model
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-2.ipynb
  * Model - Net2 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

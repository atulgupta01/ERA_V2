## Experiment-1

### Targets: 
* Copy the model from assignment 6 and train for 15 epochs and see the accuracy
### Results: 
* Num of Parameters - 13700
* Best Training Accuracy - 98.89
* Best Test Accuracy - 99.20

### Analysis:
* This model has high number of parameters. Hence need different model
* Dropout is 25% and Batch Normalization is after relu. This needs correction
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-1.ipynb
  * Model - Net1 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-2

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

## Experiment-3

### Targets: 
* Improve the model performance and hence add Batch normalization
### Results: 
* Num of Parameters - 8078
* Best Training Accuracy - 99.52
* Best Test Accuracy - 99.21

### Analysis:
* This model has slightly higher number of parameters.
* Training accuracy is decent, however it is overfitting. Adding a method to reduce the overfitting may help
* Try the same model with dropout in next iteration
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-3.ipynb
  * Model - Net3 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-3

### Targets: 
* Improve the model performance and hence add Batch normalization (before relu)
### Results: 
* Num of Parameters - 8078
* Best Training Accuracy - 99.52
* Best Test Accuracy - 99.21

### Analysis:
* This model has slightly higher number of parameters.
* Training accuracy is decent, however it is overfitting. Adding a method to reduce the overfitting may help
* Test Accuracy is not consistent
* Try the same model with dropout in next iteration
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-3.ipynb
  * Model - Net3 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-4

### Targets: 
* Reduce overfitting and hence add dropout after each layer
* Try with small dropout i.e. 0.05
* Slightly change parameters to reduce below 8000 (without changing number of layers i.e. few kernels)
### Results: 
* Num of Parameters - 7998
* Best Training Accuracy - 99.18
* Best Test Accuracy - 99.25

### Analysis:
* Overfitting is reduced and model is performing better so far
* Test Accuracy is not consistent but improving in last few epochs
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-4.ipynb
  * Model - Net4 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-5

### Targets: 
* Try global average pooling - different experiment to check how this experiment gives result
### Results: 
* Num of Parameters - 7984
* Best Training Accuracy - 99.21
* Best Test Accuracy - 99.27

### Analysis:
* No Overfitting
* Test Accuracy is not consistent
* Also training and test accuracy is stangnant.
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-5.ipynb
  * Model - Net5 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-6

### Targets: 
* Add random rotation to improve the accuracy to model 5
### Results: 
* Num of Parameters - 7984
* Best Training Accuracy - 98.96
* Best Test Accuracy - 99.25

### Analysis:
* No Overfitting
* Test Accuracy is consistent and crossed 99% in epoch 6
* Training accuracy did not improve in last few epochs
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-6.ipynb
  * Model - Net5 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-7

### Targets: 
* Add random rotation to improve the accuracy to model 4.
* Compare results of Model 4 and Model 5
### Results: 
* Num of Parameters - 7998
* Best Training Accuracy - 99.10
* Best Test Accuracy - 99.26

### Analysis:
* No Overfitting
* Test Accuracy is consistent and crossed 99.20% in epoch 7
* Training accuracy did not improve in last few epochs
* Difference between training and test is very small.
* Decided to training Model 5 instead of Model 4 - Play with the learning rate
  
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-7.ipynb
  * Model - Net4 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

## Experiment-8

### Targets: 
* Improve training and test accuracy by changing Learning rate
* Try different learning rates
### Results: 
* Num of Parameters - 7984
* Best Training Accuracy - 99.29
* Best Test Accuracy - 99.43

### Analysis:
* Did not try reducing LR from 0.1 and after 0.2, results were bad
* Kept Step Size as 5
* No Overfitting
* Test Accuracy is consistent and crossed 99.40% in epoch 8
* 
### File Link: https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/Assignment_7-8.ipynb
  * Model - Net5 in https://github.com/atulgupta01/ERA_V2/blob/main/Assignment7/model.py

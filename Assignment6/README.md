## Part-1

### Please refer to the following file for all the calculations related to backpropagation

    - Excel File - Class BP File.xlsx
    - Images for the excel - Excel-LR-<LR>.jpg i.e. Excel-LR-0.1.jpg
    - Images for the loss graph - Graph-LR-<LR>.jpg i.e. Graph-LR-0.1.jpg

![Graph1](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-0.1.jpg)|
|:--:|
| *Learning Rate = 0.1* |
![Graph2](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-0.2.jpg)|
| *Learning Rate = 0.2* |
![Graph3](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-0.5.jpg)|
| *Learning Rate = 0.5* |
![Graph4](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-0.8.jpg)|
| *Learning Rate = 0.8* |
![Graph5](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-1.jpg)|
| *Learning Rate = 1* |
![Graph6](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment6/Graph-LR-2.jpg)|
| *Learning Rate = 2* |

## Part-2

- File Name - Assignment_6.ipynb
- Highest Accuracy on test set - 99.44%
- Highest Accuracy achieved in epoch 17
- Total number of parameters - 13700
- Used Optimizer as SGD - Learning rate 0.01, Momentum - 0.9
- Used Scheduler - Step Size 15, Gamma - .1
  
#### Step Size was varied a few times between 10 to 15 to gain the accuracy 

### Following are the details of the network used
1. First Block - Conv, Relu, Batch Normalization and dropout(25%)
2. Second Block - Conv, Relu, Batch Normalization and dropout(25%)
3. Third Block - Max Pooling
4. Forth Block - Conv, Relu, Batch Normalization, and dropout(25%)
5. Fifth Block - Conv, Relu, Batch Normalization, and dropout(25%)
6. Sixth Block - Conv, Conv, Fully Connected Layer
7. Seventh Block - Softmax

#### Kept the block architecture the same but played around with the number of blocks
#### Batch size in the given file was 128 and did not try to change that
#### Achieved the results in the 9th iteration


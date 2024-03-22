## Assignment Details

* Assignment_8_BN - code for the Batch normalization
* Assignment_8_LN - code for the Layer normalization
* Assignment_8_GN - code for the Group normalization
* Each model contains less than 50,000 Parameters
* BN and GN models achieved more than 70% accuracy easily.
* LN could not achieve 70% Accuracy
* Used the Assignment 7 code and changed it to fit to CIFAR 10 dataset. No major changes in the file.
* Changed the model to fit to dataset size i.e. (3*32*32) and the parameter ranges.
* Following the suggested model - C1 C2 c3 P1 C4 C5 C6 c7 P2 C8 C9 C10 GAP c11


### Loss and Accuracy Plots
![BN_GRAPH](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Graph_BN.png)
|:--:|
| *Batch Normalization* |
![LN_GRAPH](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Graph_LN.png)
| *Layer Normalization* |
![GN_GRAPH](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Graph_GN.png)
| *Group Normalization* |

## Findings based on Graphs

1. The variation in error is much higher in Layer Normalization training and it could not reach 70% Accuracy
2. Training Accuracy has consistent falls in Group and Layer normalization.

### Error Images
![BN_ERROR](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Error_BN.png)
|:--:|
| *Batch Normalization* |
![LN_ERROR](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Error_LN.png)
| *Layer Normalization* |
![GN_ERROR](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment8/Error_GN.png)
| *Group Normalization* |

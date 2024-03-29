import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(
            # Block C1
            nn.Conv2d(3, 32, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Conv2d(32, 32, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Conv2d(32, 32, kernel_size=(3, 3), bias=False, padding = 1, stride = 2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.2),

            #Block C2
            nn.Conv2d(32, 32, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Conv2d(32,32, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Conv2d(32, 64, kernel_size=(3, 3), bias=False, padding = 1, dilation = 2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(64, 64, kernel_size=(3, 3), bias=False, padding = 1, stride = 2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.2),

            # Block C3
            nn.Conv2d(64, 128, kernel_size=(3, 3), bias=False, padding = 1, groups = 64),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(128, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 128),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),


            # Block C4
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(256, 256, kernel_size=(3, 3), bias=False, padding = 1, groups = 256),

            # Block C0
            nn.Conv2d(256, 32, kernel_size=(3, 3), bias=False, padding = 1),
            nn.Sequential(nn.AvgPool2d(kernel_size=6)),
            nn.Conv2d(32, 10, kernel_size=(1, 1), bias=False)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 10)
        x = F.log_softmax(x, dim=1)
        return x
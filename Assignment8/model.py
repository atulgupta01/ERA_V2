import torch
import torch.nn as nn
import torch.nn.functional as F

class Net1(nn.Module):
    def __init__(self):
        super(Net1, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(0.25),
            nn.Conv2d(16, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(0.25),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(0.25),
            nn.Conv2d(16, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(0.25),
            nn.Conv2d(16, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(0.25),
            nn.Conv2d(16, 16, 3),
            nn.Conv2d(16, 10, 1),
        )

        self.fc = nn.Sequential(
            nn.Linear(160, 10)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x

class Net2(nn.Module):
    def __init__(self):
        super(Net2, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3),
            nn.ReLU(),
            nn.Conv2d(16, 12, 3),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(12, 12, 3),
            nn.ReLU(),
            nn.Conv2d(12, 12, 3),
            nn.ReLU(),
            nn.Conv2d(12, 12, 3),
            nn.ReLU(),
            nn.Conv2d(12, 10, 3),
            nn.Conv2d(10, 6, 1),

        )

        self.fc = nn.Sequential(
            nn.Linear(96, 10)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x

class Net3(nn.Module):
    def __init__(self):
        super(Net3, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 12, 3),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(12, 12, 3),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Conv2d(12, 12, 3),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Conv2d(12, 12, 3),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Conv2d(12, 10, 3),
            nn.Conv2d(10, 6, 1),

        )

        self.fc = nn.Sequential(
            nn.Linear(96, 10)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x

class Net4(nn.Module):
    def __init__(self):
        super(Net4, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
			nn.Dropout(0.05),
            nn.Conv2d(16, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
			nn.Dropout(0.05),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(12, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
			nn.Dropout(0.05),
            nn.Conv2d(12, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
			nn.Dropout(0.05),
            nn.Conv2d(12, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Conv2d(12, 10, 3, bias=False),
            nn.Conv2d(10, 6, 1, bias=False),

        )

        self.fc = nn.Sequential(
            nn.Linear(96, 10)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x

class Net5(nn.Module):
    def __init__(self):
        super(Net5, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Dropout(0.05),
            nn.Conv2d(16, 16, 3, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Dropout(0.05),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Dropout(0.05),
            nn.Conv2d(12, 12, 3, bias=False),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.Conv2d(12, 20, 3, bias=False),
            nn.BatchNorm2d(20),
            nn.ReLU(),
            nn.Sequential(nn.AvgPool2d(kernel_size=6)),
            nn.Conv2d(20, 10, kernel_size=(1, 1), bias=False)
        )

        self.fc = nn.Sequential(
            nn.Linear(96, 10)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 10)
        x = F.log_softmax(x, dim=1)
        return x

class Net_BN(nn.Module):
    def __init__(self):
        super(Net_BN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(1, 1), bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(1, 1), bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=(3, 3), bias=False, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Sequential(nn.AvgPool2d(kernel_size=6)),
            nn.Conv2d(16, 10, kernel_size=(1, 1), bias=False)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 10)
        x = F.log_softmax(x, dim=1)
        return x

class Net_GN(nn.Module):
    def __init__(self):
        super(Net_GN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=(3, 3), bias=False),
            nn.GroupNorm(32, 32),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=(3, 3), bias=False),
            nn.GroupNorm(32, 32),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=(1, 1), bias=False),
            nn.GroupNorm(32, 32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 32, kernel_size=(3, 3), bias=False),
            nn.GroupNorm(32, 32),
            nn.ReLU(),
            nn.Conv2d(32, 24, kernel_size=(3, 3), bias=False, padding = 1),
            nn.GroupNorm(24,24),
            nn.ReLU(),
            nn.Conv2d(24, 24, kernel_size=(3, 3), bias=False, padding = 1),
            nn.GroupNorm(24,24),
            nn.ReLU(),
            nn.Conv2d(24, 24, kernel_size=(1, 1), bias=False),
            nn.GroupNorm(24, 24),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(24, 24, kernel_size=(3, 3), bias=False, padding = 1),
            nn.GroupNorm(24,24),
            nn.ReLU(),
            nn.Conv2d(24, 24, kernel_size=(3, 3), bias=False, padding = 1),
            nn.GroupNorm(24,24),
            nn.ReLU(),
            nn.Conv2d(24, 24, kernel_size=(3, 3), bias=False, padding = 1),
            nn.GroupNorm(24,24),
            nn.ReLU(),
            nn.Sequential(nn.AvgPool2d(kernel_size=6)),
            nn.Conv2d(24, 10, kernel_size=(1, 1), bias=False)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 10)
        x = F.log_softmax(x, dim=1)
        return x
        
class Net_LN(nn.Module):
    def __init__(self):
        super(Net_LN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 6, kernel_size=(3, 3), bias=False),
            nn.LayerNorm([6, 30, 30]),
            nn.ReLU(),
            nn.Conv2d(6, 6, kernel_size=(3, 3), bias=False),
            nn.LayerNorm([6, 28, 28]),
            nn.ReLU(),
            nn.Conv2d(6, 6, kernel_size=(1, 1), bias=False),
            nn.LayerNorm([6,28,28]),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 6, kernel_size=(3, 3), bias=False),
            nn.LayerNorm([6,12,12]),
            nn.ReLU(),
            nn.Conv2d(6, 8, kernel_size=(3, 3), bias=False, padding = 1),
            nn.LayerNorm([8,12,12]),
            nn.ReLU(),
            nn.Conv2d(8, 12, kernel_size=(3, 3), bias=False, padding = 1),
            nn.LayerNorm([12,12,12]),
            nn.ReLU(),
            nn.Conv2d(12, 12, kernel_size=(1, 1), bias=False),
            nn.LayerNorm([12,12,12]),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(12, 12, kernel_size=(3, 3), bias=False, padding = 1),
            nn.LayerNorm([12,6,6]),
            nn.ReLU(),
            nn.Conv2d(12, 12, kernel_size=(3, 3), bias=False, padding = 1),
            nn.LayerNorm([12,6,6]),
            nn.ReLU(),
            nn.Conv2d(12, 12, kernel_size=(3, 3), bias=False, padding = 1),
            nn.LayerNorm([12,6,6]),
            nn.ReLU(),
            nn.Sequential(nn.AvgPool2d(kernel_size=6)),
            nn.Conv2d(12, 10, kernel_size=(1, 1), bias=False)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 10)
        x = F.log_softmax(x, dim=1)
        return x
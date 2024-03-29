import cv2
import torchvision
import albumentations as A
from albumentations.pytorch import ToTensorV2

cv2.setNumThreads(0)
cv2.ocl.setUseOpenCL(False)


class Cifar10Dataset(torchvision.datasets.CIFAR10):
    def __init__(self, root="~/data/cifar10", train=True, download=True, transform=None):
        super().__init__(root=root, train=train, download=download, transform=transform)

    def __getitem__(self, index):
        image, label = self.data[index], self.targets[index]

        if self.transform is not None:
            transformed = self.transform(image=image)
            image = transformed["image"]

        return image, label

class args():

  def __init__(self,device = 'cpu' ,use_cuda = False) -> None:
    self.batch_size = 128
    self.device = device
    self.use_cuda = use_cuda
    self.kwargs = {'num_workers': 1, 'pin_memory': True} if self.use_cuda else {}

train_transforms = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.2, rotate_limit=20,
                             p=0.5,  border_mode=0, interpolation=4),
    A.CoarseDropout(max_holes = 1, max_height=.5, max_width=.5, min_holes = 1,
                    fill_value=([0.4914, 0.4822, 0.4465]), mask_fill_value = None),
    A.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010]),
    ToTensorV2(),
])

test_transforms = A.Compose([
    A.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010]),
    ToTensorV2(),
])


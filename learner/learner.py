from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
import torch
from torch import nn


class TrainingInformation:
    model: nn.Module or List[nn.Module]
    optim: torch.optim
    epochs: int

def get_torch_func(module, name):
    if module and name:
        return getattr(module, name)



class TrainingStrategy(ABC):

    @abstractmethod
    def epoch(self):
        pass

    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def validate(self):
        pass

class BaseStrategy(TrainingStrategy):
    def epoch(self):
        epoch_loss = 0.0
        for i, data in enumerate(self.trainloader, 0):
            loss = self.trainings_loop(i, data)
            epoch_loss += loss
        print("[%d] loss: %.3f" % (self.current_epoch, epoch_loss / self.epochs))
    
    def training(self, training_data):
        x, x_t = data, self.augment(data)
        self.optimizer.zero_grad()

        y_h = self.model(x)
        loss = self.criterion(y_h, y)
        loss.backward()

        self.optimizer.step()
        return loss.item

class BYOLStrategy(TrainingStrategy):
    def epoch(self, data):
        pass 

    def training(self):
        pass

    def validate(self):
        pass

class Learner():
    def __init__(self, strategy, data, **kwargs):
        self.data = data
        self.strategy = strategy
        self.__start_training()

    def __start_training(self):
        # self.test_run?
        for i in range(epochs):
            # self.before_epoch?
            self.current_epoch = i
            self.strategy.epoch(self.data)
            # self.after_epoch?
            if i + 1 % self.val_epoch == 0:
                self.strategy.validate()


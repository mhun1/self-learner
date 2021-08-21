from dataclasses import dataclass
from typing import List, Optional
from torch import nn, optim
from pydantic.dataclasses import dataclass

@dataclass
class TrainingInformation():
    model: nn.Module or List[nn.Module]
    optimizer: optim or List[optim]


m = nn.Sequential(nn.Linear(5,5), nn.Linear(5,5))
o = torch.optim.Adam(m.parameters())

b = 5
x = TrainingInformation(m,o)

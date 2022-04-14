from dataclasses import dataclass
from hashlib import new
from numpy import _2Tuple

from pandas import array

@dataclass
class new_dict():
    loss: int
    prediction_logits: int
    hidden_states: list
    attention: list

class model():
    
    def forward():
    
        return new_dict(
            loss = 1.2,
            prediction_logits=1.3,
            hidden_states=[2, 3, 4],
            attention=[10, 11, 2]
        )
        


    



arr_ = [1, 2, 3]


outputs = model.forward() # 이런 식으로 하면 tuple이 반환되어 slicing이 가능해짐 
print(outputs[:2]) # loss, logits : tuple 
# output[3] 하면 hidden states를 뽑을 수 있음 
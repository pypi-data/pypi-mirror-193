from cerebrium.models.base import BaseModel
from typing import List


class HFTransformer(BaseModel):
    def predict(self, input: List[any]) -> list:
        res = self.model(input)
        return res

from fastapi import FastAPI

from pydantic import BaseModel

import requests

app = FastAPI(title="Python Application")

class TensorClass(BaseModel):
  """
  TensorClass Type
  """
  instances : list[list[float]]

@app.get("/")
async def MainFile():
  """
  Main File Function
  """
  return {"result":"Main Python Application"}

@app.post("/logits")
async def GetResult(input_source : TensorClass):
  """
  Fastapi TensorFlow Serving Docker Compose

  >>> {"instances": [[5.0], [10.0]]}
  >>> {"instances": [[5.0], [58.0], [15.0], [45.0], [65.0]]}
  """
  url = "http://tensor:8501/v1/models/SimpleReg:predict"
  instances = {"instances":input_source.instances}
  content = {"Content-Type": "application/json"}
  response = requests.post(url, json=instances, headers=content)

  if response.status_code == 200:
    return response.json()
  else:
    return {"error":response.text}

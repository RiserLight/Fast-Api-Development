from fastapi import FastAPI ,Body, Response,status, Request, HTTPException
from pydantic import BaseModel, Field
from typing import Union,Optional,List


fake_db=[{"title":"Title of post 1","content":"Content of post ","id":1},{"title":"Title of post 1","content":"Content of post ","id":2},{"title":"Title of post 1","content":"Content of post ","id":3}
        , {"title":"Title of post 1","content":"Content of post ","id":4}]

app=FastAPI(
  docs_url="/v1/docs",
  openapi_url="/v1/openapi.json",
  title="Basic app of fastapi",
  description="Basic app of fastapi to understand the concepts",
  version="1.0"
)



class Post(BaseModel):
  title:str=Field(description="Title of post ",min_length=5, max_length=30)
  content:str=Field(description="Description of post",min_length=3,max_length=300)
  id:Union[int,None]=Field(description="Ration of post",default=None,gt=0)
  name:Optional[List[str]]=Field(description="Check",default=None)

@app.get("/")
def get(request:Request):
  print(dir(request))
  return {"message":"Hello World"}


@app.post("/create-post")
async def post(payload:Union[Post,None]=Body(default=None,description="Request body")):
  if payload:
    print(payload)
  else:
    print("Payload is none")
  return payload

# @app.post("/posts")
# async def post(payload:Post=Body(default=...,description="Request body")):
#   params=payload.dict()
#   print(params)
#   return params

@app.get("/posts")
async def get():
  return {"message":fake_db}

@app.post("/posts")
async def post(response:Response,payload:Post =Body(default=...,description="Create new post")):
  params=payload.model_dump()
  fake_db.append(params)
  print(dir(response))
  return {"data":params}

@app.get("/posts/{id}")
async def get_post_by_id(id:int,response:Response):
  for p in fake_db:
    if p.get("id")==id:
      response.status_code=status.HTTP_201_CREATED
      return {"data":p}
    
  # response.status_code=status.HTTP_404_NOT_FOUND
  # return {"data":[],"message":f"Detail not found for {id}"}
  # Cleaner way of doing this
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")

@app.delete("/post/{id}")
async def delete_post(id:int):
  pass
from fastapi import FastAPI,APIRouter,HTTPException
from config import collection
from database.schema import all_data
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime
# import logging

app=FastAPI()
# logging.basicConfig(level=logging.DEBUG)
router=APIRouter()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}


@router.get("/")
async def get_all_todos():
    data=collection.find()
    return all_data(data)

@router.post("/")
async def create_task(new_task:Todo):
    try:
        resp=collection.insert_one(dict(new_task))
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500,detail=f"Some error occured {e}")


# @router.put("/{task_id}")
# async def update_task(task_id:str,updated_task:Todo):
#     try:
#         id=ObjectId(task_id)
#         existing_doc=collection.find_one({"_id":id,"is_deleted":False})
#         if not existing_doc:
#             return HTTPException(status_code=404,detail=f"Task does not exists")
#         updated_task.updated_at=datetime.timestamp(datetime.now())
#         resp=collection.update_one({"_id":id},{"$set":dict(updated_task)})
#         return {"status_code":200,"message":"Task updated successfully"}
#     except Exception as e:
#         return HTTPException(status_code=500,detail=f"some error occured {e}")

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        # Convert task_id to ObjectId
        try:
            id = ObjectId(task_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid task ID format")

        # Fetch existing task
        existing_doc = collection.find_one({"_id": id, "is_deleted": {"$in": [False, None]}})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")

        # Update timestamp
        updated_task.updated_at = datetime.now().timestamp()

        # Prepare update dictionary (ignore None values)
        updated_data = {k: v for k, v in updated_task.dict().items() if v is not None}

        # Update task in MongoDB
        resp = collection.update_one({"_id": id}, {"$set": updated_data})

        # Check if update actually modified anything
        if resp.modified_count == 0:
            return {"status_code": 200, "message": "No changes detected"}

        return {"status_code": 200, "message": "Task updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.delete("/{task_id}")
async def delete_task(task_id:str):
    try:
        id=ObjectId(task_id)
        existing_doc=collection.find_one({"_id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code=404,detail=f"Task does not exists")
        resp=collection.update_one({"_id":id},{"$set":{"is_deleted":True}})
        return {"status_code":200,"message":"Task Deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=500,detail=f"some error occured {e}")


app.include_router(router)
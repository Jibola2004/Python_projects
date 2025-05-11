from firebase import db
from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from users import register_user, authenticate_user
from auth import create_access_token
from models import User,Token,TaskRead,TaskCreate,UserLogin
from database import Task



router = APIRouter()

# FastAPI app
app = FastAPI(title="📝 ToDo List API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



@app.post("/register", tags=["Auth"])
def register(user: User):
    register_user(user.email, user.username, user.password)
    return {"msg": "User registered successfully ✅"}




'''
@app.post("/login", response_model=Token, tags=["Auth"])
def login(user: User):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})

    # Store the active user in Firestore
    db.collection('active_users').document(access_token).set({
        'username': user.username
    })
    
    return {"access_token": access_token, "token_type": "bearer"}

'''
@app.post("/login", response_model=Token, tags=["Auth"])
def login(user: UserLogin):  # JSON input
    if not authenticate_user(user.username, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": user.username})

    # Store the active user in Firestore
    db.collection('active_users').document(access_token).set({
        'username': user.username
    })

    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Check if the token is in the active_users collection in Firestore
    user_ref = db.collection('active_users').document(token).get()
    if not user_ref.exists:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_ref.to_dict()['username']




@app.get("/tasks", response_model=list[TaskRead], tags=["Tasks"])
def get_tasks(user: str = Depends(get_current_user)):
    tasks_ref = db.collection('tasks').stream()
    tasks_list = []
    for task in tasks_ref:
        task_data = task.to_dict()
        completed = task_data.pop("completed", False)
        tasks_list.append(TaskRead(id=task.id, completed=completed, **task_data))
    return tasks_list





@app.post("/tasks", response_model=TaskRead, tags=["Tasks"])
def create_task(task: TaskCreate, user: str = Depends(get_current_user)):
     

    new_task_ref = db.collection('tasks').add(task.dict())

    new_task = Task(id=new_task_ref[1].id, **task.dict())
    return TaskRead(id=new_task.id, **new_task.to_dict())




@app.put("/tasks/{task_id}", response_model=TaskRead, tags=["Tasks"])
def update_task(task_id: str, task: TaskRead, user: str = Depends(get_current_user)):
    task_ref = db.collection('tasks').document(task_id)
    task_ref.update(task.dict(exclude={"id"}))
    updated_task = task_ref.get()
    return TaskRead(id=updated_task.id, **updated_task.to_dict())

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: str, user: str = Depends(get_current_user)):
    task_ref = db.collection('tasks').document(task_id)
    task_ref.delete()
    return {"message": "Task deleted"}

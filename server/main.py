from fastapi import FastAPI
from .routers.orders import router as orders_router
from .routers.plates import router as plates_router
from .routers.users import router as users_router
from .routers.token import router as token_router
from .routers.reviews import router as reviews_router
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(root_path='/api/', version="0.3.0")

app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(plates_router, prefix="/plates", tags=["plates"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(token_router, prefix="/token", tags=["token"])
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass

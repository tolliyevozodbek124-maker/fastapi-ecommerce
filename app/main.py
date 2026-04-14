from fastapi import FastAPI

from routers import router


app = FastAPI(title="Ecommerce")
app.include_router(router)

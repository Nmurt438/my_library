from fastapi import FastAPI
from routers.books import router as books_router 


app = FastAPI()

# Подключаем роутер к приложению
app.include_router(books_router)


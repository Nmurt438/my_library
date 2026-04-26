from fastapi import FastAPI, APIRouter, status, HTTPException
from schemas.books import SBookAdd, SBook

app = FastAPI()

router = APIRouter(prefix="/books")

books = []

@router.post("", response_model=SBookAdd, status_code=status.HTTP_201_CREATED)
async def post_book(book: SBook):
    books.append(book)
    return book

@router.get("", response_model=list[SBook], status_code=status.HTTP_200_OK)
async def get_books():
    return books

@router.get("/{id}", response_model=SBook, status_code=status.HTTP_200_OK)
async def get_one_book(id: int):
    if id < len(books):
        return books[id]
    raise HTTPException(status_code=404, detail="Книга не найдена")

@router.put("/{id}", response_model=SBookAdd)
async def update_books(id: int, book: SBook):
    if id < len(books):
        books[id] = book
        return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    if id < len(books):
        books.pop(id)
        return
    raise HTTPException(status_code=404, detail="Книга не найдена")

app.include_router(router)


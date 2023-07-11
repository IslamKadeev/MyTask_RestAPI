from fastapi import FastAPI

from database import create_database, check_database_connection
from routes.task import router as task_router


def create_app() -> FastAPI:
    app = FastAPI()

    # Подключение маршрутов
    app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

    # Создание базы данных
    create_database()
    check_database_connection()

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

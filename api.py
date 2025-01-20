import json
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Настройка логирования
logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(asctime)s - %(message)s')

app = FastAPI()

# Разрешаем запросы со всех адресов
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все источники
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/test")
async def test_endpoint(request: Request):
    # Получаем JSON-данные из запроса
    try:
        data = await request.json()
    except Exception as e:
        logging.error(f"Ошибка при получении JSON: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON")

    # Логируем полученные данные
    logging.info(f"Получен запрос: {data}")

    # Проверяем тип запроса
    if data.get("type") == "confirmation":
        group_id = data.get("group_id")
        if group_id == 229078408:
            return {"response": "e3b4a4bc"}
        else:
            raise HTTPException(status_code=400, detail="Invalid group_id")
    else:
        raise HTTPException(status_code=400, detail="Invalid type")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9010)
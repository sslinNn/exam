from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict
from ..database import get_db
from ..services.excel_upload import process_excel_file

router = APIRouter()

@router.post("/upload/{table_name}")
async def upload_excel(
    table_name: str,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Эндпоинт для загрузки Excel файла в указанную таблицу
    
    Args:
        table_name: Имя таблицы для сохранения данных
        file: Загруженный Excel файл
        db: Сессия базы данных
    
    Returns:
        Результат обработки файла
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(
            status_code=400,
            detail="Поддерживаются только файлы формата .xlsx или .xls"
        )
    
    # Здесь можно добавить маппинг колонок для конкретной таблицы
    # Пример маппинга:
    column_mapping = {
        "Имя": "name",
        "Возраст": "age",
        # Добавьте другие соответствия колонок
    }
    
    return await process_excel_file(
        file=file,
        db=db,
        table_name=table_name,
        column_mapping=column_mapping
    ) 
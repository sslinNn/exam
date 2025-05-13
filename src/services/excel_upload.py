from fastapi import UploadFile, HTTPException
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

async def process_excel_file(
    file: UploadFile,
    db: AsyncSession,
    table_name: str,
    column_mapping: Dict[str, str]
) -> Dict[str, Any]:
    """
    Обрабатывает загруженный Excel файл и сохраняет данные в БД
    
    Args:
        file: Загруженный файл
        db: Сессия базы данных
        table_name: Имя таблицы для сохранения данных
        column_mapping: Словарь соответствия колонок Excel и полей БД
    
    Returns:
        Dict с результатами обработки
    """
    try:
        # Читаем Excel файл
        df = pd.read_excel(file.file)
        
        # Переименовываем колонки согласно маппингу
        df = df.rename(columns=column_mapping)
        
        # Конвертируем DataFrame в список словарей
        records = df.to_dict('records')
        
        # Подготавливаем данные для вставки
        stmt = insert(table_name).values(records)
        
        # Выполняем вставку
        await db.execute(stmt)
        await db.commit()
        
        return {
            "status": "success",
            "message": f"Успешно загружено {len(records)} записей",
            "records_count": len(records)
        }
        
    except Exception as e:
        logger.error(f"Ошибка при обработке файла: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Ошибка при обработке файла: {str(e)}"
        )
    finally:
        await file.close() 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status
from src.database import get_db
from src.models.partners import Partners

router = APIRouter()

@router.get("/")
async def getAllPartners(db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Partners)
        result = await db.execute(stmt)
        return result.scalars().all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/{id}")
async def getPartner(id, db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Partners).where(Partners.id == id)
        result = await db.execute(stmt)
        return result.one_or_none()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/")
async def createPartner():
    return f""

@router.delete("/{id}")
async def deletePartner(id):
    return f""

@router.put("/{id}")
async def updatePartner(id):
    return f""


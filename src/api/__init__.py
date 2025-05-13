from fastapi import APIRouter

from src.api.partnersCrud import router as partners_router
from src.api.productsCrud import router as products_router
from src.api.excel_upload import router as excel_router

main_router = APIRouter()

main_router.include_router(partners_router, prefix="/partners", tags=["Партнеры"])
main_router.include_router(products_router, prefix="/products", tags=["Продукты"])
main_router.include_router(excel_router, prefix="/excel", tags=["Excel"])
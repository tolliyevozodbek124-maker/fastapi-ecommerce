from fastapi import APIRouter

from .user import router as user_router
from .category import router as category_router
from .product import router as product_router


router = APIRouter(prefix="/api")
router.include_router(user_router)
router.include_router(category_router)
router.include_router(product_router)

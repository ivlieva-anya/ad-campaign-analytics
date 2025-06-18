from fastapi import APIRouter

from backend.routers.articles.view import articles_router
from backend.routers.auth import auth_router
from backend.routers.users import user_router

router_routes = APIRouter()

router_routes.include_router(router=articles_router,tags=["articles"])
router_routes.include_router(router=auth_router,tags=["auth"])
router_routes.include_router(router=user_router,tags=["users"])
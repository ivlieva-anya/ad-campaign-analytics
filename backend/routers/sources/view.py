
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend import models, database, auth
from backend.routers.sources.dependencies import createSource, source_update, source_get_all, source_get_by_id, \
    source_get_by_name, source_update_last_scan
from backend.routers.sources.schemas import SourceCreate, Source, SourceUpdateLast

sources_router = APIRouter(
    prefix="/sources",
    tags=["sources"]
)


@sources_router.post("", response_model=Source)
async def create_source(
        source: SourceCreate,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    createSource(source, db, current_user)


@sources_router.get("", response_model=List[Source])
async def get_sources(
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    return source_get_all(db)


@sources_router.get("/{source_id}", response_model=Source)
async def get_source(
        source_id: int,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):

    return source_get_by_id(source_id,db)


@sources_router.get("/byname/{name}", response_model=Source)
async def get_source(
        name: str,
        db: Session = Depends(database.get_db),
        #current_user: models.User = Depends(auth.get_current_active_user)
):
    return source_get_by_name(name,db)


@sources_router.put("/{source_id}", response_model=Source)
async def update_source(
        source_id: int,
        source: SourceCreate,
        db: Session = Depends(database.get_db),
        # current_user: models.User = Depends(auth.get_current_active_user)
):
    source_update(source_id, source, db)
    #source_update_last_scan(source_id, source, db )


@sources_router.put("/last/{source_id}", response_model=Source)
async def update_source(
        source_id: int,
        source: SourceUpdateLast,
        db: Session = Depends(database.get_db),
        # current_user: models.User = Depends(auth.get_current_active_user)
):
    #source_update(source_id, source, db)
    source_update_last_scan(source_id, source, db )


@sources_router.delete("/{source_id}")
async def delete_source(
        source_id: int,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    db_source = db.query(models.Source).filter(
        models.Source.id == source_id,
        models.Source.user_id == current_user.id
    ).first()

    if not db_source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source not found"
        )

    try:
        db.delete(db_source)
        db.commit()
        return {"message": "Source deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not delete source"
        )
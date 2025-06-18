from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend import models, database, auth
from backend.routers.sources.schemas import SourceCreate, Source

sourcesnew_router = APIRouter(
    prefix="/sourcesnew",
    tags=["sourcesnew"]
)


@router.post("", response_model=Source)
async def create_source(
        source: SourceCreate,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    # Проверяем, существует ли источник с таким URL
    db_source = db.query(models.Source).filter(models.Source.url == source.url).first()
    if db_source:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Source with this URL already exists"
        )

    # Создаем новый источник
    db_source = models.Source(
        **source.model_dump(),
        user_id=current_user.id
    )

    try:
        db.add(db_source)
        db.commit()
        db.refresh(db_source)
        return db_source
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create source"
        )


@router.get("", response_model=List[Source])
async def get_sources(
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    sources = db.query(models.Source).filter(models.Source.user_id == current_user.id).all()
    return sources


@router.get("/{source_id}", response_model=Source)
async def get_source(
        source_id: int,
        db: Session = Depends(database.get_db),
        current_user: models.User = Depends(auth.get_current_active_user)
):
    source = db.query(models.Source).filter(
        models.Source.id == source_id,
        models.Source.user_id == current_user.id
    ).first()

    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source not found"
        )

    return source


@router.put("/{source_id}", response_model=Source)
async def update_source(
        source_id: int,
        source: SourceCreate,
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

    # Проверяем, не занят ли URL другим источником
    if source.url != db_source.url:
        existing_source = db.query(models.Source).filter(
            models.Source.url == source.url,
            models.Source.id != source_id
        ).first()
        if existing_source:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Source with this URL already exists"
            )

    # Обновляем данные источника
    for key, value in source.dict().items():
        setattr(db_source, key, value)

    try:
        db.commit()
        db.refresh(db_source)
        return db_source
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not update source"
        )


@router.delete("/{source_id}")
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
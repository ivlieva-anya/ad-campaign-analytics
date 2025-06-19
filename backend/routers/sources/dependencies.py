from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

from backend import models, database, auth


def source_get_all(db):
    return db.query(models.Source).all()


def source_get_by_url(url: str, db):
    source = db.query(models.Source).filter(models.Source.url == url).first()
    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source not found"
        )
    return source


def source_get_by_id(id: int, db):
    source = db.query(models.Source).filter(models.Source.id == id).first()
    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source not found"
        )
    return source


def source_get_by_name(name: str, db):
    source = db.query(models.Source).filter(models.Source.name == name).first()
    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source not found"
        )
    return source

def createSource(source, db, current_user):

    # Проверяем, существует ли источник с таким URL
    db_source = source_get_by_url(source.url, db)
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


def source_url_existing(source, source_id, db):
    existing_source = db.query(models.Source).filter(
        models.Source.url == source.url,
        models.Source.id != source_id
    ).first()
    if existing_source:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Source with this URL already exists"
        )
    return True

def source_update(source_id, source, db):

        db_source = source_get_by_id(source_id, db)

        # Проверяем, не занят ли URL другим источником
        if source.url != db_source.url:
            source_url_existing(source, source_id, db)
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


def source_update_last_scan(source_id, source, db):
    db_source = source_get_by_id(source_id, db)
    dt = datetime.now(timezone.utc).isoformat(timespec='microseconds')

    # Обновляем данные источника
    setattr(db_source, 'last_scan_date', dt)

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



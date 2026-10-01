from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import repository, schemas


def list_members(db: Session):
    return repository.get_all(db)


def get_member(db: Session, member_id: str):
    member = repository.get_by_id(db, member_id)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found",
        )
    return member


def create_member(db: Session, data: schemas.MemberCreate):
    return repository.create(db, data)


def update_member(db: Session, member_id: str, data: schemas.MemberUpdate):
    member = get_member(db, member_id)
    return repository.update(db, member, data)


def delete_member(db: Session, member_id: str):
    member = get_member(db, member_id)
    repository.delete(db, member)


def delete_all_members(db: Session):
    return repository.delete_all(db)

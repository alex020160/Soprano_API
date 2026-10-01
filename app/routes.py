from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from .database import get_db
from . import schemas, service

router = APIRouter(prefix="/api/members", tags=["members"])


@router.get("", response_model=list[schemas.MemberRead])
def get_members(db: Session = Depends(get_db)):
    return service.list_members(db)


@router.get("/{member_id}", response_model=schemas.MemberRead)
def get_member(member_id: str, db: Session = Depends(get_db)):
    return service.get_member(db, member_id)


@router.post("", response_model=schemas.MemberRead, status_code=status.HTTP_201_CREATED)
def create_member(data: schemas.MemberCreate, db: Session = Depends(get_db)):
    return service.create_member(db, data)


@router.patch("/{member_id}", response_model=schemas.MemberRead)
def update_member(
    member_id: str,
    data: schemas.MemberUpdate,
    db: Session = Depends(get_db),
):
    return service.update_member(db, member_id, data)


@router.put("/{member_id}", response_model=schemas.MemberRead)
def replace_member(
    member_id: str,
    data: schemas.MemberCreate,
    db: Session = Depends(get_db),
):
    update_data = schemas.MemberUpdate(**data.model_dump())
    return service.update_member(db, member_id, update_data)


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: str, db: Session = Depends(get_db)):
    service.delete_member(db, member_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("")
def delete_all_members(db: Session = Depends(get_db)):
    deleted = service.delete_all_members(db)
    return {"deleted": deleted}

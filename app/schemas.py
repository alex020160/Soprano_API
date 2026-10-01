from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

MemberStatus = Literal["active", "inactive", "deceased"]


class MemberCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    nickname: Optional[str] = Field(default=None, max_length=120)
    family: str = Field(min_length=1, max_length=120)
    rank: str = Field(min_length=1, max_length=80)
    status: MemberStatus = "active"


class MemberUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=120)
    nickname: Optional[str] = Field(default=None, max_length=120)
    family: Optional[str] = Field(default=None, min_length=1, max_length=120)
    rank: Optional[str] = Field(default=None, min_length=1, max_length=80)
    status: Optional[MemberStatus] = None


class MemberRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    nickname: Optional[str]
    family: str
    rank: str
    status: MemberStatus

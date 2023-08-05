from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from enums import UserStatus


class LoginDto(BaseModel):
    username: str
    password: str


class UserBaseDto(BaseModel):
    username: str
    email: str


class UserProfilePublicDto(UserBaseDto):
    id: int
    status: UserStatus = UserStatus.Active


class UserFullDto(UserProfilePublicDto):
    password: str

    class Config:
        orm_mode = True


class CreateUserDto(BaseModel):
    username: str
    email: str
    password: str


class LoginResponseDto(BaseModel):
    token: str
    token_type: str

    @staticmethod
    def create_bearer(token: str) -> LoginResponseDto:
        return LoginResponseDto(token=token, token_type='bearer')

class TokenDataDto(BaseModel):
    username: str
    expiry_date: datetime

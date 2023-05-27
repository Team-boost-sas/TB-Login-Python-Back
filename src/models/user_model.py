from typing import Optional
from datetime import date, datetime, time, timedelta
from pkg_resources import require
from pydantic import BaseModel, Field, EmailStr

class user_login(BaseModel):
    email: EmailStr = Field(
        ...,
        title="Email",
        description="The user's email address.",
        example="tugrp@example.com"
    )
    password: str = Field(
        ...,
        title="Password",
        description="The user's password.",
        example="password",
        min_lenght = 6,
        max_length = 20
    )

class user_register(user_login):
    phone: str = Field(
        ...,
        title="Phone",
        description="The user's phone number.",
        example = "0123456789",
        min_length = 10,
        max_length = 10,
        regex = r"^\d{10}$",
        regex_description = "The phone number must be a 10 digit number."
    )
    updated_at: Optional[datetime] = Field(
        default_factory = datetime.now,
        title="Updated At",
        description="The user's last update.",
        example = "2020-01-01T00:00:00"
    )
    created_at: Optional[datetime] = Field(
        default_factory = datetime.now,
        title="Created At",
        description="The user's creation date.",
        example = "2020-01-01T00:00:00"
    )
    status: Optional[str] = Field(
        default = "created",
        title="Status",
        description="The user's status.",
        example = "created"
    )
    status_email: Optional[bool] = Field(
        default = False,
        title="Status Email",
        description="The user's status email.",
        example = False
    )
    status_phone: Optional[bool] = Field(
        default = False,
        title="Status Phone",
        description="The user's status phone.",
        example = False
    )

class user(user_register):
    id: int = Field(
        ...,
        title="ID",
        description="The user's ID.",
        example=123
    )

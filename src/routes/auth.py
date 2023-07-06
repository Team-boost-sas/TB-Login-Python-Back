from fastapi import APIRouter
from src.service import auth
from src.models import user_model
from src.config.databases import Session, engine, Base  # Esta linea se creo
from src.models.user import User

router_auth = APIRouter(prefix="/auth")

Base.metadata.create_all(bind=engine) #aqui agrego lineas

@router_auth.get(
    "/check-user",
    summary="Check user in DB",
    tags=[
        "Auth"
    ]
    )
def check_user(email: str):
    print("paso por routes")
    return auth.check_user(email)

@router_auth.post(
    "/sing-up",
    summary="Check user in DB",
    tags=[
        "Auth"
    ])
def sing_up(user: user_model.user_register):
    return auth.sing_up(user)
    db = Session()
    new_user = user_model(**User.dict())
    db.add(new_user)
    db.commit()
    return User.dict()
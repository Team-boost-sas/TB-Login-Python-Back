from fastapi import APIRouter
from service import auth

router_auth = APIRouter(prefix="/auth")


@router_auth.get("/check-user")
def check_user(email: str):
    print("paso por routes")
    return auth.check_user(email)



"sing-up"



"sing-in"


"check-user"
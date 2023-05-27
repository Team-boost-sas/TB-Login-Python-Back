from src.models import user_model

def check_user(email: str):
    print("paso por service")
    return {"email": email}

def sing_up(user:user_model.user_register):
    print(user)
    return
from fastapi import APIRouter

router = APIRouter(tags=["user"])


@router.get("/user")
async def get_users():
    return [
        {
            "name": "jaynam",
            "position": "data engineer",
        },
        {
            "name": "min",
            "position": "data analytics",
        },
    ]


@router.get("/user/me")
async def get_users():
    return {
        "name": "jaynam",
        "position": "data engineer",
    }


from app.schemas.user_schema import UserInfoType


@router.get("/user/info/{type}")
async def get_user_info(type: UserInfoType):
    if type == UserInfoType.name:
        return {
            "type": type,
            "name": "jaynam",
        }
    if type.value == "position":
        return {
            "type": type,
            "position": "data engineer",
        }


@router.get("/user/{id}")
async def get_users(id: int):
    if id == "1":
        return {
            "name": "jaynam",
            "position": "data engineer",
        }
    else:
        return {"message": "Not found user from id"}

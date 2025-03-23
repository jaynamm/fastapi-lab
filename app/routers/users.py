from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["user"])


@router.get("/")
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


@router.get("/{id}")
async def get_users(id: str):
    if id == "1":
        return {
            "name": "jaynam",
            "position": "data engineer",
        }
    else:
        return {"message": "Not found user from id"}

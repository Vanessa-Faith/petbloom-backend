from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserResponse, UserUpdate
from app.services.fbase_service import verify_fbase_token
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/users", tags=["users"])

def get_current_user(token: str = Depends(lambda: None)):
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    decoded = verify_fbase_token(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid token")
    return decoded

@router.post("/register")
async def register(email: str, name: str, firebaseUid: str):
    try:
        user = await prisma_client.user.create(data={"email": email, "name": name, "firebaseUid": firebaseUid})
        return {"id": user.id, "email": user.email, "name": user.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    try:
        user = await prisma_client.user.find_unique(where={"id": user_id})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    try:
        updated_user = await prisma_client.user.update(where={"id": user_id}, data=user_update.dict(exclude_unset=True))
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/by-email/{email}", response_model=UserResponse)
async def get_user_by_email(email: str):
    try:
        user = await prisma_client.user.find_unique(where={"email": email})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

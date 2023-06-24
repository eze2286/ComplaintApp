from fastapi import APIRouter, Depends
from typing import List, Optional

from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from models import RoleType
from schemas.response.user import UserOut

router = APIRouter(tags=["Users"])


@router.get(
    "/users/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    response_model=List[UserOut],
)
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_users(email)
    return await UserManager.get_users()


@router.put(
    "/users/{user_id}/make-admin/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def make_admin(user_id: int):
    return await UserManager.change_role(role=RoleType.admin, user_id=user_id)


@router.put(
    "/users/{user_id}/make-approver/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def make_admin(user_id: int):
    return await UserManager.change_role(role=RoleType.approver, user_id=user_id)

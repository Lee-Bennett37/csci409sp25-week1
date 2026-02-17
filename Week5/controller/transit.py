from fastapi import APIRouter

router = APIRouter()

@router.get("/transit/{portal_id}")
def access_portal(portal_id:int):
    return {'message': 'Transit ERP Systems'}
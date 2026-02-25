from fastapi import APIRouter
router = APIRouter()

@router.get('/rbi')
def get_rbi():
    return {'rbi':'placeholder'}

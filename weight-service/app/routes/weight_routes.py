from fastapi import APIRouter
router = APIRouter()

@router.get('/weight')
def get_weight():
    return {'weight':'placeholder'}

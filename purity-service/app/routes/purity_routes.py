from fastapi import APIRouter
router = APIRouter()

@router.get('/purity')
def get_purity():
    return {'purity':'placeholder'}

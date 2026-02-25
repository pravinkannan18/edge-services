from fastapi import APIRouter
router = APIRouter()

@router.get('/rfid')
def get_rfid():
    return {'rfid':'placeholder'}

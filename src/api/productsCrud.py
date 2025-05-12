from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def getAllPartners():
    return f""

@router.get("/{id}")
async def getPartner(id):
    return f""

@router.post("/")
async def createPartner():
    return f""

@router.delete("/{id}")
async def deletePartner(id):
    return f""

@router.put("/{id}")
async def updatePartner(id):
    return f""

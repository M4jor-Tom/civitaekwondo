from fastapi import APIRouter, Depends

from core.constant import main
from core.provider import get_routine_executor
from core.service.routine_executor import RoutineExecutor

routine_router: APIRouter = APIRouter()

@routine_router.get(path="/generate_connexion_url", tags=[main])
async def generate_connexion_url(routine_executor: RoutineExecutor = Depends(get_routine_executor)):
    return await routine_executor.execute_routine()

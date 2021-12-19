from typing import List
from fastapi import APIRouter

from ..models.customer import Customer_Post_Request, Customer_Post_Response
from ..manager.customer import CustomerManager

router = APIRouter(tags=["Customer"])

@router.post("/customers", response_model=Customer_Post_Response)
async def post_customer(request: Customer_Post_Request):
    return await CustomerManager.post_customer(request=request)

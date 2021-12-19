from typing import List, Dict
from fastapi import APIRouter

from ..models.customer import CustomerPostRequest, CustomerPostResponse, CustomerPutRequest, CustomerPutResponse
from ..manager.customer import CustomerManager

router = APIRouter(tags=["Customer"])

@router.post("/customers", response_model=CustomerPostResponse)
async def post_customer(request: CustomerPostRequest):
    return await CustomerManager.post_customer(request=request)

@router.put("/customers/{customer_id}", response_model=CustomerPutResponse)
async def put_customer(customer_id: str, request: CustomerPutRequest):
    return await CustomerManager.put_customer(customer_id=customer_id, request=request)

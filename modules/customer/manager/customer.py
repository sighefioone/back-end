from fastapi import HTTPException
from pymysql.err import InternalError, IntegrityError
from db_manager.manager import get_db, get_connection
from ..models.customer import CustomerPostRequest, CustomerPostResponse, CustomerPutRequest, CustomerPutResponse

CUSTOMER_TABLE_CONNECTION = get_connection("customer")

class CustomerManager:

    @classmethod
    async def post_customer(cls, request: CustomerPostRequest):
        conn = await get_db(CUSTOMER_TABLE_CONNECTION)
        cursor = await conn.cursor()
        try:
            await cursor.execute(request.create())
            await conn.commit()
        except Exception as err:
            if err.args[0] == 1062:
                raise HTTPException(status_code=403, detail=err.args[1])
        finally:
            await cursor.close()
            conn.close()
        return CustomerPostResponse(token=request.create())

    @classmethod
    async def put_customer(cls, customer_id: str, request: CustomerPutRequest):
        conn = await get_db(CUSTOMER_TABLE_CONNECTION)
        cursor = await conn.cursor()
        try:
            await cursor.execute(f"SELECT COUNT(*) FROM customer WHERE customer_id='{customer_id}'")
            data = await cursor.fetchone()
            if not data[0]:
                raise HTTPException(status_code=404, detail=f"No customer found with this customer_id [{customer_id}]")
            query = request.update(customer_id=customer_id)
            if query:
                await cursor.execute(query)
                await conn.commit()
            else:
                raise HTTPException(status_code=400, detail="No payload in request")
        except (InternalError, IntegrityError) as err:
            if err.args[0] == 1062:
                raise HTTPException(status_code=403, detail=err.args[1])
        finally:
            await cursor.close()
            conn.close()
        return CustomerPutResponse(detail="Customer Updated Successfully!")

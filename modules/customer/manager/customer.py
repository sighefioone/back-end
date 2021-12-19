from fastapi import HTTPException
from db_manager.manager import get_db, get_connection
from ..models.customer import Customer_Post_Request, Customer_Post_Response

CUSTOMER_TABLE_CONNECTION = get_connection("customer")

class CustomerManager:

    @classmethod
    async def post_customer(cls, request: Customer_Post_Request = None):
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
        return Customer_Post_Response(token=request.create())

    async def put_customer(cls, request=None):
        pass

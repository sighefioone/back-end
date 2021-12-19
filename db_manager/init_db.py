from pymysql.err import InternalError

from .manager import model_list, get_db

async def create_db():
    for model in model_list:
        try:
            conn = await get_db(model.connection)
            cursor = await conn.cursor()
            await cursor.execute(model.table)
            await conn.commit()
        except InternalError as err:
            if err.args[0] == 1050:
                pass
        finally:
            await cursor.close()
            conn.close()

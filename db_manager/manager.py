import aiomysql
from collections import namedtuple

from .connection import mysqldb1
from .customer_module import CustomerSQLQuery

ModelPair = namedtuple("ModelPair", ["name", "connection", "table"])

model_list = [
    ModelPair(name="customer", connection=mysqldb1, table=CustomerSQLQuery)
]

def get_connection(name: str) -> dict:
    for model in model_list:
        if model.name == name:
            return model.connection

async def get_db(sql_connection: dict):
    conn = await aiomysql.connect(**sql_connection)
    return conn

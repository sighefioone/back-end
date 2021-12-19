from hashlib import sha256
from uuid import uuid4
from collections import namedtuple
from typing import Optional

from common.datamodel import DataModel, AllOptional

insert_customer_query = """
INSERT INTO customer
(customer_id, email, username, password, first_name, last_name) VALUES 
('%s', '%s', '%s', '%s', '%s', '%s');
"""

class CustomerPostRequest(DataModel):
    email: str
    username: str
    password: str
    first_name: str
    last_name: Optional[str]

    def create(self):
        customer_id = uuid4().hex
        password = sha256(self.password.encode('utf-8')).hexdigest()
        query = insert_customer_query%(customer_id, self.email, self.username, password, self.first_name, self.last_name)
        return query

class CustomerPostResponse(DataModel):
    token: str
    message: str = "Successfully Created"

class CustomerPutRequest(CustomerPostRequest, metaclass=AllOptional):
    def update(self, customer_id: str) -> str:
        query = "UPDATE customer SET %s WHERE customer_id='%s';"
        data = ""
        count = 0
        for key,val in self.dict(exclude_unset=True).items():
            data += f"{key}='{val}'" if count==0 else f",{key}='{val}'"
            count += 1
        return query%(data, customer_id) if data else None

class CustomerPutResponse(DataModel):
    detail: str

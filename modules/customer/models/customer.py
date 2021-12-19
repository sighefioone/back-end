from hashlib import sha256
from uuid import uuid4
from collections import namedtuple
from typing import Optional

from common.datamodel import DataModel

insert_customer_query = """
INSERT INTO customer
(customer_id, email, username, password, first_name, last_name) VALUES 
('%s', '%s', '%s', '%s', '%s', '%s');
"""

class Customer_Post_Request(DataModel):
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

class Customer_Post_Response(DataModel):
    token: str
    message: str = "Successfully Created"


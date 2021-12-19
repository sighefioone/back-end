CustomerSQLQuery = """
                    CREATE TABLE customer(
                        id SERIAL NOT NULL,
                        customer_id VARCHAR(40) NOT NULL UNIQUE,
                        email VARCHAR(30) NOT NULL UNIQUE,
                        username VARCHAR(20) NOT NULL UNIQUE,
                        password VARCHAR(70) NOT NULL,
                        first_name VARCHAR(20) NOT NULL,
                        last_name VARCHAR(20),
                        create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                        write_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        PRIMARY KEY(id)
                    );
                    CREATE INDEX customer_index 
                    ON customer(customer_id, username, email);
"""

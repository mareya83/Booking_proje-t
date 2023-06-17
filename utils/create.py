import sqlite3

class CreateTable:
    @staticmethod
    def create(manager, table_name):
        manager.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}(
            Id INTEGER PRIMARY KEY,
            Test_element	TEXT,
            Click  INT,
            Input TEXT,	
            Expected_result TEXT,                                            
            Actual_result TEXT
            );
            """)
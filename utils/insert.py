import sqlite3

class Insert:
    @staticmethod
    def insert(manager, table_name, test_element, expected_result):
        manager.execute(f"""
        INSERT INTO {table_name} (Test_element, Click, Expected_result) 
        VALUES('{test_element}', '0', '{expected_result}');
        """)
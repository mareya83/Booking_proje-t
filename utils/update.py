import sqlite3

class Update:

    @staticmethod
    def update_by_condition(manager, table_name, column_name, new_value, condition, condition_value):
        manager.execute(f"""
     UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {condition} == '{condition_value}'
        """)

        
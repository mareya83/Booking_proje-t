import sqlite3

class DeleteTable:
    @staticmethod
    def delete(manager, table_name):
        manager.execute(f"""
        DROP TABLE IF EXISTS {table_name}
        """)
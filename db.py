import sqlite3


class Database:
    def __init__(self, db_name: str = 'database.sqlite'):
        self.db_name = db_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def all(self, table_name: str) -> list:
        results = self.cursor.execute(f'SELECT * FROM {table_name}')
        return results.fetchall()

    def find(self, table_name: str, _id: int) -> dict:
        result = self.cursor.execute(f'SELECT * FROM {table_name} WHERE {table_name}.id = {_id}')
        return result.fetchone()

    def create(self, table_name: str, attributes: tuple, fillable: tuple):
        self.cursor.execute(f"""INSERT INTO {table_name}{fillable}
                                VALUES {attributes}""")
        self.connect.commit()

    def update(self, table_name: str, _id: int, payload: dict):
        self.cursor.execute(f"""UPDATE {table_name}
                              SET {", ".join([f"{column} = {value}" for column, value in payload.items()])}
                              WHERE {table_name}.id = {_id}""")

        self.connect.commit()

    def destroy(self, table_name: str, _id: int) -> dict:
        self.cursor.execute(f'DELETE FROM {table_name} WHERE {table_name}.id = {_id}')
        self.connect.commit()

        if self.cursor.rowcount >= 1:
            return {'method': 'destroy', 'status': 'ok'}

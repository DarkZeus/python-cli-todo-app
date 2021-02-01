from db import Database
from typing import Optional


class Tasks(Database):

    def __init__(self):
        super(Tasks, self).__init__()

        self.fillable = ('title', 'user_id')
        self.attributes = ("id", "title", "created_at", "user_id", "is_done")

    def all(self, table_name: str = None) -> Optional[list]:
        if not table_name:
            table_name = self.__class__.__name__.lower()

        return [dict(zip(self.attributes, tasks)) for tasks in super().all(table_name)]

    def find(self, _id: int, table_name: str = None) -> Optional[dict]:
        if not table_name:
            table_name = self.__class__.__name__.lower()

        return dict(zip(self.attributes, super().find(table_name, _id)))

    def complete(self, _id: int, table_name: str = None) -> Optional[dict]:
        if not table_name:
            table_name = self.__class__.__name__.lower()

        return super().update(table_name, _id, payload={
            'is_done': 1,
        })

    def create(self, attributes: tuple, fillable: tuple = None, table_name: str = None) -> Optional[dict]:
        if not table_name:
            table_name = self.__class__.__name__.lower()

        return super().create(attributes=attributes, table_name=table_name, fillable=self.fillable)

    def delete(self, _id: int, table_name: str = None) -> dict:
        if not table_name:
            table_name = self.__class__.__name__.lower()

        return super().destroy(table_name, _id)

import os
import json

from storage.base_storage import BaseStorage

class JsonStorage(BaseStorage):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def load_all(self) -> list[dict]:
        self._ensure_file_exists()
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Файл {self.file_path} повреждён")

    def save_all(self, data: list[dict]) -> None:
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_by_id(self, item_id: str) -> dict | None:
        data = self.load_all()
        for item in data:
            if item['item_id'] == item_id:
                return item
        return None

    def add(self, item: dict) -> str:
        data = self.load_all()
        item_id = str(max([int(item['item_id']) for item in data], default=0) + 1)
        new_item = item.copy()
        new_item.update({'item_id': item_id})
        data.append(new_item)
        self.save_all(data)
        return item_id

    def update(self, item_id: str, item: dict) -> None:
        data = self.load_all()
        for index, some_item in enumerate(data[:]):
            if some_item['item_id'] == item_id:
                updated_item = item.copy()
                updated_item.update({'item_id': some_item['item_id']})
                data[index] = updated_item
                break
        self.save_all(data)

    def delete(self, item_id: str) -> None:
        data = self.load_all()
        data = [item for item in data if item['item_id'] != item_id]
        self.save_all(data)
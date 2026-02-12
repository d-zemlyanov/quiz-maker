from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any


class BaseStorage(ABC):
    """Абстрактный базовый класс для всех хранилищ."""

    @abstractmethod
    def load_all(self) -> List[Dict[str, Any]]:
        """Загружает все записи из хранилища"""
        pass

    @abstractmethod
    def save_all(self, data: List[Dict[str, Any]]) -> None:
        """Сохраняет все записи"""
        pass

    @abstractmethod
    def get_by_id(self, item_id: str) -> Optional[Dict[str, Any]]:
        """Возвращает запись по ID или None"""
        pass

    @abstractmethod
    def add(self, item: Dict[str, Any]) -> str:
        """Добавляет запись, генерирует ID, возвращает ID"""
        pass

    @abstractmethod
    def update(self, item_id: str, item: Dict[str, Any]) -> None:
        """Обновляет запись по ID"""
        pass

    @abstractmethod
    def delete(self, item_id: str) -> None:
        """Удаляет запись по ID"""
        pass
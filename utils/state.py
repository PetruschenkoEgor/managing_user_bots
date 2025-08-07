from typing import Dict, List, Any, Optional, TypeVar

T = TypeVar('T')  # Может быть любой тип


class UserState:
    """
    Класс для хранения состояния пользователя и данных.
    """
    def __init__(self):
        self.states: Dict[int, str] = {}
        self.data: Dict[int, Dict[str, List[Any]]] = {}

    def set_state(self, user_id: int, state: str) -> None:
        """
        Установка состояния пользователя.
        """
        self.states[user_id] = state

    def get_state(self, user_id: int) -> Optional[str]:
        """
        Получение состояния пользователя.
        """
        return self.states.get(user_id)

    def set_data(self, user_id: int, key: str, value: T) -> None:
        """
        Записываем в словарь данные пользователя.
        """
        if user_id not in self.data:
            self.data[user_id] = {}
        self.data[user_id][key] = value

    def get_data(self, user_id: int) -> Dict[str, List[Any]]:
        """
        Получаем данные пользователя.
        """
        return self.data.get(user_id, {})

    def get_data_value(self, user_id: int, key: str) -> T:
        """
        Получаем конкретное значение данных пользователя.
        """
        return self.data.get(user_id, {}).get(key)

    def clear(self, user_id: int) -> None:
        """
        Очистка состояния и данных.
        """
        if user_id in self.states:
            del self.states[user_id]
        if user_id in self.data:
            del self.data[user_id]

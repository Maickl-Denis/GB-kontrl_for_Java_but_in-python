class Toys:
    """
    Класс для представления игрушек
    ...
    Атрибуты
    --------
    id : int
        Уникальный индификационный номер игрушки
    name : str
        Наименование игрушки
    weight : int
        частота выпадения игрушки от 1 до 9 (1=10%) (вес в % от 100)

    Методы
    ------
    choice_weight (new_weight=""):
        изменения веса (частоты выпадения игрушки). На вход принемает вес [new_weight]
    get_id():
        Возвращает ID игрушки в формате int
    get_weight():
        Возвращает вес игрушки в формате int

    Перегрузка функций
    __str__(self):
        при запросе print экзепляра класса будет выведен текст "ID[id] - Игрушка: имя[name]"
    __repr__(self):
        при запросе print списка, каждый экзепляр класса будет выдавать "ID[id].имя[name]:вес[weight]"
    """

    def __init__(self, id: int, name: str, weight: int):
        self.id: int = id
        self.name: str = name
        self.weight: int = weight

    def change_weight(self, new_weight: int) -> None:
        self.weight = new_weight

    def get_id(self) -> int:
        return self.id

    def get_weight(self) -> int:
        return self.weight

    def __str__(self):
        return f"{self.id} - Игрушка: {self.name}"

    def __repr__(self):
        return f"{self.id}.{self.name}:{self.weight}"

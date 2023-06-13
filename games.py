from random import choices

from toys import Toys


class Game:
    """
    Класс для для работы и органинизации викторины с игрушками
    ...
    Атрибуты
    --------
    list_toys = []
        Список игрушек
    list_gift_toys = []
        Список игрушек участвующих в розыгрыше
    id : int
        Уникальный индификационный номер игрушки начинающийся с 1 и увеличивающий после добавления игрушки

    Методы
    ------
    add_toys (name: str, weight: int):
        Добовляет в список list_toys игрушку. На вход принемает Наименнование игрушки [name] и вес [weight]
    change_weight(id: int, weight: int):
        Изменения веса (частоты выпадения игрушки). На вход принимает ID игрушки и новый вес
    choice_toys():
        Выбираем призовую игрушку и записываем в список list_gift_toys призовых игрушек, которые ожидают выдачи.
    gift_toys():
        Выдача призовой игрушки победителю.
        После его вызова – удаляеся из списка list_gift_toys первая игрушка и сдвигаем массив.
        А эту игрушку записываем в текстовый файл file_vin_toys.txt, файл дозаписывается и ни чего не удаляет
    print_list_toys()
        Выводит в терминал содержимое списка list_toys
    print_list_gift_toys()
        Выводит в терминал содержимое списка list_gift_toys
    """

    def __init__(self):
        self.list_toys = []
        self.list_gift_toys = []
        self.id = 1

    def add_toys(self, name: str, weight: int):
        game_toy_for_viktorina = Toys(self.id, name, weight)
        self.list_toys.append(game_toy_for_viktorina)
        self.id += 1

    def change_weight(self, id: int, weight: int):
        for toy in self.list_toys:
            if Toys.get_id(toy) == id:
                Toys.change_weight(toy, weight)

    def choice_toys(self):
        total_weight = [Toys.get_weight(toy) for toy in self.list_toys]
        self.list_gift_toys.append(choices(self.list_toys, total_weight, k=1))

    def gift_toys(self):
        with open(file="file_vin_toys.txt", mode="a+", encoding="UTF-8") as file:
            temp = self.list_gift_toys.pop(0)
            print(temp[0], file=file)

    def print_list_toys(self):
        return print(self.list_toys)

    def print_list_gift_toys(self):
        return print(self.list_gift_toys)

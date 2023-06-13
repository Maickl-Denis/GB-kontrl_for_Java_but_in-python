from games import Game

#Создаем экземпляр класа
run_viktorina= Game()

#В класс добовляем 3 игрушки
run_viktorina.add_toys("Зайчик", 3)
run_viktorina.add_toys("Слоненок", 3)
run_viktorina.add_toys("Питон", 6)

# распечатываем список имеющихся игрушек
run_viktorina.print_list_toys()

# Изменяем вес одной игрушки
run_viktorina.change_weight(1, 5)

# распечатываем список имеющихся игрушек
run_viktorina.print_list_toys()

# формируем список игруек в количестве 9 штук участвующих в викторине согласно их весу
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()
run_viktorina.choice_toys()

# распечатываем список игрушек предстоящих выдаче победителю
run_viktorina.print_list_gift_toys()

# Выдача 3 игрушек победителям и запись их в файл file_vin_toys.txt
run_viktorina.gift_toys()
run_viktorina.gift_toys()
run_viktorina.gift_toys()

# распечатываем список игрушек предстоящих выдаче победителю
run_viktorina.print_list_gift_toys()

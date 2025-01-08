class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует {new_floor}')

        else:
            for floor in range(new_floor):
                print(floor + 1)
            print(f'Дом {self.name} имеет {self.number_of_floors} этажей \nПоднимаемся на {new_floor}-й')

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)



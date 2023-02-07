class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def name(self):
        return (f'Имя Героя{self.name}')
    def hp(self):
        return (f'Здоровье Героя {self.health_points *2}')
    def __str__(self):
        return (f'Прозвище {self.nickname} \n'
               f'Суперспособность {self.superpower} \n'
               f'Кол-во здоровья {self.health_points}')
    def __len__(self):
        return len(f'{self.catchphrase}')

a = SuperHero("Anthony Edward Stark", "Iron man", "Immortatity", 1000, "I'll take it apart, drown the motherboard and make a hanger out of you")
print(a)
print(a.hp())
print(a.__len__())
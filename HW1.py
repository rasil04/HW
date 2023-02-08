class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def name_hero(self):
        return (f'Имя {self.name}')
    def hp(self):
        print(f'Здоровье {self.health_points * 2}')
    def __str__(self):
        return (f'Прозвище {self.nickname} \n'
               f'Суперспособность {self.superpower} \n'
               f'Количество здоровья {self.health_points}')
    def __len__(self):
        print('Количество букв в коронной фразе ', len(self.catchphrase))

a = SuperHero("Anthony Edward Stark", "Iron man", "Immortality", 1000, "I'll take it apart, drown the motherboard and make a hanger out of you")
print(a)
print(a.name_hero())
print(a.hp())
print(a.__len__())

class FlyHero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.fly = fly
        self.damage = damage

    def hp(self):
        return (f'Здоровье {self.health_points ** 2}')
    def __str__(self):
        self.fly = True
        return (f'fly in the {self.fly}_phrase')

a = FlyHero('Clark Joseph Kent','SuperMan','speed',100, "Loving another is hard, but hating is easy", 100,)
print(a)
print(a.name_hero())
print(a.hp())
print(a.__len__())
print(a.__str__())



class SpaceHero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.fly = fly
        self.damage = damage

    def hp(self):
        self.fly = True
        return (f'Здоровье {self.nickname} {self.health_points ** 2}')

b = SpaceHero('Peter Jason Quill', 'Star Lord', 'dexterity', 200, "Don`t choke on your ambitions",1000 )
print(b)
print(b.name_hero())
print(b.hp())
print(b.__len__())
print(a.__str__())

class Villiain(SpaceHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)
        self.fly = fly
    def gen_x(self):
        pass
    def Brand_phrase(self):
        self.fly = True
        return (f'fly in the {self.fly}_phrase')
    def crit(self):
        return (f"Крит героя {self.nickname} {self.damage **2}")

c = Villiain('Anakin Skywalker', 'Darth Vader', 'anger', 50, "Luke, I'm your father!", 190)
print(c)
print(c.name_hero())
print(c.hp())
print(c.__len__())
print(c.__str__())
print(c.Brand_phrase())
print(c.crit())
print(Villiain.crit(b))
print(Villiain.crit(a))
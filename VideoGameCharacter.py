#код --
#Создать класс с полями, в котором реализовать инициализатор и метод обработки данных.
#Спроектировать иерархию классов от изначально написаного класса, используя наследование. Дописать как минимум одно уникальное поле для каждого класса.
#В классах-наследниках реализовать метод обработки данных.
#Класс и его поля: Персонаж видеоигры: очки здоровья, очки выносливости, урон
#Метод 1: Рассчитать, сколько ударов наносит персонаж, пока выносливость не кончится
#Иерархия: слабый враг, босс
#Метод 2: Рассчитать, сколько ударов понадобится до смерти врага

# Overload the addition operator add 


class GameCharacter:
    def __init__(self, health, stamina, damage):
        self.health = health
        self.stamina = stamina
        self.damage = damage

    def attacks_before_exhaustion(self):
        return self.stamina // self.damage

    def __add__(self, other):
        if isinstance(other, GameCharacter):
            new_health = self.health + other.health
            new_stamina = self.stamina + other.stamina
            new_damage = self.damage + other.damage
            return GameCharacter(new_health, new_stamina, new_damage)
        raise ValueError("Can only add another GameCharacter")

    def __str__(self):
        return f"GameCharacter(Health: {self.health}, Stamina: {self.stamina}, Damage: {self.damage})"


class WeakEnemy(GameCharacter):
    def __init__(self, health, stamina, damage, agility):
        super().__init__(health, stamina, damage)
        self.agility = agility

    def hits_to_defeat(self, attacker_damage):
        return -(-self.health // attacker_damage)

    def __str__(self):
        return (f"WeakEnemy(Health: {self.health}, Stamina: {self.stamina}, "
                f"Damage: {self.damage}, Agility: {self.agility})")


class Boss(GameCharacter):
    def __init__(self, health, stamina, damage, defense_multiplier):
        super().__init__(health, stamina, damage)
        self.defense_multiplier = defense_multiplier

    def hits_to_defeat(self, attacker_damage):
        effective_damage = attacker_damage / self.defense_multiplier
        return -(-self.health // effective_damage)

    def __str__(self):
        return (f"Boss(Health: {self.health}, Stamina: {self.stamina}, "
                f"Damage: {self.damage}, Defense Multiplier: {self.defense_multiplier})")


player = GameCharacter(health=100, stamina=50, damage=10)
print("player attacks before exhaustion:", player.attacks_before_exhaustion())

weak_enemy = WeakEnemy(health=30, stamina=20, damage=5, agility=15)
print("WeakEnemy hits to defeat:", weak_enemy.hits_to_defeat(player.damage))

boss = Boss(health=200, stamina=100, damage=25, defense_multiplier=2)
print("Boss hits to defeat:", boss.hits_to_defeat(player.damage))

combined_character = player + weak_enemy
print("Combined Character:", combined_character)

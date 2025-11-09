class Hero:
    __jumlah = 0  # private class variable

    def __init__(self, nama, health, attPower, armor):
        # Private Base Stats
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # Level & EXP
        self.__level = 1
        self.__exp = 0

        # Derived Stats
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def gainEXP(self):
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP

        # Level Up Logic
        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100

            # Update stats sesuai level baru
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

            # Reset full HP saat naik level
            self.__health = self.__healthMax

    def attack(self, musuh):
        # Serang musuh (logika serangan belum diminta, fokus gain EXP)
        self.gainEXP = 50

    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n" \
               f"\thealth = {self.__health}/{self.__healthMax}\n" \
               f"\tattack = {self.__attPower}\n" \
               f"\tarmor = {self.__armor}"


# Test
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)

class Car:
    def __init__(self, vel_med, consumo_km, combus_tank):
        self.vel_med = vel_med
        self.consumo_km = consumo_km
        self.combus_tank = combus_tank
        self.combus_atual = self.combus_tank
    def viagem(self, dist):
        tempo = dist / self.vel_med
        gasto_gasol = dist / self.consumo_km
        self.combus_atual = self.combus_atual - gasto_gasol
        print(f"O carro andou {dist:.2f} km em {tempo:.2f} horas e gastou {gasto_gasol:.2f} litros de combustivel. O carro agora possui {self.combus_atual:.2f} litros de combustivel.")
    def gasol(self, combus_atual):
        combus = self.combus_atual
        self.combus_atual = self.combus_atual + combus_atual
        if self.combus_atual > self.combus_tank:
            self.combus_atual = self.combus_tank
        print(f"O carro foi abastecido com {self.combus_atual - combus:.2f} litros. O tanque agora esta com {self.combus_atual:.2f} litros de combustivel.")
    def completa(self):
        combus_antes = self.combus_atual
        self.combus_atual = self.combus_tank
        encher = self.combus_atual - combus_antes
        print(f"O carro foi abastecido com {encher:.2f} litros e esta com o tanque cheio!")
vel_med = int(input())
consumo_km = int(input())
combus_tank = int(input())
carro = Car(vel_med, consumo_km, combus_tank)
while True:
    x = input()
    if x == "Abastece":
        y = int(input())
        carro.gasol(y)
    elif x == "Viaja":
        y = int(input())
        carro.viagem(y)
    elif x == "Completa":
        carro.completa()
    elif x == "Encerra":
        break

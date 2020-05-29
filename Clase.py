class Cuenta:

    def __init__(self, name, money):
        self._money = money
        self._name = name
        # depending on the _mode, the queue has to behave like a FIFO or LIFO


    def cuenta_clase(self):
        print('Hola, ' + self._name +' tienes ' + str(self._money) + ' en tu cuenta.')
        pass
  
    def retiro_clase(self,retiro):
        if self._money == 0 :
            print('No hijo no tienes ni medio')
        elif self._money >= retiro :
            self._money = self._money - retiro
            print('Su transacción fue exitosa')
        else: 
            print('Su transacción no fue exitosa')
        return self._money
    
    def deposito_clase(self,deposito):
        if deposito == 0:
            print('Su transacción no fue exitosa')
        elif deposito <0:
            print('Su transacción no fue exitosa')
        else:
            self._money = self._money + deposito
            print('Su transacción fue exitosa')
        return self._money
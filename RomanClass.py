
class RomanNumber():    
    simbolos = {

    'unidades': ['', 'I' , 'II' , 'III' , 'IV' , 'V', 'VI' , 'VII' , 'VIII' , 'IX'],
    'decenas': ['' , 'X' , 'XX' , 'XXX' , 'XL' , 'L' , 'LX' , 'LXX' , 'LXXX' , 'XC'],
    'centenas': ['' , 'C' , 'CC' , 'CCC' , 'CD' , 'D' , 'DC' , 'DCC' , 'DCCC' , 'CM'],
    'millares': ['' , 'M' , 'MM' , 'MMM']

    }

    digitos_romanos = {

    'I': 1 , 'V': 5 , 'X': 10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000 

    }
 

    def __init__ (self, valor):

        if isinstance(valor, int):
            self.valor = valor
            self.cadena = self.a_romano()

        if isinstance(valor, str):
            self.cadena = valor
            self.valor = self.a_numero()

        

    def validar(self):

        if not isinstance(self.valor, int):
            raise ValueError("{} debe ser un entero".format(self.valor))

        if self.valor < 0 or self.valor > 3999:
            raise ValueError("{} debe estar entre 0 y 3999".format(self.valor))

    def a_romano(self):

        self.validar()
        c = str(self.valor)

        unidades = 0
        decenas = 0
        centenas = 0
        millares = 0


        if len(c) >= 1:
            unidades = int(c[-1])

        if len(c) >= 2:
            decenas = int(c[-2])

        if len(c) >= 3:
            centenas = int(c[-3])

        if len(c) >= 4:
            millares = int(c[-4])


        return self.simbolos['millares'][millares] + self.simbolos['centenas'][centenas] + self.simbolos['decenas'][decenas] + self.simbolos['unidades'][unidades]

    def a_numero(self):
        
        acumulador = 0
        valor_anterior = 0
        repeticiones = 0
        restas = 0 

        for caracter in self.cadena:
            valor = self.digitos_romanos.get(caracter)

            if not valor:
                raise ValueError('no es un caracter valido')

            
            if valor_anterior and valor > valor_anterior:
                if restas > 0:
                    raise ValueError('No se pueden concatenar 2 restas seguidas ')

                if repeticiones >0:
                    raise ValueError('No se pueden hacer restas dentro de repeticiones')

                if valor_anterior in (5, 50, 500):
                    raise ValueError("no se pueden restar V, L, D")

                if valor_anterior > 0 and  valor > 10 * valor_anterior:
                    raise ValueError('no se admiten restas entre digitos 10 veces mayores')

                acumulador -= valor_anterior
                acumulador += valor - valor_anterior
                restas += 1
            else:
                acumulador += valor
                restas = 0

            if valor == valor_anterior:
                if valor in (5, 50, 500):
                    raise ValueError("no se pueden repetir V, L o D")

                repeticiones += 1
            
            else:
                repeticiones = 0

            if repeticiones == 3:
                raise ValueError('no se puede repetir mas de 3 veces los caracateres')

            valor_anterior = valor

        return acumulador

def __str__(self):
    return self.cadena

def __repr__(self):
    return self.__str__()

def __len__(self):
    return self.__len__()

def __eq__(self, otrovalor):
    if isinstance(otrovalor, RomanNumber):
        return self.valor == otrovalor.valor
    if isinstance(otrovalor, int):
        return self.valor == otrovalor
    if isinstance(otrovalor, float):
        return self.valor == otrovalor
    if isinstance(otrovalor, str):
        return self.cadena == otrovalor
    raise ValueError("{} solo puede ser entero, cadena, flotante o RomanNumber")




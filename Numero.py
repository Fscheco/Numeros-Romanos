
digitos_romanos = {

    'I': 1 , 'V': 5 , 'X': 10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000 

}


def a_numero(cadena):
    
    acumulador = 0
    valor_anterior = 0
    repeticiones = 0
    restas = 0 

    for caracter in cadena:
        valor = digitos_romanos.get(caracter)

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




    


















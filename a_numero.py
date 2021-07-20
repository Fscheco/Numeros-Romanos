
digitos_romanos = {

    'I': 1 , 'V': 5 , 'X': 10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000 

}


def a_numero(cadena):
    
    acumulador = 0
    valor_anterior = 0

    for caracter in cadena:
        valor = digitos_romanos[caracter]
        if valor > valor_anterior:
            if valor_anterior in (5, 50, 500):
                raise ValueError("no se pueden restar V, L, D")

            if valor_anterior and  valor > 10 * valor_anterior:
                raise ValueError('no se admiten restas entre digitos 10 veces mayores')
            acumulador -= valor_anterior
            acumulador += valor - valor_anterior
        else:
            acumulador = acumulador + valor

        valor_anterior = valor

    return acumulador




    


















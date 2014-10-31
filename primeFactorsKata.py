def primeFactors(number):
    factoresprimos = []
    while number > 1:
        for x in range (2, number+1):        #numeros primos
            while number%x == 0:
                number = number/x
                factoresprimos.append(x)#agrega los numeros primos al index de factores primos 
    return (factoresprimos)
    raise NotImplementedError



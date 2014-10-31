def fizzbuzz(num):
    if num % 15 == 0:
        return ('fizzbuzz')
    elif num % 5 == 0:
        return ('buzz')
    elif num % 3 == 0:
        return ('fizz')
    else:
        return str(num)
        raise NotImplementedError

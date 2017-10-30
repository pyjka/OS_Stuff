""" https://www.codewars.com/kata/544aed4c4a30184e960010f4 """

def divisors(integer):
    lol = []
    for i in range(1,integer):
        if integer % i == 0:
            lol.append(i)
            if i == 1 :
                lol.pop(0)
    if len(lol) == 0:
        return '%s is prime' %integer
    return lol

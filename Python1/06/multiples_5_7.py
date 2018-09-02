# Function multiples_5_7 returns a list of numbers between [77, 777] which are divisible by 7 but not 5
def multiples_5_7():
    result = []
    for n in range(77, 778):
        if n % 5 == 0:
            continue
        elif n % 7 == 0:
            result.append(n)
    return result


if __name__ == '__main__':
    print(multiples_5_7())

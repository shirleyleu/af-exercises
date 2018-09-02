result = []

for n in range(77, 778):
    if n % 5 == 0:
        continue
    elif n % 7 == 0:
        result.append(n)

if __name__ == '__main__':
    print(result)

# Function count_upper returns the number of capital ASCII letters in text.txt
def count_upper():
    count = 0
    # File text.txt must be in the same directory
    file = open('text.txt', 'r')
    for l in file.read():
        if l.isupper():
            count += 1
    file.close()
    return count


if __name__ == '__main__':
    print(count_upper())

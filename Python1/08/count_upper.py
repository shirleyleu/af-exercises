# Function count_upper takes a file-like object and returns the number of
# capital ASCII letters it contains
def count_upper(file):
    count = 0
    for l in file.read():
        if l.isupper():
            count += 1
    file.close()
    return count


if __name__ == '__main__':
    file = open("text.txt", 'r')
    print(count_upper(file))

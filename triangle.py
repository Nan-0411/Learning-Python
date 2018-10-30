height = input('Enter triangle height: ')
height = int(height)

for i in range(height):
    for j in range(i + 1):
        print('#', end='')
    print() 
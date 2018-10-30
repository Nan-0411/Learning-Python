height = input('Enter square height: ')
height = int(height)

width = input('Enter square width: ')
width = int(width)

square= (height, width)
print ('#'*width)
for i in range(height-2):
    print('#'+' '*(width-2)+'#')
print ('#'*width)


square= (height, width)
print ('╔' + '═' * (width-2) + '╗')
for i in range(height-2):
    print('║' + ' ' * (width-2) + '║')
print ('╚' + '═' * (width-2) + '╝')

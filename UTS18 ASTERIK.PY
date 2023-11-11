tinggi = 5
lebar = 8

for i in range(tinggi):
    if i == 0 or i == tinggi - 1:
        print('*' * lebar)
    else:
        print('*' + ' ' * (lebar - 2) + '*')

print('Calculating your love...')
name_1 = input('What\'s your name? ')
name_2 = input('What\'s their name? ')

name_1, name_2 = name_1.upper(), name_2.upper()
true_ocurrance, love_ocurrance = 0, 0

true_case = ['T', 'R', 'U', 'E']
love_case = ['L', 'O', 'V', 'E']

x = 0
while x < len(name_1):
    if name_1[x] in true_case:
        true_ocurrance += 1
    if name_1[x] in love_case:
        love_ocurrance += 1
    x += 1

y = 0
while y < len(name_2):
    if name_2[y] in true_case:
        true_ocurrance += 1
    if name_2[y] in love_case:
        love_ocurrance += 1
    y += 1

love = int((str(true_ocurrance) + str(love_ocurrance)))

if love >= 40 and love <= 50:
    print(f'score: {love}, you go well together.')
elif love <= 10 or love >= 90:
    print(f'score: {love}, you go together like coke and mentos.')
else:
    print(f'Your score: {love} is lame.')

number = int((input('Введите число: ')))
squares = []
for value in range(1, number):
    square = value**2
    if square <= number:
        squares.append(square)
print(squares) 

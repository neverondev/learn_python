number = 23
guess = int(input("введите целое число: "))

if guess == number:
	print('вы угадали')
elif guess < number:
	print('число больше введенного')
else:
	print('число меньше введенного')

print('завершено')

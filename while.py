number = 23
running = True

while running:

	guess = int(input("введите целое число: "))

	if guess == number:
		print('вы угадали')
		running = False
	elif guess < number:
		print('число больше введенного')
	else:
		print('число меньше введенного')

print('завершено')

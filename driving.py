country = input('請輸入國籍: ')
age = input('請輸入年陵齡')
age = int(age)
if country == "台灣":
	if age >= 18:
		print('符合考駕照資格')
	else:
		print('不符考駕照資格')
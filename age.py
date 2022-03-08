driving = input('請問你有沒有開過車')
if driving != '有' or 
age = input('請問你幾歲')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼開過車 484在唬爛我')
if driving == '沒有':
	if age >= 18:
			print('你怎麼不去考駕照')
	else:
			print('再忍一下就可以考駕照惹')	
else:
	print('只能打有或沒有拉操')
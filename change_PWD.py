password = 'a123456'
password_time = 3
while password_time > 0:
	key_password = input('請輸入密碼: ')
	if key_password == password:
		print('登入成功')
		break
	else:
		password_time = password_time - 1
		if password_time <= 0:
			print('結束程式')
			break
		print('輸入錯誤')
		print('請再輸入密碼,還有', password_time, '次機會')
		
		



punctuation = '!#$%&*+-=?@^_,.'

def cezar_code_en(text, n):
    code = ''
    for i in text:
        if (65 < ord(i) < 91) and (ord(i) + n > 90):
            code += chr(ord(i) + n - 26)
        elif (96 < ord(i) < 123) and (ord(i) + n > 122):
            code += chr(ord(i) + n - 26)            
        elif i in punctuation:
            code += i
        else:
            code += chr(ord(i) + n)
    return code

def cezar_code_ru(text, n):
	code = ''
	for i in text:
		if 1039 < ord(i) < 1072 and (ord(i) + n > 1072):
			code += chr(ord(i) + n - 32)
		elif 1071 < ord(i) < 1104 and (ord(i) + n > 1103):
			code += chr(ord(i) + n - 32)
		elif i in punctuation:
			code += i
		else:
			code += chr(ord(i) + n)
	return code

def decode_ru(text,n):
	code = ''
	for i in text:
		if 1039 < ord(i) < 1072 and (ord(i) - n < 1040):
			code += chr(ord(i) - n + 32)
		elif 1071 < ord(i) < 1104 and (ord(i) - n < 1072):
			code += chr(ord(i) - n + 32)
		elif i in punctuation:
			code += i
		else:
			code += chr(ord(i) - n)
	return code


def decode_en(text, n):
	code = ''
	for i in text:
		if (65 < ord(i) < 91) and (ord(i) - n < 65):
			code += chr(ord(i) - n + 26)
		elif (96 < ord(i) < 123) and (ord(i) - n < 97):
			code += chr(ord(i) - n + 26)			
		elif i in punctuation:
			code += i
		else:
			code += chr(ord(i) - n)
	return code


def get_length(text):
    length = 0
    for i in text:
        if i not in punctuation:
            length += 1
    return length


def cesar_code_hot(text):
    word_length = text.split()
    code = ''
    for i in range(text.count(' ')+1):
        code += cezar_code_en(word_length[i], get_length(word_length[i]))
        code +=' '
    return code



type = input('Шифрование или дешифрование (1 / 2): ')
lang = input('Язык алфавита: русский или английский (1 / 2): ')
# n = int(input('Шаг сдвига: '))
text = input('Введите текст: ')
# n = len(text)

if type == '1':
	if lang == '2':
		print(f'Зашифрованнй текст: {cezar_code_en(text, n)}')
	elif lang == '1':
		print(f'Зашифрованнй текст: {cezar_code_ru(text, n)}')
	elif lang == '3': 
		print(cesar_code_hot(text))
	else:
		print('Ошибка ввода. Введите 1 или 2.')
elif type == '2':
	if lang == '1':
		print(f'Дешифрованнй текст: {decode_ru(text, n)}')
	elif lang == '2':
		print(f'Дешифрованнй текст: {decode_en(text, n)}')
	elif lang == '3':
		for n in range(25):
			print(f'Дешифрованнй текст: {decode_en(text, n)}')




























'''name = 'sasa'
age = 12
gorod = 'Saratov'

#print(f'Меня зовут {name}\n Мне {age} лет\n Я живу {gorod}')
#print('dadsa {0:.3f}'.format(5.3125421))
x = ['dsadsa','fdsfsag','diojhiobvcbvcd']

print(x)
print(type(x), '\n')

a = ', '.join(x)
print(a)
print(type(a), '\n')

m = a.split('\n')
print(m)
print(type(m), '\n')

print(type(a), '\n')


my_string = special_string = '\"Привет, мир!\"\n\"Python\"\t\"Я изучаю \"язык программирования\"!\"'

print(my_string,'\n')

a = "Привет, мир!\nPython\tЯ изучаю \"язык программирования\"!"
print(a)

multi_line_string = 'Текст:
Это многострочная строка.
Она состоит из нескольких строк текста.
Вот здесь новая строка

print(multi_line_string)

name = 'Alice'
age = 25
message = 'Привет, меня зовут {} и мне {} лет'.format(name, age)

print(message)
s = 'Hello, World!'

upper_case_text = s.upper()
lower_case_text = s.lower()
s.swapcase()
print(s.swapcase())

l = "Hello", "World", "Python"
joined_string = ', '.join(l)

print(joined_string)
print(type(joined_string))

text = 'Программирование на Python - это весело и мощно!'
starts_with_programming = text.startswith('мощно!')
ends_with_powerful= text.endswith(' мощно!')
print(starts_with_programming, '\n', ends_with_powerful)

text = 'это секретное сообщение: тайна, тайна и еще тайна'
secret_message = text[25:30]
print(secret_message)

start = text.find('тайна')
full = start + len('тайна')
print(start,':', full)

text = 'Python - замечательный язык программирования!'
reversed_text = text.reversed()

text = 'Python - замечательный язык программирования!'
old_substring = 'замечательный'
new_substring = 'удивительный'
modified_text = text.replace('замечательный', 'удивительный')
print(modified_text)

a_arr = [1,2,3]
b_arr = a_arr.copy()

b_arr[2] = 12312312
print(a_arr)
print(b_arr)
'''
a = [312,312,312, 4, 124,5,321,4,3245]
a.insert(0, 1111111)
print(a)`
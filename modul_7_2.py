def custom_write(file_name, strings):
    file_name = 'test.txt'  # добавление в файл
    strings_position = {}
    file = open (file_name, 'w', encoding='utf-8')
    for i, string in enumerate (strings, start=1):
        a = (i, file.tell ())
        strings_position[a] = string
        file.write (f'\n{string}')
    file.close ()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('test.txt', info)

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
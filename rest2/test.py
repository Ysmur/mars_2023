from requests import get, post

# тестирование получения 1 пользователя по id - корректный запрос
#print(get('http://localhost:5000/api/v2/users/1').json())

# тестирование получения 1 пользователя по id - некорректный запрос
#print(get('http://localhost:5000/api/v2/users/19').json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Wok',
                 'name': 'John',
                 'age': 12,
                 'position': 'gl_doctor',
                 'speciality': 'doctor',
                 'address': 'module_1',
                 'email': 'ya@ya.com',
                 'hashed_password': '123'}).json())

print(get('http://localhost:5000/api/v2/users').json())

from requests import get, post

# тестирование получения 1 пользователя по id - корректный запрос
print(get('http://localhost:5000/api/v2/users/1').json())

# тестирование получения 1 пользователя по id - некорректный запрос
print(get('http://localhost:5000/api/v2/users/19').json())
from requests import get

# тестирование получения всех работ из бд в виде словаря
# print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/19').json())

print(get('http://localhost:5000/api/jobs/q').json())
import datetime

from requests import get, post

# тестирование получения всех работ из бд в виде словаря
# print(get('http://localhost:5000/api/jobs').json())

# print(get('http://localhost:5000/api/jobs/1').json())

# print(get('http://localhost:5000/api/jobs/19').json())

# print(get('http://localhost:5000/api/jobs/q').json())

# print(post('http://localhost:5000/api/jobs').json())

# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'Work2'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Work3',
                 'team_leader': 1,
                 'work_size': 12,
                 'collaborators': '1, 2'}).json())

print(get('http://localhost:5000/api/jobs').json())

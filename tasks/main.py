from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())

print(post('http://localhost:5000/api/v2/users', json={}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Юлия'}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Фамилия',
                 'name': 'Имя',
                 'age': 10,
                 'position': "позитион",
                 'speciality': "специалити",
                 'address': "РК, г. Элиста, 2-мкр, д.10",
                 'email': "school17@mail.ru",
                 'hashed_password': "A2udh7y381h!"}).json())

print(delete('http://localhost:5000/api/v2/users').json())
# user с id = 999 нет в базе

print(delete('http://localhost:5000/api/v2/users').json()

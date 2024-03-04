from requests import get, post, delete

print(get('http://localhost:5000/api/news').json())
print(get('http://localhost:5000/api/news/2').json())
print(get('http://localhost:5000/api/news/999').json())
print(get('http://localhost:5000/api/news/6').json())
print(get('http://localhost:5000/api/news/q').json())
print(post('http://localhost:5000/api/news').json())
print(post('http://localhost:5000/api/news', json={'title': 'Заголовок'}).json())
print(post('http://localhost:5000/api/news', json={
    'title': 'Заголовок3',
    'content': 'Текст новости3',
    'user_id': 3,
    'is_private': False,
    'is_published': True}).json())
# print(delete('http://localhost:5000/api/news/999').json()) # новости с id = 999 нет в базе
# print(delete('http://localhost:5000/api/news/10').json())

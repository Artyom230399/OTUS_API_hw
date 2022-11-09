import requests
import pytest


@pytest.mark.parametrize('cond, ExpectedName', [
    (0, 'Leanne Graham'),
    (1, 'Ervin Howell'),
    (2, 'Clementine Bauch'),
    (3, 'Patricia Lebsack'),
    (4, 'Chelsey Dietrich'),
    (5, 'Mrs. Dennis Schulist'),
    (6, 'Kurtis Weissnat'),
    (7, 'Nicholas Runolfsdottir V'),
    (8, 'Glenna Reichert'),
    (9, 'Clementina DuBuque')
])
def test_users(status_code_JSONPlaceholder, cond, ExpectedName):
    assert status_code_JSONPlaceholder.json()[cond]['name'] == ExpectedName


# Проверка того, что количество фото 5000 штук
def test_photos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1/photos')
    assert len(response.json()) == 5000


# Проверка POST
json_post1 = {
    'title': 'First',
    'body': 'Second',
    'userId': 12345
}


def test_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=json_post1)
    assert response.json()['title'] == 'First' and response.json()['body'] == 'Second' and response.json()[
        'userId'] == 12345


# Проверка Name и Email в комментариях
@pytest.mark.parametrize('cond, ExpectedName, ExpectedEmail', [
    (0, 'id labore ex et quam laborum', 'Eliseo@gardner.biz'),
    (1, 'quo vero reiciendis velit similique earum', 'Jayne_Kuhic@sydney.com'),
    (2, 'odio adipisci rerum aut animi', 'Nikita@garfield.biz'),
    (3, 'alias odio sit', 'Lew@alysha.tv'),
    (4, 'vero eaque aliquid doloribus et culpa', 'Hayden@althea.biz')
])
def test_comments(cond, ExpectedName, ExpectedEmail):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    assert response.json()[cond]['name'] == ExpectedName, response.json()[cond]['email'] == ExpectedEmail


# Проверка реализации метода patch
def test_patch():
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1')
    assert response.ok

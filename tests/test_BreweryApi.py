import json
import pytest
import requests


# Валидация имени в Json
@pytest.mark.parametrize("cond, ExpectedName", [
    ('madtree-brewing-cincinnati', 'MadTree Brewing'),
    ('10-56-brewing-company-knox', '10-56 Brewing Company'),
    ('10-barrel-brewing-co-bend-1', '10 Barrel Brewing Co'),
    ('2kids-brewing-company-san-diego', '2Kids Brewing Company'),
    ('32-north-brewing-co-san-diego', '32 North Brewing Co')
])
def test_Name(cond, ExpectedName):
    response = requests.get(f'https://api.openbrewerydb.org/breweries/{cond}')
    assert response.json()['name'] == ExpectedName


# Данные в Json для DDT
with open('param.json', 'r') as f:
    param = json.load(f)


# Проверка количества пивоварен на странице
@pytest.mark.parametrize("cond", param)
def test_page(cond):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'per_page': cond})
    assert len(response.json()) == cond


# Проверка сортировки по городу
@pytest.mark.parametrize("cond", [
    'Bend',
    'San Diego'
])
def test_by_city(cond):
    for i in range(0, 9):
        response = requests.get('https://api.openbrewerydb.org/breweries',
                                params={'by_city': cond, 'per_page': 10})
        assert response.json()[i]['city'] == cond


# Проверка сортировки по штату
@pytest.mark.parametrize("cond", [
    'New York',
    'Texas'
])
def test_by_state(cond):
    for i in range(0, 4):
        response = requests.get('https://api.openbrewerydb.org/breweries',
                                params={'by_state': cond, 'per_page': 5})
        assert response.json()[i]['state'] == cond


def test_by_postal():
    response = requests.get('https://api.openbrewerydb.org/breweries',
                            params={'by_postal': str(44107), 'per_page': 1})
    assert response.json()[0]['postal_code'][0:5] == str(44107)

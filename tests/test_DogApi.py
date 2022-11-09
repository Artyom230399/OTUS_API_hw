import pytest
import requests
import json


# Валидация json для списка всех пород собак
def test_AllDogs_Json(status_code_all_dogs):
    with open('all_dogs.json', 'r') as f:
        json_file = json.load(f)

    assert json_file == status_code_all_dogs


# Валидация статуса ответа для списка всех пород собак
def test_AllDogs_Status(status_code_all_dogs):
    assert status_code_all_dogs['status'] == 'success'


# Валидация статуса ответа для рандомной породы
def test_randomDogs_Status(status_code_random_dogs):
    assert status_code_random_dogs['status'] == 'success'


# Валидация расширения для рандомной породы
def test_randomDogs_Jpg(status_code_random_dogs):
    expansion = status_code_random_dogs['message'][-4:]
    assert expansion == '.jpg'


# Проверка правильного количества изображений
@pytest.mark.parametrize("cond", [
    3,
    4,
    5,
    10,
    30
])
def test_randomDogs_quantity(cond):
    response = requests.get('https://dog.ceo/api/breed/hound/images/random/' + str(cond))
    quantity = len(response.json()['message'])
    assert cond == quantity


@pytest.mark.parametrize("cond", [
    "hound/afghan",
    "hound/blood",
    "mastiff/bull",
    "poodle/toy",
    "sheepdog/english"
])
def test_single_random_image(cond):
    response = requests.get('https://dog.ceo/api/breed/' + cond + '/images/random')
    status = response.json()['status']
    assert status == "success"

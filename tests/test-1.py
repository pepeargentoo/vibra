import requests
import json
def test_name():
    response = requests.get("http://172.17.0.2:8000/search?name=Man")
    assert response.status_code == 200
    result = json.loads(response.text)
    for i in result:
        assert i['name'] == "Man"

def test_city():
    response = requests.get("http://172.17.0.2:8000/search?city=Tugulym")
    assert response.status_code == 200
    result = json.loads(response.text)
    for i in result:
        assert i['city'] == "Tugulym"

def test_name_city():
    response = requests.get("http://172.17.0.2:8000/search?city=Bizhou&name=Man")
    assert response.status_code == 200
    result = json.loads(response.text)
    for i in result:
        assert i['city'] == "Bizhou"
        assert i['name'] == "Man"

def test_all():
    response = requests.get("http://172.17.0.2:8000/search?quantity=1&name=Man")
    assert response.status_code == 200
    result = json.loads(response.text)
    assert len(result) == 1
    for i in result:
        assert i['city'] == "Bizhou"
        assert i['name'] == "Man"
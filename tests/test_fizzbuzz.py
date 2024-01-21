def test_validation_failure_1(client):
    response = client.get('/api/search')
    assert response.status_code == 400

def test_validation_failure_2(client):
    response = client.get('/api/search')

    payload = {
        "errors": {
            "int1": "The value must be a valid integer between 1 and 1000",
            "int2": "The value must be a valid integer between 1 and 1000",
            "limit": "The value must be a valid integer between 1 and 1000",
            "str1": "The value must be a valid string with a max length of 10 chars",
            "str2": "The value must be a valid string with a max length of 10 chars"
        },
        "message": "Validation failure"
    }

    assert response.json == payload

def test_success_response_1(client):
    response = client.get('/api/search?limit=20&int1=2&int2=3&str1=fizz&str2=buzz')

    payload = {
        "result": "1,fizz,buzz,fizz,5,fizzbuzz,7,fizz,buzz,fizz,11,fizzbuzz,13,fizz,buzz,fizz,17,fizzbuzz,19,fizz"
    }
    assert response.json == payload
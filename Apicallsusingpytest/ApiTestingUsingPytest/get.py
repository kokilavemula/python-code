import requests


# check the status_code
def test_get_employees_check_status_code_equals_200():
     response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
     assert response.status_code == 200

# check content type
def test_employees_check_content_type_equals_json():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    assert response.headers['Content-Type'] != "application/json"

# check data
def test_data_equals_employe_name():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    response_body = response.json()
    assert response_body["data"][0]["employee_name"] == "Tiger Nixon"

# check the one data is returned
def test_data_returned():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    response_body = response.json()
    assert len(response_body["data"]) != 1
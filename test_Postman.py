def test_status_code(postman_request):
    assert postman_request.status_code == 200

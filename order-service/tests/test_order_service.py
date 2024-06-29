# test_order_service.py
def test_create_order(order_client, product_client, auth_client):
    # Register and login user
    auth_client.post('/auth/register', json={
        'username': 'orderuser',
        'email': 'order@example.com',
        'password': 'password123'
    })
    login_response = auth_client.post('/auth/login', json={
        'email': 'order@example.com',
        'password': 'password123'
    })
    access_token = login_response.get_json()['access_token']

    # Create product
    product_client.post('/products/', json={
        'name': 'Order Test Product',
        'description': 'This is a test product for order',
        'price': 15.99,
        'stock': 150,
        'version': 1
    })

    # Create order
    response = order_client.post('/orders/', json={
        'user_id': 1,
        'product_id': 1,
        'quantity': 2,
        'total_price': 31.98,
        'status': 'Pending'
    }, headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 201

def test_get_order(order_client, auth_client):
    # Register and login user
    auth_client.post('/auth/register', json={
        'username': 'orderuser',
        'email': 'order@example.com',
        'password': 'password123'
    })
    login_response = auth_client.post('/auth/login', json={
        'email': 'order@example.com',
        'password': 'password123'
    })
    access_token = login_response.get_json()['access_token']

    # Create order
    order_client.post('/orders/', json={
        'user_id': 1,
        'product_id': 1,
        'quantity': 2,
        'total_price': 31.98,
        'status': 'Pending'
    }, headers={'Authorization': f'Bearer {access_token}'})

    # Get order
    response = order_client.get('/orders/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.get_json()['status'] == 'Pending'

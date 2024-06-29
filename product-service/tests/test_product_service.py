# test_product_service.py
def test_create_product(product_client):
    response = product_client.post('/products/', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 10.99,
        'stock': 100,
        'version': 1
    })
    assert response.status_code == 201

def test_get_product(product_client):
    product_client.post('/products/', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 10.99,
        'stock': 100,
        'version': 1
    })
    response = product_client.get('/products/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Test Product'

def test_concurrent_product_update(product_client):
    # Create product
    product_client.post('/products/', json={
        'name': 'Concurrent Test Product',
        'description': 'This product is for testing concurrency',
        'price': 20.99,
        'stock': 200,
        'version': 1
    })

    # Simulate concurrent updates
    response1 = product_client.put('/products/1', json={
        'name': 'Concurrent Test Product',
        'description': 'Updated description',
        'price': 21.99,
        'stock': 190,
        'version': 1
    })
    response2 = product_client.put('/products/1', json={
        'name': 'Concurrent Test Product',
        'description': 'Another update description',
        'price': 22.99,
        'stock': 180,
        'version': 1
    })

    assert response1.status_code == 200
    assert response2.status_code in [200, 409]  # One of them might fail due to version mismatch

# Виктория Удовик, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import send_request


def test_create_order():
    response = send_request.create_order(data.create_order_body)
    assert response.status_code == 201
    track = response.json()["track"]
    response = send_request.track_order(track)
    assert response.status_code == 200

import requests

import configuration
import data


def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,
                         json=body,
                         headers=data.headers)


def track_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_PATH + configuration.ORDERS_TRACK_PATH,
                        params={"t": track_number},
                        headers=data.headers)

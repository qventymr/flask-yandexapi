import requests
import os

def geocode(address):
    API_KEY_GEOCODE = "API_KEY_GEOCODE"
    API_KEY_STATICMAPS = "API_KEY_STATICMAPS"

    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    geocoder_request = f'{server_address}apikey={API_KEY_GEOCODE}&geocode={address}&format=json'
    response = requests.get(geocoder_request)

    try:
        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            toponym_coordinates = toponym["Point"]["pos"]
            address_components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
            country = next((comp["name"] for comp in address_components if comp["kind"] == "country"), None)
            province = next((comp["name"] for comp in address_components if comp["kind"] == "province"), None)
            area = next((comp["name"] for comp in address_components if comp["kind"] == "area"), None)
            locality = next((comp["name"] for comp in address_components if comp["kind"] == "locality"), None)
            street = next((comp["name"] for comp in address_components if comp["kind"] == "street"), None)
            house = next((comp["name"] for comp in address_components if comp["kind"] == "house"), None)

            coords = toponym_coordinates.split()
            coords1 = coords[0]
            coords2 = coords[1]

            # Запрос статической карты
            server_address = 'http://static-maps.yandex.ru/v1?'
            static_maps_request = f'{server_address}ll={coords1},{coords2}&spn=0.00125,0.00125&apikey={API_KEY_STATICMAPS}'
            response = requests.get(static_maps_request)

            # Сохраняем изображение на сервере
            if not os.path.exists('static/img'):
                os.makedirs('static/img')
            image_path = f'static/img/{"image"}.jpg'
            with open(image_path, 'wb') as f:
                f.write(response.content)

            return toponym_address, toponym_coordinates, country, province, area, locality, street, house, image_path
    except Exception as e:
        print(f"Ошибка: {e}")
    return None, None, None, None, None, None, None, None, None

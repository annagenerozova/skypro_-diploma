import requests

class TourApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    
    def get_city_id(self,city_name):
        response = requests.get(self.url+ '/filters/DepartureCities')
        # Проверка статуса ответа
        if response.status_code == 200:
            try:
                cities = response.json()
                for city in cities:
                    if city['name'].lower() == city_name.lower():
                        return city['id']
                return f"City '{city_name}' not found in the list."
            except ValueError:
                return "Error decoding JSON from the response."
        else:
            return f"Error: Unable to fetch data, status code {response.status_code}"

    def get_coutry_id(self,city_name):
        response = requests.get(self.url+'/geoip')
        # Проверка статуса ответа
        if response.status_code == 200:
            try:
                cities = response.json()
                for city in cities:
                    if city['name'].lower() == city_name.lower():
                        return city['id']
                return f"City '{city_name}' not found in the list."
            except ValueError:
                return "Error decoding JSON from the response."
        else:
            return f"Error: Unable to fetch data, status code {response.status_code}"


    def search(self,id_city, id_country , start_date, nights_count, adults):
        params = {
            "departureCityId": id_city,
            "country": id_country,
            "minStartDate": start_date,
            "minNightsCount": nights_count,
            "adults": adults
        }
        response = requests.get(self.url , params=params)
        if response.status_code == 200:
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                print("Error decoding JSON from the response.")
                print("Response content:", response.text)
                return None
        else:
            print(f"Error: Unable to fetch data, status code {response.status_code}")
            return None

    def get_hotel_ids(self):
        response = requests.get(self.url+"/geo")
        if response.status_code == 200:
            try:
                data = response.json()
                hotels = data.get('hotels', [])
                hotel_ids = [hotel.get('id') for hotel in hotels if hotel.get('id') is not None]
                return hotel_ids
            except requests.exceptions.JSONDecodeError:
                print("Error decoding JSON from the response.")
                print("Response content:", response.text)
                return []
        else:
            print(f"Error: Unable to fetch data, status code {response.status_code}")
            return []
  
    def like(self, id_hotel):
        params={
            "objectKey":id_hotel
            }
        response = requests.get(self.url+'/search/wishList',params=params )
        assert response.status_code == 200
        return response.json()
    
    def list_like(self, params_to_add=None):
        resp = requests.get(self.url + '/wishlist', params=params_to_add)
        return resp

    
    def delete_like(self, id_hotel):
        params={
            "objectKey":id_hotel
            }
        response = requests.delete(self.url+'/search/wishList/' + str(id_hotel) ,params=params )
    

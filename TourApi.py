import requests

class TourApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    # id города откуда
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
            response = requests.get(self.url+'/filters/GetArrivalCountries/244707') #244707 город отправления
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
            "arrivalCountryId": id_country,
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
    #Поиск Id тура/отеля
    def get_hotel_ids(self,id_city, id_country):
        params = {
            "departureCityId": id_city,
            "arrivalCountryId": id_country
         }
        response = requests.get(self.url+"/filters/getFilters" ,params=params)
       

  
    def like(self, id_hotel):
        params={
            "objectKey":id_hotel
            }
        response = requests.get(self.url+'/search/wishList',params=params )
        assert response.status_code == 200
        return response.json()
    
    def list_like(self, params_to_add=None):
        resp = requests.get(self.url + '/search/wishList', params=params_to_add)
        return resp.json()

    
    def delete_like(self, id_hotel):
        params={
            "objectKey":id_hotel
            }
        response = requests.delete(self.url+'/search/wishList/' + str(id_hotel) ,params=params )
    

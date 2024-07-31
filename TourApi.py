import requests

token ="eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJraWQiOiI4NjUxMDI5MTY3NDIyQTY4Qjc5QTJDQ0Y0MTRFMDUyQjNEN0VEMTI0IiwidHlwIjoiYXQrand0IiwiY3R5IjoiSldUIn0.JBEkpo3oACdZN9Ng6glGnituRd2um_tjxNo2P3ecVE3Pr5hI1Fq21cdudYOkXkFSUt1bdKHSHMlJzT0U_uZdkfCra6t-AZpUP55FpB5xvlVsZh7Ve_qcKEnqci75xQusNXKayP4aRYQPC1aISufqKGSZKRTDe8tcFyrIUsPooku7nmvLUrt0a1vGiZhn4CKn3soc63Bh4Xu5GVHYyOnzaWFvGqPd_0-spEh5qNxOBv8LKhGBXKNR80C-FHHUPbHcfZoryprmgzfEd4iYtzWbqRjjJMjLU03JciN3FZOTPpgUddkeJJ1zw62YDA0ZdOH80P0_N4zBmEO1ianq-rAkbQ.oXeqlXqGCKgLWasBD4RYOQ.qAiZdfIBWE5q5cNxpC6kwKx-eXfIz-cMPeIY-EQc6AkvihL6Ubp4wjScu5BW9zmBPt4Ywu-7gx_xJgRGQclDskbyXfVd50ZPqMQX5x_S8oqd0mtPpxmC05kF0XGgihz4o21J9PKR-btaV7HYtHLOPAoXrFAFEtbFaTSu_7s5JDks1emIktdBsGF2qyo47T-Eeafo9DtjEbFS5NUkjrm1_QJWMPvAyx2c1tzVSm1eY7vhATBJ3V8K_vadYfM_E1bBB1NFJ-6rFHAybL7jRpUXIY3wo7uC3NpsY0JToYWGCrMZJ3eV5nNjpbwvoXgQe6FnegqWGKxLXI6YsQVqIb_zO7gf0_kO_hPwHJ0ZAat6UmOE3BHUNBMxDh7BmqfcYWdAVzCMxYXsJoCdFnBQaTlAeebAPO5-nuVbtJsnnwllDAx2DiKJ0rGKiiuU50D4hbbVUXsmbEv4jAXdS6qsWtEGnf1jf9tx3hcWjs59HGdeFsDXeLlBsdoe6lHNQgMb3iIAzWbV_oT2M3qM-DXr9S0WiMhb4yQ5rJAbTOFFtWBAl5FQ1fCxAyZ3binIbLoujnAb5nhIh3HkQlu5D3_UGn1zIZS1MdIlx4MC9DIZK4preJ9oAP4RLFNCHJXwZtIjfbzYRpP_kjKvrqhvk6hxWqbqTJTiq-VlXjWsQkY_DJ_-F0EjzIre2ZZHUM7rPBQiCfsjPb8VNE3FzxkFkojcAYXDeMItdKAW1OOymvT3eXtXbUuBbwxphZEhI5ZsDrSLM5OTXhhHb6iU21Uj-uLC9BHkD_INkG9eBS8TG9DW2EMxY9sSBLzD4Kz_meEsURDW0wm_jqoSgI_25-o2qoul3n9Am_Bj80QodADrAQKXY9wQpS1Ik3fiC4y5iAlOHCd4_C4Ti8gRyT55-1zf3wHcoykdrCzrvVrCljPu9YPoC_GhOeO_R3FqUfFhGoKD5dV0q43Ju2yzJ6GfDPTohIw4yree6rUbxOYG-PP6N_lhqnvxK7G5NY49h0vJxEp1uoAB09l3TZbVS9XRT5POD5iksuUJSlrE_tq7H7GtRUMlT9ljg-vJCgHI2WhxpB5fIYVgLUi4SpvUfCAP8nC-6sCAR_4mXzglR8sZYAw-sBn2naFXfjKDeiMK07Nz0CmAbip9-Lj6v3tGIENwJatU_tNaQ841QdKd5VdBR1qwGO-c4ZParztcff7Q4xw6WRVnROzK2qJYFbkulhkW0Jpcz8pZhF7k1yY7-XicqQla_egwHLyN749JYlFSVYnUbKd0OR4LJccE.fY8RwwSbB60bHs-W5Ekp28Cp2E93vWWrE-naJarl_hE"
class TourApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
        self.session = requests.Session()

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
    
    #Поиск id страны прибывания
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
    def post_hotel_ids(self,id_city, id_country):

        headers = {
            'x-csrf-token': 'RDcqQ2GjjbH5wJXgGjivNhTojA5a2RnXvWIK6IhO',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6Ikl1RVFsUmlnTGh2aklSWExtRFJnbXc9PSIsInZhbHVlIjoiS2gvcG9MMnBoYWFjZ3ZzK2dZMFYzQmFOY0t0Y0ZzalpCekJPMXFrd0cxV3JTcGxNVkNuMXVvNUtIK1FZOEc0K05DU1RwZGQrc3RReS9nd3dxS2dXTms3UmxIbzFYWjRjUUZYeDFXSGsxR2lTbHVyNnpMeXVOcFJVQTRtb3IzSk8iLCJtYWMiOiIzZGFjNmRlY2Q1NGYzMDBjODAwOTFjNjQxYWQwMjAyMThlYjBmNjA3MDk2MjRkNDQ3YjFkNDA2MTNkMjM5M2VlIn0%3D; __ddg1_=HYuNSBNE9aiAMogFtsv1; funsan_session=eyJpdiI6IncwRFgxcVl5elhzbXorR0x2NnJCeHc9PSIsInZhbHVlIjoiejF5N1NZd0pvUjZSQ2FkVGtRNkllTXpkN2QwV1FkaWZleHpGSko4eXBwVVlCcURoSHNGTGlVNjBMT2lRZzVLNGQ3NjVXb0liVkt2SitFMDZGdDJMVGY2WUZPeWdrS2NpTzFLNWU4cFhpZEJrazJoakl1bkhvSDFGQ0thVUpvU2MiLCJtYWMiOiIzZDJhNDk1ODJhNTRmNGM5OGZjZGUxNzM2ZjU5NTVhYWViYjFkZDMxMTkwYWQ0OTdiZGRhZTNkYjI5NjVjOTUxIn0%3D',
            'x-xsrf-token': 'eyJpdiI6IjZ5M2lsV3FoMGF3S3dXYVltVHQyZkE9PSIsInZhbHVlIjoiVWNFSzNRWk9CMDIwMjUzR2pLTXlDWWQxclJWTWFpakYzQjk5aVZWcVhVektNREFHcTVvMHJMTHZWanlRdWRjdXpBQW9yRzg0ZE1zQkFJYm1iNk5LUGVsMUtjUmUyRmZKdmlTZzllTE5BMHRjL1FLcmIwbW90U01kT3UxM1BxbTAiLCJtYWMiOiJkY2JmNWUzZDZlYTg5OTAwNDQ4NTY3OWFhNzA3Y2UwNzRmNWYxNzk1MGQyNzcwYWJmOTdkZjk0ZDc3N2NhNTZiIn0='
        }
        body = {
            "departureCityId": id_city,
            "arrivalCountryId": id_country
         }

        response = requests.post(self.url+"/filters/getFilters" , headers=headers, json=body)
        return response.json()[0]['id']

  
    def like(self, id_hotel):
        headers = {
            'x-csrf-token': 'RDcqQ2GjjbH5wJXgGjivNhTojA5a2RnXvWIK6IhO',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6IjR1QWF4WVJEVCtPWkVsaGtITWJGblE9PSIsInZhbHVlIjoiNlBieUpQK2thMGovZzhoYmtVWkN3TUxCRW10YWI5MHJRL2pHaTVYV3JVNFEvMGtUVzNQWmhCTFpMeEJQOHRQZG8wUjlYSUwrcStNZkVyaWhZdk8rMHZ1NVpJN1hGSlVLTDV2bFZJQmJsaHQyVkJ5all3blhjMEVSVHZIQ1ovSlEiLCJtYWMiOiJlMzhhMGFkODQ5YzM3Y2VhMDFkMWQ0OGE2ZTdlOTU0MTliMzZmZWJkYzRiN2RmNTM2ZTllMTJmYWUyNjk5ZWQwIn0%3D; __ddg1_=HYuNSBNE9aiAMogFtsv1; funsan_session=eyJpdiI6IkRLOW9HSU9KdE1aQ29zZ2R4M0lTQ0E9PSIsInZhbHVlIjoiWWZoZ1JkeVBMUW9pNzUvU0xBSTlIa3gzVldZcDdRZ2xrajRlY1FzQnZ0ZWFORFByMUlSL1FaVlRRZko0UjdhblYrejIvbEpqUndLWStRNTRYU00zSnl6eUhBeFg2YTVsNFM1STd0RTVJOUwrUG9lY09LWjlSTm5xZ1BoZ1ZpQlEiLCJtYWMiOiIxY2ZjMzNhMzE3ZmE4MjU3OTRmOWZjYmQ1OGU4ZWVjYjc1ZTJhZTFhNWQwMjk4NTllY2NkZDZkZDAyOTdiNWNhIn0%3D',
            'x-xsrf-token': 'eyJpdiI6IjZ5M2lsV3FoMGF3S3dXYVltVHQyZkE9PSIsInZhbHVlIjoiVWNFSzNRWk9CMDIwMjUzR2pLTXlDWWQxclJWTWFpakYzQjk5aVZWcVhVektNREFHcTVvMHJMTHZWanlRdWRjdXpBQW9yRzg0ZE1zQkFJYm1iNk5LUGVsMUtjUmUyRmZKdmlTZzllTE5BMHRjL1FLcmIwbW90U01kT3UxM1BxbTAiLCJtYWMiOiJkY2JmNWUzZDZlYTg5OTAwNDQ4NTY3OWFhNzA3Y2UwNzRmNWYxNzk1MGQyNzcwYWJmOTdkZjk0ZDc3N2NhNTZiIn0='
        }
        body={
            "objectTypeId":2,
            "objectKey":id_hotel
            }
        response = requests.post(self.url+'/search/wishList',headers=headers, json=body )
        assert response.status_code == 200
        return response.json()

    
    def list_like(self, params_to_add=None):
        headers = {
            'x-csrf-token': 'RDcqQ2GjjbH5wJXgGjivNhTojA5a2RnXvWIK6IhO',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6Ikl1RVFsUmlnTGh2aklSWExtRFJnbXc9PSIsInZhbHVlIjoiS2gvcG9MMnBoYWFjZ3ZzK2dZMFYzQmFOY0t0Y0ZzalpCekJPMXFrd0cxV3JTcGxNVkNuMXVvNUtIK1FZOEc0K05DU1RwZGQrc3RReS9nd3dxS2dXTms3UmxIbzFYWjRjUUZYeDFXSGsxR2lTbHVyNnpMeXVOcFJVQTRtb3IzSk8iLCJtYWMiOiIzZGFjNmRlY2Q1NGYzMDBjODAwOTFjNjQxYWQwMjAyMThlYjBmNjA3MDk2MjRkNDQ3YjFkNDA2MTNkMjM5M2VlIn0%3D; __ddg1_=HYuNSBNE9aiAMogFtsv1; funsan_session=eyJpdiI6IncwRFgxcVl5elhzbXorR0x2NnJCeHc9PSIsInZhbHVlIjoiejF5N1NZd0pvUjZSQ2FkVGtRNkllTXpkN2QwV1FkaWZleHpGSko4eXBwVVlCcURoSHNGTGlVNjBMT2lRZzVLNGQ3NjVXb0liVkt2SitFMDZGdDJMVGY2WUZPeWdrS2NpTzFLNWU4cFhpZEJrazJoakl1bkhvSDFGQ0thVUpvU2MiLCJtYWMiOiIzZDJhNDk1ODJhNTRmNGM5OGZjZGUxNzM2ZjU5NTVhYWViYjFkZDMxMTkwYWQ0OTdiZGRhZTNkYjI5NjVjOTUxIn0%3D',
            'x-xsrf-token': 'eyJpdiI6IjZ5M2lsV3FoMGF3S3dXYVltVHQyZkE9PSIsInZhbHVlIjoiVWNFSzNRWk9CMDIwMjUzR2pLTXlDWWQxclJWTWFpakYzQjk5aVZWcVhVektNREFHcTVvMHJMTHZWanlRdWRjdXpBQW9yRzg0ZE1zQkFJYm1iNk5LUGVsMUtjUmUyRmZKdmlTZzllTE5BMHRjL1FLcmIwbW90U01kT3UxM1BxbTAiLCJtYWMiOiJkY2JmNWUzZDZlYTg5OTAwNDQ4NTY3OWFhNzA3Y2UwNzRmNWYxNzk1MGQyNzcwYWJmOTdkZjk0ZDc3N2NhNTZiIn0='
        }
        resp = requests.get(self.url + '/search/wishList', headers=headers, params=params_to_add)
        return resp.json()

    
    def delete_like(self, id_hotel):
        headers = {
            'x-csrf-token': 'RDcqQ2GjjbH5wJXgGjivNhTojA5a2RnXvWIK6IhO',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6Ikl1RVFsUmlnTGh2aklSWExtRFJnbXc9PSIsInZhbHVlIjoiS2gvcG9MMnBoYWFjZ3ZzK2dZMFYzQmFOY0t0Y0ZzalpCekJPMXFrd0cxV3JTcGxNVkNuMXVvNUtIK1FZOEc0K05DU1RwZGQrc3RReS9nd3dxS2dXTms3UmxIbzFYWjRjUUZYeDFXSGsxR2lTbHVyNnpMeXVOcFJVQTRtb3IzSk8iLCJtYWMiOiIzZGFjNmRlY2Q1NGYzMDBjODAwOTFjNjQxYWQwMjAyMThlYjBmNjA3MDk2MjRkNDQ3YjFkNDA2MTNkMjM5M2VlIn0%3D; __ddg1_=HYuNSBNE9aiAMogFtsv1; funsan_session=eyJpdiI6IncwRFgxcVl5elhzbXorR0x2NnJCeHc9PSIsInZhbHVlIjoiejF5N1NZd0pvUjZSQ2FkVGtRNkllTXpkN2QwV1FkaWZleHpGSko4eXBwVVlCcURoSHNGTGlVNjBMT2lRZzVLNGQ3NjVXb0liVkt2SitFMDZGdDJMVGY2WUZPeWdrS2NpTzFLNWU4cFhpZEJrazJoakl1bkhvSDFGQ0thVUpvU2MiLCJtYWMiOiIzZDJhNDk1ODJhNTRmNGM5OGZjZGUxNzM2ZjU5NTVhYWViYjFkZDMxMTkwYWQ0OTdiZGRhZTNkYjI5NjVjOTUxIn0%3D',
            'x-xsrf-token': 'eyJpdiI6IjZ5M2lsV3FoMGF3S3dXYVltVHQyZkE9PSIsInZhbHVlIjoiVWNFSzNRWk9CMDIwMjUzR2pLTXlDWWQxclJWTWFpakYzQjk5aVZWcVhVektNREFHcTVvMHJMTHZWanlRdWRjdXpBQW9yRzg0ZE1zQkFJYm1iNk5LUGVsMUtjUmUyRmZKdmlTZzllTE5BMHRjL1FLcmIwbW90U01kT3UxM1BxbTAiLCJtYWMiOiJkY2JmNWUzZDZlYTg5OTAwNDQ4NTY3OWFhNzA3Y2UwNzRmNWYxNzk1MGQyNzcwYWJmOTdkZjk0ZDc3N2NhNTZiIn0='
        }
        params={
            "objectKey":id_hotel
            }
        resp = requests.delete(self.url+'/search/wishList/' + str(id_hotel) ,params=params,headers=headers )
        return resp.json()
    
    #поиск туров в определенной стране - Тайланде
    def thailand_tour(self):
        response = requests.get(self.url+'/country/asia/thailand' )
        assert response.status_code == 200
        
    
    def authorization(self,email, password,):
        
        body = {
            "email": email,
            "password":password
        }
        response = self.session.post(self.url + '/login/signin', json=body)
        response.raise_for_status()
        return response.json()
   

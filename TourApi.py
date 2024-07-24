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
            'x-csrf-token': 'tdLG3vZnZWFbt3eq36FUDO0SxHGwGztTJBzFwlKH',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6InA0cFg5STJJSU40WlUrZUEzckFITmc9PSIsInZhbHVlIjoib1VnUEpsbjYxdUdMS0tqbE1TREtCNzlsYS9tZ3lZQm9LUjFMM3phc2N4NndyL1Y1UzZXejhUVnprZStzTlBaeFZJNXdXVnpjam1HTDdFd1VTMzhDVHFrMmd2RlFaVTY0VHdRNkZmaFZzaEJkcXVmUGlFVDNobElUVVlZRDJzZ1oiLCJtYWMiOiJmNzhlZTkzNzRlZmIyOGUwNjc3Zjc2YmI2ODBkYjA3NmFmOGQwYWViZTgwYTkzNjFkZWUyMjg0ZDJhYmExMTYyIn0%3D; __ddg1_=eT3uVnvvcKCwGzQJj9w5; funsan_session=eyJpdiI6IngxQ2FVVU9oeWg1RU1qd0JjK0pnR3c9PSIsInZhbHVlIjoiak5oTy80akJMdS8xOFpUOFZQM2kxcFBzd2RRd1VvTUhiQ3h1OFN0V1VvaDVFaU9VUjBHMjBDUnBnOGpEVnd1d1RXSCttdkVKZVRidFRPZ3Z3QlJzWHovbFUwNHVBTmdnR2VER3NmNzNFZ0ZWdWUwcFA2empEMDdrdyt3elgvREQiLCJtYWMiOiJjMWY4MzFjMTU1MmZiYzA0YWJjNThhMTcwNjNkN2M0YmExNWZlYjcxNWQzMGU2YzcyMGY3NzAyZjFiNmU0OTE3In0%3D',
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
            'x-csrf-token': 'tdLG3vZnZWFbt3eq36FUDO0SxHGwGztTJBzFwlKH',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6IkhKUTI0RWJKWi9VS2FTOEpRT2cxVmc9PSIsInZhbHVlIjoiN3ZWTkRWbUVod2JWV2ZWNnpIVzkrdlQrcjlWRGFWT3dGNnBod243N0Qva1NZTTMrMVdzMGhKSkRXZUVHWWQ5RmxjaWRBd1ZpZzJIMFN5a1RPYS9Vc2ViNzNhVW5wZUhGVEx1R0IyYi9ZSUZnL1ExM0J6QWN0dU4zcGlmd0NiMXkiLCJtYWMiOiI4ZmJlMGM0ZDJmYmEwMmZlOGUwZWU0Mzg5NTYxMzBmNWMxZWZiZDQ2MTMxN2I3ZGQ5MDJhYmFlZWNiMGIyYjg3In0%3D; __ddg1_=eT3uVnvvcKCwGzQJj9w5; funsan_session=eyJpdiI6InNsRHpQeUlDbC80WTJoRFVhV3RCbEE9PSIsInZhbHVlIjoiNFFic1BVWVAwdU9ncFRES2ZnSWZrcGdSV1ZBclZTQmhMdENGN1VDYVRKOE9XVzY4a1JWUHdHTktrWGdVeFgxMGJDa1JkL1ovUlM1UUFpakpLa3lnckRBRHFaMHZ2RmVmTUtvWks5M2htdExGWVFDMEFORk5wRzN2QTdKWEd6c00iLCJtYWMiOiIwYTAzYWI2ODYzMzcwNWZkMGM3NjczMmMzY2I5OWY0OWMyZDgxMzg0ODFhMDYwNjJlZDBjZDQ1ZWI3YjM3ODg2In0%3D',
            'x-xsrf-token': 'eyJpdiI6IlhsUDFzZC9paVZuTlhmcFlsNUs4cWc9PSIsInZhbHVlIjoiYXVFMU5hSk9MV3RqdFQvM0dGaWsydnJ3aVlzdDRVVDlzeGtFanFQUzMrZGlTVTNEN2tLYjBqU0pJc1laRDZ2c2M1L1NEV2JZQWFndDYrWU9oZ2doZ0E4L3hmR2pJRzhOMHhpVmNDRkgyYTFoZGswYURqOEF5cG9rV1phczNiZUkiLCJtYWMiOiJjNDA1ZDYzMmE3NWE4ZWJjNjMyYjNmNmRhOWFiNzBiNDdmM2Y5ZWI1MWFkYjIzZGRhZjNjZmM4MjcxMWE2NDJiIn0='
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
            'x-csrf-token': 'tdLG3vZnZWFbt3eq36FUDO0SxHGwGztTJBzFwlKH',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6IkhKUTI0RWJKWi9VS2FTOEpRT2cxVmc9PSIsInZhbHVlIjoiN3ZWTkRWbUVod2JWV2ZWNnpIVzkrdlQrcjlWRGFWT3dGNnBod243N0Qva1NZTTMrMVdzMGhKSkRXZUVHWWQ5RmxjaWRBd1ZpZzJIMFN5a1RPYS9Vc2ViNzNhVW5wZUhGVEx1R0IyYi9ZSUZnL1ExM0J6QWN0dU4zcGlmd0NiMXkiLCJtYWMiOiI4ZmJlMGM0ZDJmYmEwMmZlOGUwZWU0Mzg5NTYxMzBmNWMxZWZiZDQ2MTMxN2I3ZGQ5MDJhYmFlZWNiMGIyYjg3In0%3D; __ddg1_=eT3uVnvvcKCwGzQJj9w5; funsan_session=eyJpdiI6InNsRHpQeUlDbC80WTJoRFVhV3RCbEE9PSIsInZhbHVlIjoiNFFic1BVWVAwdU9ncFRES2ZnSWZrcGdSV1ZBclZTQmhMdENGN1VDYVRKOE9XVzY4a1JWUHdHTktrWGdVeFgxMGJDa1JkL1ovUlM1UUFpakpLa3lnckRBRHFaMHZ2RmVmTUtvWks5M2htdExGWVFDMEFORk5wRzN2QTdKWEd6c00iLCJtYWMiOiIwYTAzYWI2ODYzMzcwNWZkMGM3NjczMmMzY2I5OWY0OWMyZDgxMzg0ODFhMDYwNjJlZDBjZDQ1ZWI3YjM3ODg2In0%3D',
            'x-xsrf-token': 'eyJpdiI6IlhsUDFzZC9paVZuTlhmcFlsNUs4cWc9PSIsInZhbHVlIjoiYXVFMU5hSk9MV3RqdFQvM0dGaWsydnJ3aVlzdDRVVDlzeGtFanFQUzMrZGlTVTNEN2tLYjBqU0pJc1laRDZ2c2M1L1NEV2JZQWFndDYrWU9oZ2doZ0E4L3hmR2pJRzhOMHhpVmNDRkgyYTFoZGswYURqOEF5cG9rV1phczNiZUkiLCJtYWMiOiJjNDA1ZDYzMmE3NWE4ZWJjNjMyYjNmNmRhOWFiNzBiNDdmM2Y5ZWI1MWFkYjIzZGRhZjNjZmM4MjcxMWE2NDJiIn0='
        }
        resp = requests.get(self.url + '/search/wishList', headers=headers, params=params_to_add)
        return resp.json()


    
    def delete_like(self, id_hotel):
        params={
            "objectKey":id_hotel
            }
        response = requests.delete(self.url+'/search/wishList/' + str(id_hotel) ,params=params )
    
    #поиск туров в определенной стране - Тайланде
    def thailand_tour(self):
        response = requests.get(self.url+'/country/asia/thailand' )
        assert response.status_code == 200
        
    
    def authorization(self,email, password,):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Accept': 'application/json'
        # }
        body = {
            "email": email,
            "password":password
        }
        response = self.session.post(self.url + '/login/signin', json=body)
        response.raise_for_status()
        return response.json()
   

class ExternalTools:
    @staticmethod
    def query_api(api_url, params):
        import requests
        response = requests.get(api_url, params=params)
        return response.json()
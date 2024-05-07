import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

class HttpClient:
    """
    Default implementation to call all REST API's
    """

    def __init__(self, app_id):
        self._app_id = app_id
        self.base_url = "https://api.woovi.com"

    def request(self, method, path, maxretries=None, **kwargs):
        """Makes a call to the API.

        All **kwargs are passed verbatim to ``requests.request``.
        """
        url = self.base_url + path
        headers = kwargs.get('headers', {})
        headers['Authorization'] = self._app_id
        kwargs['headers'] = headers

        retry_strategy = Retry(
            total=maxretries,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        http = requests.Session()
        http.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        with http as session:
            api_result = session.request(method, url, **kwargs)
               
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            if response["status"] > 299 and maxretries == 0:
                raise ValueError(response["response"])

        return response

    def get(self, path, params=None, timeout=None, maxretries=None):  
        """Makes a GET request to the API"""
        return self.request(
            "GET",
            path=path,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def post(self, path, data=None, params=None, timeout=None, maxretries=None):  
        """Makes a POST request to the API"""
        return self.request(
            "POST",
            path=path,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def put(self, path, data=None, params=None, timeout=None, maxretries=None):  
        """Makes a PUT request to the API"""
        return self.request(
            "PUT",
            path=path,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def delete(self, path, params=None, timeout=None, maxretries=None):  
        """Makes a DELETE request to the API"""
        return self.request(
            "DELETE",
            path=path,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )
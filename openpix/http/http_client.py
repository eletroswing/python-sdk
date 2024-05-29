import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from urllib.parse import urlencode, urljoin

class HttpClient:
    """
    Default implementation to call all REST API's
    """

    def __init__(self, app_id):
        self._app_id = app_id
        self.base_url = "https://api.woovi.com"

    def request(self, method, path, query, maxretries=None, data = None, **kwargs):
        """Makes a call to the API.

        All **kwargs are passed verbatim to ``requests.request``.
        """
        if(query):
            query_string = urlencode({k: v for k, v in query.items() if v is not None})
            url = urljoin(self.base_url + path, '?' + query_string)
        else:
            url = self.base_url + path
            
        if(data):
            data = {k: v for k, v in data.items() if v is not None}

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
            api_result = session.request(method, url, data=data,**kwargs)
               
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            if response["status"] > 299:
                raise ValueError(response["response"])

        return response

    def get(self, path, query = None, params=None, timeout=None, maxretries=None):  
        """Makes a GET request to the API"""
        return self.request(
            method="GET",
            path=path,
            query=query,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def post(self, path, query = None, data=None, params=None, timeout=None, maxretries=None):  
        """Makes a POST request to the API"""
        return self.request(
            method="POST",
            path=path,
            query=query,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )
    
    def patch(self, path, query = None, data=None, params=None, timeout=None, maxretries=None):  
        """Makes a PATCH request to the API"""
        return self.request(
            method="PATCH",
            path=path,
            query=query,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def put(self, path, query = None, data=None, params=None, timeout=None, maxretries=None):  
        """Makes a PUT request to the API"""
        return self.request(
            method="PUT",
            path=path,
            query=query,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def delete(self, path, query = None, params=None, timeout=None, maxretries=None):  
        """Makes a DELETE request to the API"""
        return self.request(
            method="DELETE",
            path=path,
            query=query,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )
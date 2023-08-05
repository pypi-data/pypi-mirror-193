import requests
import logging
import os
import pickle
import reactivex as rx
from reactivex import Observable
from reactivex import operators as ops
from typing import Dict, Any, Callable, List

class Url:
    def __init__(self, url: str, method: str = "GET", params: Dict[str, Any] = None, json: Dict[str, Any] = None) -> None:
        self.url: str = url
        self.method: str = method
        self.params: Dict[str, Any] = params
        self.json: Dict[str, Any] = json

class HttpRequest:
    def __init__(self, 
                 cache_key_calculator: Callable[[str, str, Dict[str, Any], Dict[str, Any], Dict[str, str]], str], 
                 session_builder: Callable[[], requests.Session] = lambda: requests.Session(),
                 headers: Dict[str, str] = None):
        self.session_builder: Callable[[], requests.Session] = session_builder
        self.cache_key_calculator = cache_key_calculator
        self.cache: Dict[Any, Any] = {}
        self.headers: Dict[str, str] = headers

    def get_response_stream(self, url: Url, pipes: List[Observable] = [], headers: Dict[str, str] = None, allow_redirects: bool = True, timeout: int = 5, max_retries: int = 3) -> rx.Observable:
        headers = headers or self.headers
        cache_key = self.cache_key_calculator(url.url, url.method, url.params, url.json, headers)
        if cache_key in self.cache:
            logging.info(f"Getting response from cache for URL: {url}")
            return rx.of(self.cache[cache_key])

        logging.info(f"Making a request to URL: {url.url}")
        retries = 0
        while retries < max_retries:
            try:
                response = self.session_builder().request(
                    url.method, url.url, headers=headers, json=url.json, params=url.params, allow_redirects=allow_redirects, timeout=timeout, stream=True)
                self.cache[cache_key] = response
                return rx.of(response) \
                    .pipe(*pipes) \
                    .run()
            except Exception as e:
                logging.warning(f"Request to URL {url.url} failed: {e}. Retrying...")
                retries += 1

        raise Exception(f"Failed to get response from URL {url.url} after {max_retries} retries")

    def store_cache(self, file_path: str):
        with open(file_path, "wb") as cache_file:
            pickle.dump(self.cache, cache_file)

    def load_cache(self, file_path: str):
        if os.path.exists(file_path):
            with open(file_path, "rb") as cache_file:
                self.cache = pickle.load(cache_file)

    def clear_cache_by_key(self, cache_key: str):
        if cache_key in self.cache:
            del self.cache[cache_key]

    def clear_cache_by_url(self, url: str):
        cache_keys = [k for k, v in self.cache.items() if v.url == url]
        for key in cache_keys:
            del self.cache[key]

    def clear_all_cache(self):
        self.cache.clear()



def default_cache_key_calculator(url: str, method: str, params: Dict[str, Any], json: Dict[str, Any], headers: Dict[str, str]) -> str:
    return (url, method, str(params), str(json), str(headers))


default_headers: Dict[str, str] = {}
default_headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
default_headers["Accept-Language"] = "en-US,en;q=0.8"
default_headers["Connection"] = "keep-alive"





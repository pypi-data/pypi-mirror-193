from distutils.core import setup

setup(
    name = 'it4u_http_request',
    packages = ['it4u_http_request'],
    version = 'v1.0.5',  # Ideally should be same as your GitHub release tag varsion
    description = 'HttpRequest will return response in cache if exists, else it will open request',
    author = 'Louis',
    author_email = 'thonh.it@gmail.com',
    url = 'https://github.com/louis-it4u/http-request',
    download_url = 'https://github.com/louis-it4u/http-request/archive/refs/tags/v1.0.5.tar.gz',
    keywords = ['requests', 'cached_requests'],
    classifiers = [],
)
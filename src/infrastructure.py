import pymysql
import pymysql.cursors
import requests
from sqlalchemy import create_engine


class ApiFetcher:

    def __init__(self, api_url, geo_api_url):
        self.api_url = api_url
        self.geo_api_url = geo_api_url

    def fetch_food_security_data(self, iso3, start_date, end_date):
        url_ = self.api_url.format(iso3=iso3) + f"?date_start={start_date}&date_end={end_date}"
        response = requests.get(url_)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data for {iso3}: {response.status_code}")
            return None

    def fetch_geo_boundaries(self, iso3):
        url_ = self.geo_api_url + f"?adm0={iso3}&admcode={iso3}"
        response = requests.get(url_)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch geo boundaries for {iso3}: {response.status_code}")
            return None


class DbRepository:
    def __init__(self, host, user, password, db_name, port=3306, charset='utf8mb4', autocommit=False):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port
        self.charset = charset
        self.autocommit = autocommit
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port,
            charset=charset,
            autocommit=autocommit,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset={charset}')

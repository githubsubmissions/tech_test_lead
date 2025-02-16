from functools import lru_cache

import config


class Container:
    @property
    @lru_cache(maxsize=1)
    def api_fetcher(self):
        from src.infrastructure import ApiFetcher
        return ApiFetcher(config.API_URL, config.GEO_API_URL)

    @property
    @lru_cache(maxsize=1)
    def calculations(self):
        from src.domain import Calculations
        return Calculations(float(config.THRESHOLD))

    @property
    @lru_cache(maxsize=1)
    def db_repository(self):
        from src.infrastructure import DbRepository
        return DbRepository(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME)


container = Container()

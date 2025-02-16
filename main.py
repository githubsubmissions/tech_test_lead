import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import config
from container import container

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')


def run_pipeline(iso3):

    food_security_data = container.api_fetcher.fetch_food_security_data(iso3, start_date, end_date)
    if food_security_data:
        df = container.calculations.compute_cfii(food_security_data)
        print(df.head())


def run_in_parallel():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(run_pipeline, iso3) for iso3 in config.COUNTRIES]
        results = [future.result() for future in futures]
        saved_paths = [result for result in results if result is not None]

    # saved_paths_str = '\n'.join(saved_paths)

# def run_pipeline()


run_pipeline(config.COUNTRIES[0])

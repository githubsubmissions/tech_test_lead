from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import config
from src.domain import Pipeline

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=config.DAYS_TO_FETCH)).strftime('%Y-%m-%d')


def run_pipeline(iso3):
    Pipeline(iso3, start_date, end_date).etl()


def run_in_parallel():
    print("parallel run")
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(run_pipeline, iso3) for iso3 in config.COUNTRIES]
        [future.result() for future in futures]


def run_sequentially():
    print("sequential run")
    for iso3 in config.COUNTRIES:
        run_pipeline(iso3)


if config.RUN_IN_PARALLEL:
    run_in_parallel()
else:
    run_sequentially()

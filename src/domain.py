import json

import pandas as pd
from pandas import DataFrame

from container import container


class Pipeline:
    def __init__(self, iso3, start_date, end_date):
        self.iso3 = iso3
        self.start_date = start_date
        self.end_date = end_date

    def etl(self):
        food_security_data = self.extract()
        transformed_df = self.transform(food_security_data)
        computed_df = self.computations(transformed_df)
        saved_df = self.save(computed_df, self.iso3)

        if saved_df:
            print("send notification")

    def extract(self):
        food_security_data = container.api_fetcher.fetch_food_security_data(self.iso3, self.start_date, self.end_date)
        self.get_geo_data(food_security_data)

        return food_security_data

    def get_geo_data(self, food_security_data):
        country_id = food_security_data['body'][0]['country']['id']
        geo_data = container.api_fetcher.fetch_geo_boundaries(country_id)
        with open(f"api_boundaries/geo_data_{self.iso3}.json", "w") as f:
            json.dump(geo_data, f, indent=4)

    @staticmethod
    def transform(food_security_data) -> DataFrame:
        df = pd.json_normalize(food_security_data, record_path=["body"])
        desired_columns = ['date', 'country.name', 'country.iso3', 'region.id', 'region.name',
                           'metrics.fcs.prevalence', 'metrics.rcsi.prevalence']
        df = df[desired_columns].copy()
        df = df.rename(columns={'country.name': 'country_name', 'country.iso3': 'iso3', 'region.id': 'region_id',
                                'metrics.fcs.prevalence': 'fcs', 'metrics.rcsi.prevalence': 'rcsi'})
        df['fcs'] = df['fcs'].astype(float)
        df['rcsi'] = df['rcsi'].astype(float)

        df["national_fcs"] = df.groupby("date")["fcs"].transform("mean")
        df["national_rcsi"] = df.groupby("date")["rcsi"].transform("mean")

        return df

    @staticmethod
    def save(df: DataFrame, iso3) -> bool:
        try:
            df.to_csv(f"db/food_security_data_{iso3}.csv", index=False)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def computations(df):
        container.calculations.compute_cfii(df)
        return container.calculations.compute_national_cfii(df)

    def load(self):
        pass


class Calculations:

    def __init__(self, cfii_threshold):
        self.cfii_threshold = cfii_threshold

    def compute_cfii(self, df):
        df["cfii"] = 0.5 * df["fcs"] + 1.5 * df["rcsi"]
        df["alert"] = df["cfii"] > self.cfii_threshold
        return df

    def compute_national_cfii(self, df):
        df["national_cfii"] = 0.5 * df["national_fcs"] + 1.5 * df["national_rcsi"]
        df["national_alert"] = df["national_cfii"] > self.cfii_threshold
        return df

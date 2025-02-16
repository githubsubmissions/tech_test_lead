import pandas as pd


class Pipeline:
    def __init__(self, etl_processor, computations, save_process):
        pass

    def etl(self):
        pass

    def computations(self):
        pass

    def save(self):
        pass


class ETLProcessor:

    def extract(self):
        pass

    def transform(self):
        pass

    def load(self):
        pass


class Calculations:

    def __init__(self, cfii_threshold):
        self.cfii_threshold = cfii_threshold

    def compute_cfii(self, data):
        df = pd.DataFrame(data)
        df["cfii"] = 0.5 * df["fcs"] + 1.5 * df["rcsi"]
        df["alert"] = df["cfii"] > self.cfii_threshold
        return df

from math import floor
import pandas as pd


class CriteoDataset:
    def __init__(self, train_file_path: str):
        self.file_path = train_file_path

        self._df = self._load_feather_df(self.file_path)

        self._val_index = None

    @staticmethod
    def _load_feather_df(path: str) -> pd.DataFrame:
        return pd.read_feather(path)

    def _define_val_index(self, val_size: float):
        nb_rows = self.df.shape[0]
        val_start_index = floor(nb_rows * val_size)

        self._val_index = val_start_index

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @property
    def train_df(self) -> pd.DataFrame:
        return self.df.iloc[:self._val_index]

    @property
    def val_df(self) -> pd.DataFrame:
        return self.df.iloc[self._val_index:]


if __name__ == '__main__':
    criteo_dataset = CriteoDataset("data/processed/train.feather")

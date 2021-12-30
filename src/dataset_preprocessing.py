import numpy as np
import pandas as pd
import unittest


def preprocessing_data(file_name, first_col):
    df = pd.read_csv("../data/" + file_name + ".csv", header=0, index_col=False)

    columns = list(df.columns.values)
    columns.remove('ALT')

    sum_col = df[columns].sum(axis=0)
    zero_col = list(dict((k, v) for (k, v) in sum_col.items() if v == 0.0).keys())

    df.drop(columns=zero_col, inplace=True)

    df[first_col] = np.log1p(df[first_col])

    df.to_csv("../data/hepatotoxicity_" + first_col + "_preprocessing_and_analyst.csv", index=False)

    return df


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.file_name = "hepatotoxicity_ALT_KlekFP_ready_set_after_conversion"
        self.data = preprocessing_data(self.file_name, 'ALT')

    def test_any_zero_column(self):
        columns = list(self.data.columns.values)
        columns.remove('ALT')
        self.assertEqual(True, self.data[columns].sum(axis=0).min() > 0)

    def test_any_zero_row(self):
        columns = list(self.data.columns.values)
        columns.remove('ALT')
        self.assertEqual(True, self.data[columns].sum(axis=1).min() > 0)

    def test_first_column_natural_log(self):
        first_column = np.log1p(pd.read_csv("../data/" + self.file_name + ".csv", header=0, index_col=False, usecols=[0]))
        self.assertEqual(True, self.data['ALT'].equals(first_column['ALT']))


if __name__ == "__main__":
    unittest.main()

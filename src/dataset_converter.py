import pandas as pd
import unittest


def convert_fingerprint_CSV(file_name, first_col):
    df_values = pd.read_csv("data/" + file_name + ".csv", header=1)

    main_column = df_values.iloc[:, 0]

    main_column_wo_nan = main_column.dropna().reset_index().drop('index', axis=1)
    df_after_drop = df_values.drop(df_values.columns[0], axis=1).dropna().reset_index().drop('index', axis=1)

    df_after_drop.insert(0, first_col, main_column_wo_nan)
    df_after_drop.to_csv("data/" + file_name + "_after_conversion.csv", index=False)


class TestConverter(unittest.TestCase):
    def setUp(self):
        convert_fingerprint_CSV('hepatotoxicity_ALT_KlekFP_ready_set', 'ALT')
        self.data = pd.read_csv("data/hepatotoxicity_pTD50_KlekFP_ready_set_after_conversion.csv", header=0)

    def test_any_null(self):
        self.assertEqual(False, self.data.isnull().values.any())

    def test_first_column_name(self):
        self.assertEqual(True, self.data.columns[0] != 'Field 11')


if __name__ == "__main__":
    unittest.main()
    # convert_fingerprint_CSV('hepatotoxicity_pTD50_KlekFP_ready_set', 'TD50')
    # convert_fingerprint_CSV('hepatotoxicity_ALT_KlekFP_ready_set', 'ALT')

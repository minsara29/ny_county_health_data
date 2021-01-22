import pandas as pd
import requests as re
from database_script import SqliteDb
import json
import sys
from datetime import date



URL = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD'


class CovidHealthAPI:
    """

    extract the data for each county in New York state from the above API

    """
    def __init__(self, url):
        self.url = url
        self.county_data = self.get_data()["data"]

    def get_data(self):
        """ get data from API. """
        try:
            return re.get(self.url).json()
        except re.exceptions.RequestException as e:
            print(f"Error while request get : {e}")
            raise SystemExit(e)

    def process_data(self, county):
        health_df = pd.DataFrame(self.county_data)
        health_data = health_df.iloc[:, [8, 9, 10, 11, 12, 13]]
        health_data.columns = ['test_date', 'county', 'new_pos', 'cum_no_pos', 'total_no_tests', 'cum_no_tests']
        county_data = health_data[health_data['county'] == county]
        county_dr_data = county_data.drop(columns=['county'], axis=1)
        # print(county_list_data)
        county_data_tuples = [tuple(x) for x in county_dr_data.values]
        return county_data_tuples


if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError('County Parameters is missing ......')
    elif len(sys.argv) > 2:
        target_county = " ".join(sys.argv[1:])
    else:
        target_county = sys.argv[1]


    print("New York state Covid Status for county: " + target_county)

    covid = CovidHealthAPI(URL)
    county_data = covid.process_data(target_county)

    db = SqliteDb()
    db.create_table(target_county)

    db.insert_data(target_county, county_data)
    values = db.select_data(target_county)
    print(values)

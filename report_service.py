import copy
import pandas as pd
import emp
from report import Report


class ReportService: 
    def __init__(self, data):
        self.df = copy.deepcopy(data) 
        self.df.loc[:,'Produkt'] = self.df.loc[:,'Produkt'].str.lower()

    def get_df_filtered_by_manufacturer(self, manufacturer_name):
        self.df.loc[:, 'Inex'] = self.df.loc[:, 'Produkt'].str.find(manufacturer_name)
        return self.df[self.df.loc[:, 'Inex'] != -1 ]
    
    def get_manufacturer_report(self, manufacturer_name):
        data_filtered_by_manufacturer = self.get_df_filtered_by_manufacturer(manufacturer_name)
        return Report(data_filtered_by_manufacturer) 

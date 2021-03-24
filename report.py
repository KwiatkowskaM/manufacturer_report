import pandas as pd
import emp
import copy


class Report:
    def __init__(self, data):
        self.data = copy.deepcopy(data)
        self.create_nazwa_uz_coll(self.data)
        if self.check_if_emp_record_is_empty() == False:
            raise Exception(self.find_NAN_values())

    def create_nazwa_uz_coll(self, data):
        self.data.loc[:, 'nazwa_uzytkownika'] = self.data.loc[:, 'IDemp'].map(emp.wszyscy2)
        
    def drop_ID_by_emp(self):
        index_to_drop = self.data.loc[self.data['IDemp'].isin(emp.to_drop_id.keys())].index.tolist()
        return self.data.drop(index_to_drop)

    def find_NAN_values(self):
        wt = self.drop_ID_by_emp()
        nan_df = wt.loc[wt['nazwa_uzytkownika'].isnull()]
        return nan_df.loc[:, ('Kto', 'IDemp', 'nazwa_uzytkownika')].drop_duplicates('IDemp')

    def check_if_emp_record_is_empty(self):
        wt = self.find_NAN_values()
        return wt.empty

    def drop_duplicates(self):
        return self.data.loc[:, ('nazwa_uzytkownika','IDemp', 'Dostawca', 'data')].drop_duplicates()

    def get_orders_count_by_empl(self):
        wt = self.drop_duplicates()
        return wt.groupby('nazwa_uzytkownika')['Dostawca'].agg('count')

    def get_orders_value_by_empl(self):
        return self.data.groupby('nazwa_uzytkownika')['cena'].agg('sum')

    def create_report_tab(self):
        wt = pd.merge(self.get_orders_count_by_empl(), self.get_orders_value_by_empl(), on='nazwa_uzytkownika').reset_index()
        wt.columns = ['nazwa_uzytkownika','liczba_zam', 'wartosc']
        return wt

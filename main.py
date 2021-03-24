import pandas as pd 
from report_service import ReportService
from report import Report


manufacturerList = ['manufacturer1', 'manufacturer2', 'manufacturer3', 'manufacturer4']
data = pd.read_excel('plik1.xls')
df = pd.DataFrame(data)
report_ser = ReportService(df)
manufacturer1Report = report_ser.get_manufacturer_report('manufacturer1')
manufacturer2Report = report_ser.get_manufacturer_report('manufacturer2')
manufacturer3Report = report_ser.get_manufacturer_report('manufacturer3')

table = pd.merge(manufacturer1Report.create_report_tab(), pd.merge(manufacturer2Report.create_report_tab(), manufacturer3Report.create_report_tab(), on='nazwa_uzytkownika', how = 'outer'), 
                    on='nazwa_uzytkownika', how = 'outer')
columns = pd.MultiIndex.from_product([['Manufacturer1', 'Manufacturer2', 'Manufacturer3'], ['liczba_zam', 'wartosc']], names=['producent', 'obrot'])
table.index = table.loc[:, 'nazwa_uzytkownika']
table = table.drop(columns = 'nazwa_uzytkownika')
table.columns=columns
print(table)

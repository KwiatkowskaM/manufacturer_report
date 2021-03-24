import pandas as pd


konsultanci = {'Adam Adamski' : 1, 'Bartosz Bartowski ' : 2, 'Celina Cel' : 3, 'Dominik Dominikowski' : 4} 

inne = {'web' : 5, 'mail' : 6, 'tel' : 7} 

to_drop_id = {8 : 'inne_z1', 9 : 'administrator', 10 : 'inne_z2'}
wszyscy = {**konsultanci, **inne}
wszyscy2 = dict(zip(wszyscy.values(), wszyscy.keys()))


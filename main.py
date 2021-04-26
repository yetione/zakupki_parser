import re
from pandas import *

tableONE = ExcelFile(r'./full.xlsx')
tableTWO = ExcelFile(r'./test.xlsx')
FirstTable = tableONE.parse(tableONE.sheet_names[0])
SecondTable = tableTWO.parse(tableTWO.sheet_names[0])
regex = '[-]'
results = [v for k, v in FirstTable.items() if re.match (regex, k)]
print (results)
#print (FirstTable.to_dict)
#print (SecondTable.to_dict)
k=input("waiting")
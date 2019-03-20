import pandas as pd
results=[]
draft1=pd.read_table('sample.tsv')
print(draft1)
for row in draft1:
    results.append(row)

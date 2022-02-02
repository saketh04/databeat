import pandas as pd
import csv
from pathlib import Path 
activity= pd.read_csv("activity_data.csv")
movies= pd.read_csv("data.csv")
output=pd.merge(movies,activity,on='_id', how='outer')
df=pd.DataFrame(output,columns= ['_source','rating','hide','watchlist','watched']) 
filepath = Path('out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  
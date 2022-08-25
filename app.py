from urllib import response
import pandas as pd
from client import *

data = Dimagi_Client()

dataset = data.run()

df = pd.DataFrame.from_dict(dataset['objects'])


print(df)


df.columns

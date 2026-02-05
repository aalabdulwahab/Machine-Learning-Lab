

import pandas as pd
dataFrame = pd.read_csv('/content/global_cars_dataset_synthetic.csv')

print('Shape of the DataFrame:', dataFrame.shape)

print('\nFirst 10 rows of the DataFrame:')
display(dataFrame.head(10))

print('\nColumn names and data types:')
dataFrame.info()
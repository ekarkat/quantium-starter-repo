import pandas as pd
import glob

csv_files = glob.glob('data/*.csv')

combined_df = pd.DataFrame()

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])

combined_df = combined_df[(combined_df['product'] == 'pink morsel')]

combined_df['price'] = combined_df['price'].replace('[\$,]', '', regex=True).astype(float)

combined_df['sales'] = combined_df['price'] * combined_df['quantity']

combined_df = combined_df.drop('price', axis=1)
combined_df = combined_df.drop('quantity', axis=1)
combined_df = combined_df.drop('product', axis=1)
combined_df = combined_df.sort_values(by='date')

combined_df.to_csv('newdata.csv', index=False)
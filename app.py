import pandas as pd

your_df = pd.DataFrame(data={'Date': ['31/10/2017', '1/1/2018', '31/12/2018',
                                      '28/02/2016', '09/11/2017']})

your_df['Date'] = pd.to_datetime(your_df['Date'], format="%d/%m/%Y")

your_df['Day of week (str)'] = your_df['Date'].dt.day_name()

print(your_df)

is_ok = id('AAA')==  id('AAA')

print(is_ok)
import pandas as pd

product_price = [5000,2000,4000,3500,2500]
product_label = ['Sunlight','le mineral','indomie jumbo','indomie','egg']

product_series = pd.Series(product_price, index = product_label)
print(product_series)

# we can access pandas series (product_series) using :
# its index, example :
# product_series[0]
# product_series[:3] => accessing product_series from index 0 - 2
# product_series[-2:] => we can count from last index. so the last index is -1. then the -2 index is indomie
# product_series[[0,1,2]] => we can access it manually

# its label
# product_series['Sunlight']
# product_series[:'le mineral']

# actually same with accessing using its index
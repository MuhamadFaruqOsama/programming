# importing the libraries
import numpy as np
import pandas as pd

# declaration
med_price_list = [45, 25, 40, 50, 35]

# convert to array
med_price_arr = np.array(med_price_list)

# converting to pandas series object
series_list = pd.Series(med_price_list)
series_arr = pd.Series(med_price_arr)

# print
# print(series_list)
# print(series_arr)

# giving label for price list on the index
med_price_list_labeled = pd.Series(med_price_list, index = ['Omeprazole','Azithromycin','Metformin','Ibuprofen','Cetirizine'])
# print(med_price_list_labeled)

# adding the price (+2.5)
med_price_list_labeled_updated = med_price_list_labeled + 2.5
# print(med_price_list_labeled_updated)

# creating new price
new_med_price_list = [55,35,45,55,45]
new_med_price_labeled = pd.Series(new_med_price_list, index = ['Omeprazole','Azithromycin','Metformin','Ibuprofen','Cetirizine'])
# print(new_med_price_labeled)

# the differences between old_price vs new_price
print("The differences between the old price (updated) and new price : ")
print(new_med_price_labeled - med_price_list_labeled_updated)
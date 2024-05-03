import pandas as pd

store_data = pd.DataFrame({
    'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04'],
    'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin'],
    'gender': ['M','M','F','M','F'],
    'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty'],
    'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]
})

print(store_data)
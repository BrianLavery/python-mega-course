# Did most of below in ipython in the terminal
# Press ipythton then enter to commence
import pandas

df1=pandas.DataFrame([[2,4,6],[10,20,30]])

df1
#     0   1   2
# 0   2   4   6
# 1  10  20  30

df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

df1
#    Price  Age  Value
# 0      2    4      6
# 1     10   20     30

df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

df1
#         Price  Age  Value
# First       2    4      6
# Second     10   20     30

# print(df1) # => Use this to look at it if run this file

# Less common to pass in data as dictionaries
df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

df2
#    Name
# 0  John
# 1  Jack

df2=pandas.DataFrame([{"Name":"John", "Surname":"Jones"},{"Name":"Jack"}])

df2
#    Name Surname
# 0  John   Jones
# 1  Jack     NaN

# Pandas gives us new data types with own methods
type(df1)
# => pandas.core.frame.DataFrame

dir(df1)

df1.mean()
# Price     6.0
# Age      12.0
# Value    18.0
# dtype: float64

df1.mean().mean()
# 12.0

# We can access specific data series
df1.Price.mean() # => 6.0
df1.Price.max() # => 12.0


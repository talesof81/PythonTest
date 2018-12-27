import pandas as pd

friend_dic_list = [
    {'namme': 'john', 'age' : 25, 'job': 'student'},
    {'namme': 'nate', 'age' : 30, 'job': 'teacher'}
]

df = pd.DataFrame(friend_dic_list)
print(df)
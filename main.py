import numpy as np
import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()
value_to_index = {value: index for index, value in enumerate(unique_values)}

one_hot_encoded = np.zeros((len(data), len(unique_values)), dtype=int)
for i, value in enumerate(data['whoAmI']):
    one_hot_encoded[i, value_to_index[value]] = 1

one_hot_df = pd.DataFrame(one_hot_encoded, columns=unique_values)

one_hot_df.head()

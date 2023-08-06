import numpy as np

'''
import pytorch_helper

from sklearn.preprocessing import MinMaxScaler
transformer = MinMaxScaler()
transformer.fit(train_df[['Close']].to_numpy())
train_np_array = transformer.transform(validation_df[['Close']].to_numpy())
train_x, train_label = pytorch_helper.utils.slice_time_series_data_from_np_array(train_np_array, x_column_indexes=[0], label_column_indexes=[0], sequence_length=7)
#print(train_x.shape) #(973, 7, 1)
#print(train_labels.shape) #(973, 1)
#print(validation_x.shape) #(238, 7, 1)
#print(validation_labels.shape) #(238, 1)
'''
'''
import pytorch_helper

from sklearn.preprocessing import MinMaxScaler
transformer = MinMaxScaler()
transformer.fit(train_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].to_numpy())
train_np_array = transformer.transform(validation_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].to_numpy())
train_x, train_label = pytorch_helper.utils.slice_time_series_data_from_np_array(train_np_array, x_column_indexes=[0, 1, 2, 3, 4, 5], label_column_indexes=[3], sequence_length=7)
#print(train_x.shape) #(973, 7, 6)
#print(train_labels.shape) #(973, 1)
#print(validation_x.shape) #(238, 7, 6)
#print(validation_labels.shape) #(238, 1)
'''
def slice_time_series_data_from_np_array(np_array, x_column_indexes=None, label_column_indexes=None, sequence_length=7):
    #print(np_array.shape) #(980, 1)
    window_length = sequence_length + 1
    x = []
    labels = []
    for i in range(0, len(np_array) - window_length + 1): #0 ~ (980 - 4 - 1) 
        window = np_array[i:i + window_length, :]
        if x_column_indexes:
            x.append(window[:-1, x_column_indexes])
        else:
            labels.append(window[:-1, :])
        if label_column_indexes:
            labels.append(window[-1, label_column_indexes])
        else:
            labels.append(window[-1, :])
    x = np.array(x)
    labels = np.array(labels)
    #print(x.shape) #(977, 3, 1)
    #print(labels.shape) #(977, 1)
    return x, labels 

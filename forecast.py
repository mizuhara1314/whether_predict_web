# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import base64
from io import BytesIO,StringIO




def get_forecast():
    df = pd.read_csv('t_pm25.csv',encoding='utf-8')
    
    df['time'] = pd.to_datetime(df['time'])
    df_gd = df[df['place'] == '济南市（总）']
    data = df_gd[df['time'].dt.hour.isin(np.arange(8, 10))]
    data['time'] = data['time'].apply(lambda x: x.timestamp())
    #訓練集處理
    x= data.drop(['AQI','place','city','time_slot','空气质量'], axis=1)
    y= data['AQI']

        # 数据归一化
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(x)
    y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))

    # 找到分割索引，将数据分为训练集和测试集
    split_index = int(len(X_scaled) * 0.9)  # 90% 的数据用于训练，10% 的数据用于测试

    X_train = X_scaled[:split_index]
    X_test = X_scaled[split_index:]
    y_train = y_scaled[:split_index]
    y_test = y_scaled[split_index:]
    # 转换数据形状以适应LSTM模型 (样本数, 时间步数, 特征数)
    n_steps = 1  # 假设每个样本有1个时间步
    n_features = X_train.shape[1]
    X_train_reshaped = X_train.reshape((X_train.shape[0], n_steps, n_features))
    X_test_reshaped = X_test.reshape((X_test.shape[0], n_steps, n_features))
    data = {'layer1': 259, 'layer2': 410, 'layer3': 473, 'epochs': 7}

        # 定义LSTM模型
    model = Sequential()
    model.add(LSTM(data['layer1'], activation='relu', return_sequences=True))
    model.add(LSTM(data['layer2'], activation='relu', return_sequences=True))
    model.add(LSTM(data['layer3'], activation='relu',return_sequences=False))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    # 训练模型
    model.fit(X_train_reshaped, y_train, epochs=data['epochs'], batch_size=20)

    y_pred_scaled = model.predict(X_test_reshaped)
    y_pred = scaler.inverse_transform(y_pred_scaled)

    # 将 y_test 转换为原始范围
    y_test_original = scaler.inverse_transform(y_test)
    # 画图
    plt.figure(figsize=(10, 6))
    plt.plot(y_test_original, color = 'black', label = 'real')
    plt.plot(y_pred, color = 'green', label = 'Predicted')
    plt.title('空氣指數预测')

    plt.xlabel('日期')
    plt.ylabel('指数')
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64," + ims

    plt.clf()

    return imd

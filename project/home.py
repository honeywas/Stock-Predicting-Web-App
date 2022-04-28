from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import plotly as go
from streamlit_option_menu import option_menu
import time
import requests
from PIL import Image



image = Image.open('img1.jpg')




def app():

 start= '2012-01-01'
 end= '2022-02-28'

 st.write("###")
 st.image(image)
 
 st.title('Stock Prediction :money_with_wings:')

  
 user_input= st.text_input('Enter Stock Ticker', 'GOOG')
 df=data.DataReader(user_input, 'yahoo', start, end)

 st.subheader('Stock Data of Company from 2012-2022')
 st.write(df.describe())

 st.subheader('Closing price vs Time chart')
 fig= plt.figure(figsize=(12,6))
 plt.plot(df.Close)
 st.pyplot(fig)

  #Moving averages
 st.subheader('Closing Price vs Time Chart with 100 & 200 days moving averages')
 ma100= df.Close.rolling(100).mean()
 ma200= df.Close.rolling(200).mean()
 fig =plt.figure(figsize=(12,6))
 plt.plot(ma100, 'r', label= '100 days ma')
 plt.plot(ma200, 'g', label= '200 days ma')
 plt.plot(df.Close, 'grey', label= 'Price of stock')
 plt.legend()
 st.pyplot(fig)
      
        
 #splitting
 data_training =pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
 data_testing =pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

 from sklearn.preprocessing import MinMaxScaler
 scaler = MinMaxScaler(feature_range=(0,1))
 data_training_array = scaler.fit_transform(data_training)


 x_train = []
 y_train = []

 for i in range(100,data_training_array.shape[0]):
    x_train.append(data_training_array[i-100: i])
    y_train.append(data_training_array[i, 0])

 x_train, y_train = np.array(x_train), np.array(y_train)


 #load model
 model= load_model('keras_model.h5')

 #testing
 past_100_days= data_training.tail(100)
 final_df= past_100_days.append(data_testing, ignore_index=True)
 input_data= scaler.fit_transform(final_df)



 x_test = []
 y_test = []

 for i in range(100,input_data.shape[0]):
   x_test.append(input_data[i-100: i])
   y_test.append(input_data[i, 0])

 x_test, y_test = np.array(x_test), np.array(y_test)
 y_predicted = model.predict(x_test)
 scaler= scaler.scale_

 scale_factor= 1/scaler[0]
 y_predicted= y_predicted*scale_factor
 y_test= y_test*scale_factor


 #final graph
 st.subheader('Predicted vs Original Stock Price')
 fig2=plt.figure(figsize=(12,6))
 plt.plot(y_test, 'b', label= 'Original Price')
 plt.plot(y_predicted, 'r', label= 'Predicted Price')
 plt.xlabel('Time(Days)')
 plt.ylabel('Price')
 plt.legend()
 st.pyplot(fig2)




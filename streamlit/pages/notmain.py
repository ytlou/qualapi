import streamlit as st
import nasdaqdatalink
st.markdown("# plot ❄️")
st.sidebar.markdown("# plot ❄️")

import pandas as pd
import matplotlib.pyplot as plt
ticker_list = {"Tencent":"HKEX-00700","Kindstar Global":"HKEX-09960"}

historical_datas = {}
@st.experimental_memo
def load_data():

  for ticker in list(ticker_list.values()):
      historical_datas[ticker] = pd.read_csv("pages/"+ticker+".csv")
  return historical_datas
historical_datas = load_data();

option = st.selectbox(
      'Which stock are you interested in?',
      list(ticker_list.keys()))

'You selected: ', option
df = historical_datas[ticker_list[option]]

f = plt.figure()
# Plot the stock price over time
plt.plot(df["Date"], df["Nominal Price"])

# Add labels to the x and y axis
plt.xlabel("Date")
plt.ylabel("Stock Price")

# Add a title to the plot
plt.title("Stock Price Over Time")

# Show the plot
st.pyplot(f)
f1 = plt.figure()
sma = df["Previous Close"].rolling(window=50).mean()

# Plot the stock price and the moving average
plt.plot(df["Date"], df["Previous Close"], label="Stock Price")
plt.plot(df["Date"], sma, label="50-day SMA")

# Add labels to the x and y axis
plt.xlabel("Date")
plt.ylabel("Stock Price")

# Add a legend to the plot
plt.legend()

# Add a title to the plot
plt.title("Stock Price with 50-day Simple Moving Average")

# Show the plot
st.pyplot(f1)
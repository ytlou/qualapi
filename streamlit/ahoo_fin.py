import nasdaqdatalink
import streamlit as st
st.markdown("# Hong Kong Exchange 🎈")
st.sidebar.markdown("# Hong Kong Exchange 🎈")

nasdaqdatalink.ApiConfig.api_key = "Jiv89EvQGVHE-6KLqo8x"
# amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")
# amazon_weekly# add_selectbox = st.sidebar.selectbox('Which number do you like best?',
#      ticker_list)
ticker_list = {"Tencent":"HKEX/00700", "Csop Healthcare":"HKEX/03174"}
  #ticker_list = ["HKEX/00700", "HKEX/40814"]
historical_datas = {}
@st.experimental_memo
def load_data():

  for ticker in list(ticker_list.values()):
      historical_datas[ticker] = nasdaqdatalink.get(ticker)
  return historical_datas
  

historical_datas = load_data();



option = st.selectbox(
      'Which stock are you interested in?',
      list(ticker_list.keys()))

'You selected: ', option
historical_datas[ticker_list[option]]


import nasdaqdatalink
import streamlit as st
st.markdown("# Hong Kong Exchange 🎈")
st.sidebar.markdown("# Hong Kong Exchange 🎈")

nasdaqdatalink.ApiConfig.api_key = "Jiv89EvQGVHE-6KLqo8x"

ticker_list = {"Tencent":"HKEX/00700", "Csop Healthcare":"HKEX/03174","alibarc": "HKEX/54061" ,"Mini-Hang Seng" :"HKEX/MHINH2022",  "Gx Asia Semicon": "HKEX/03119","Kindstar Global":"HKEX/09960"}

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


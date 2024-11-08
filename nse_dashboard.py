from nselib import capital_market
from nselib import derivatives
import streamlit as st
from datetime import date 
import datetime

st.header('Indian Stock Financial Market Dashboard');

instrument = st.sidebar.selectbox('Instrument Type', options=('NSE Equity Market', 'NSE Derivatives Market'));
if instrument == 'NSE Equity Market':
    data_info = st.sidebar.selectbox('Data to  Extract', options=('bhav_copy_equities', 'bhav_copy_with_delivery',
                                                                  'equity_list','fno_equity_list','nifty50_equity_list',
                                                                  'block_deals_data','bulk_deal_data','india_vix_data',
                                                                  'short_selling_data','deliverable_position_data',
                                                                  'index_data','price_volume_and_deliverable_position_data',
                                                                  'price_volume_data'))
    if(data_info == 'equity_list') or(data_info =='fno_equity_list') or (data_info == 'nifty50_equity_list'):
        data = getattr(capital_market, data_info)()
    if(data_info == 'bhav_copy_equities') or(data_info == 'bhav_copy_with_delivery'):
        today = date.today().strftime('%d-%m-%Y')
        date = st.sidebar.text_input('Date',today)
        data = getattr(capital_market, data_info)(date)
    if(data_info == 'block_deals_data') or(data_info == 'bulk_deal_data') or (data_info == 'india_vix_data') or (data_info == 'short_selling_data'):
        period_ = st.sidebar.text_input('Period','1M')
        data = getattr(capital_market, data_info)(period = period_)

if instrument == 'NSE Derivatives Market':
    data_info = st.sidebar.selectbox('Instrument Type', options=('future_price_volume_data','option_price_volume_data',
                                                                'fno_bhav_copy','participant_wise_open_interest',
                                                                'participant_wise_trading_volume','expiry_dates_future',
                                                                'expiry_dates_option_index','nse_live_option_chain','fii_derivatives_statistics'))
    if(data_info == 'expiry_dates_future') or(data_info =='expiry_dates_option_index'):
        data = getattr(derivatives, data_info)()
    if(data_info == 'fii_derivatives_statistics') or(data_info == 'fno_bhav_copy') or (data_info == 'participant_wise_open_interest') or (data_info == 'participant_wise_trading_volume'):
        today = datetime.date.today().strftime('%d-%m-%Y')
        date = st.sidebar.text_input('Date',today)
        data = getattr(derivatives, data_info)(date)
    if(data_info=='future_price_volume_data'):
        ticker = st.sidebar.text_input('Ticker','SBIN')
        type_ = st.sidebar.text_input('Instrument Type', 'FUTSTK')
        period_ = st.sidebar.text_input('Period','1M')
        data = derivatives.future_price_volume_data(ticker,type_,period=period_)
    if(data_info=='option_price_volume_data'):
        ticker = st.sidebar.text_input('Ticker','BANKNIFTY')
        type_ = st.sidebar.text_input('Instrument Type', 'OPTIDX')
        period_ = st.sidebar.text_input('Period','1M')
        data = derivatives.option_price_volume_data(ticker,type_,period=period_)    
    if(data_info=='nse_live_option_chain'):
        ticker = st.sidebar.text_input('Ticker','BANKNIFTY')
        today = datetime.date.today()
        days_until_thursday = (3 - today.weekday()) % 7
        next_thursday = (today + datetime.timedelta(days=days_until_thursday)).strftime('%d-%m-%Y')
        expiry_date = st.sidebar.text_input('Expiry Date',next_thursday)
        data = derivatives.nse_live_option_chain(ticker,expiry_date)
    
st.write(data)
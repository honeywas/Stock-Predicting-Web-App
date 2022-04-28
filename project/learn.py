import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests
from annotated_text import annotated_text
from streamlit_player import st_player



def app():
 
 with st.container():
    st.title("ABOUT STOCK MARKET :book:")
    
         
 
 st.header(' Stock Market Basics')
 st.write("""
            All companies need money to run their business. Sometimes the profit acquired from selling goods
            or services is not sufficient to meet the working capital requirements. And so, companies invite
            normal people like you and me to put some money into their company so that they can run it
            efficiently and in return investors get a share of whatever profit they make. Understanding this is
            the first step towards understanding stock market basics. Let's learn about this in detail.
            """)
 st_player("https://youtu.be/Xn7KWR9EOGQ") 
 st.header('  What are shares?')
 st.write("""
            Shares are a way to own a part of the company's value. In proportion to the capital you invest, you
            can get ownership rights to a certain percentage of the company. Say you own 2% of the shares
            being traded in the market, you can say you have 2% ownership in the company.
            Hence, shares are units of ownership in the company and its financial assets. Shares are also
            known as stocks, equity, scrips etc. After purchasing them you will be known as a stockholder or a
            shareholder of the company. Also, there are different types of shares available in the market to
            invest/trade in.

            """)
   
 st.header(' What is SEBI?')
 st.write("""
            Securities and Exchange Board of India is the securities market regulator to oversee any fraudulent
transactions and activities made by any of the parties: companies, investors, traders, brokers and
the likes.
            """)
   
 st.header('  What are stock exchanges and how many exchanges are there?')
 st.write("""
            Stock exchanges is a place or platform where traders and buyers come together to buy and sell
stocks. There are two primary stock exchanges in the country: Bombay Stock Exchange (BSE) and
National Stock Exchange (NSE). This is extremely important information to know about stock
market basics in India.

            """)
 st.write("[NSE WEBSITE >](https://www.nseindia.com/)")
  
 st.header(' How do you start trading or investing')
 st.write("""
            You need to open a Demat and trading account. Most investment platforms and brokers these days
provide you with a Demat cum trading account. A trading account is used for just the transactions.;
buying and selling. Generally, if you are a trader, you don't really need to open a Demat account
because if you are buying and selling within the same day, a trading account will suffice. Demat
account is where your shares are stored in electronic form. Generally takes 2 working days for
shares to get dematerialised and transferred to your Demat account. So after that, if you buy or sell
your share it gets debited or credited from your account.

            """)
 st_player("https://youtu.be/0t_VoN_xYGY")  
 st.header(' How to Invest in the Share Market in India?')
 st.write("""
            In case you're wondering how to invest in the share market online in India, we've got you covered.
Here are the steps that you need to follow to buy stocks easily from the comfort of your home:


Step 1: Open a Demat account and ensure that it is linked with a pre-existing bank account to carry
out transactions smoothly.


Step 2: Sign in to the Demat account via the mobile-based application or web platform.


Step 3: Pick a stock that you want to invest in.


Step 4: Make sure that you have sufficient funds in your bank account to buy the shares that you
wish to purchase.


Step 5: Purchase the stock at its listed price and specify the number of units.


Step 6: Once a seller reciprocates to that request, your purchase order will get executed. Post
completion of the transaction, your bank account will get debited with the required amount.
Simultaneously, you will receive the shares in your Demat account.
            """)
   
 st.header(' Are there any taxes?')
 st.write("""
            Yes, taxes are applicable to the gains you make from your stock market transactions. A brief of how
much you will be taxed is mentioned in the table below.
Long term capital gains are defined as gains you make after holding your shares for a period of 1
year or more and short term capital gains are gains you make when you hold the shares for a period
of less than a year.


 • Long term capital gains tax    :                                            10% over and above Rs. 1 Lakh on sale of equity shares.

 • Short term capital gains tax    :                                           15%, when securities transaction tax is applicable.
            """)
 st_player("https://youtu.be/W0_pFrZc8MI")  
   
 st.header('  What Factors Do I Consider before Investing in Stocks?')
 st.write("""
            • Investment objectives: If you're looking to invest in the stock market or any other investment
                                     avenue, you must first identify your financial goals. The investment objective is not universal and
                                     alters with every investor. Hence, you must pick stocks after taking your financial goals into
                                     account. Decide your investment horizon as well before investing.
            
            
            • Risk-bearing ability: Another essential factor to take into account when investing in stocks is your
                                    risk appetite. Investors who have a low-risk appetite may consider investing in defensive stocks
                                    that provide stable returns and are less impacted by market volatility.
           
           
           • Diversification: By building a diversified portfolio, you can mitigate risks. In other words, the more
                               your investment is spread across different sectors, the lower will be the financial risk associated
                                with your investments.
            """)
 
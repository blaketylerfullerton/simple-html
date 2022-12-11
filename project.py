#This is a Project by Blake Fullerton 12/11/22
import yfinance as yf







def stock(): 
    tickerSign = input('What is the ticker?: ')
    global yourShares
    yourShares = input('How many shares do you have?: ')
    ticker = yf.Ticker(tickerSign).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    yourSharesPrice = int(yourShares) * market_price
    print('---------------------------------------------')
    print('[X] Market Price:', market_price)
    print('[X] Previous Close Price:', previous_close_price)
    print('[X] Market Price for your total shares is: ', round(yourSharesPrice, 3))
    print('---------------------------------------------')
    


totalVal = 0.0
#-------------Main----------------------------------
print('Welcome to Blakes Python Stock Portfolio Bot :)')
total =  int(input('How many stocks do you have?: '))
for x in range(total):
    tickerSign = input('What is the ticker?: ')
    global yourShares
    yourShares = input('How many shares do you have?: ')
    ticker = yf.Ticker(tickerSign).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    yourSharesPrice = int(yourShares) * market_price
    print('---------------------------------------------')
    print('[X] Market Price:', market_price)
    print('[X] Previous Close Price:', previous_close_price)
    print('[X] Market Price for your total shares is: ', round(yourSharesPrice, 3))
    print('---------------------------------------------')
    totalVal = totalVal + yourSharesPrice

print('Your Portfolio Value is', round(totalVal, 3))




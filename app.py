from flask import Flask, request, render_template
import yfinance as yf

app = Flask(__name__)


@app.route("/quote")
def display_quote():
  symbol = request.args.get('symbol', default="AAPL")

  quote = yf.Ticker(symbol)

  return quote.info

# API route for pulling the stock history
@app.route("/history")
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	data = hist.to_json()
	#return the JSON in the HTTP response
	return data
    
@app.route("/")
def home():
    return render_template("homepage.html")
    return data


if __name__ == "__main__":
  app.run(debug=True)
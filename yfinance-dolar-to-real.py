import yfinance as yf
import locale
import pywhatkit as kit
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the locale to Brazilian Portuguese for currency formatting
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# WhatsApp contact information
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
recipient_whatsapp_number = os.getenv('RECIPIENT_WHATSAPP_NUMBER')

# Function to get exchange rate from yfinance
def get_exchange_rate_yfinance(ticker):
    ticker_data = yf.Ticker(ticker)
    exchange_rate = ticker_data.history(period='1d')
    
    if not exchange_rate.empty:
        rate = exchange_rate['Close'].iloc[-1]
        return rate
    else:
        print(f"No data available for {ticker}")
        return None

# Function to convert and format the rate
def convert_and_format(rate, currency_name, usd_to_brl):
    if currency_name == 'USD to BRL':
        converted_rate = rate
    else:
        converted_rate = rate * usd_to_brl
    
    # Format the number with commas and decimal points
    formatted_rate = locale.format_string("%.2f", converted_rate, grouping=True)
    return f"R$ {formatted_rate}", print("yFinance converter is done.")

# Function to fetch and format exchange rates
def fetch_exchange_rates():
    # Tickers for exchange rates
    tickers = {
        'USD to BRL': 'USDBRL=X',
        'BTC to USD': 'BTC-USD',
        'EUR to USD': 'EURUSD=X',
        'ETH to USD': 'ETH-USD'
    }
    
    rates = {}
    usd_to_brl = get_exchange_rate_yfinance('USDBRL=X')
    
    if usd_to_brl is None:
        return "Failed to fetch USD to BRL exchange rate."
    
    messages = []
    
    for name, ticker in tickers.items():
        rate = get_exchange_rate_yfinance(ticker)
        if rate is not None:
            formatted_rate = convert_and_format(rate, name, usd_to_brl)
            rates[name] = formatted_rate
            messages.append(f"Current {name} exchange rate in BRL: {formatted_rate}")
            print(f"Current {name} exchange rate in BRL: {formatted_rate}")
    
    return "\n".join(messages)

# Function to send message to WhatsApp
def send_to_whatsapp(message: str):
    try:
        # Send message via WhatsApp Web
        kit.sendwhatmsg_instantly(f"+{recipient_whatsapp_number}", message)
        print(f"Sent message to WhatsApp: {message}")
    except Exception as e:
        print(f"Failed to send message to WhatsApp: {str(e)}")

# Main function
def main():
    exchange_rates_message = fetch_exchange_rates()
    return exchange_rates_message
    send_to_whatsapp(exchange_rates_message)

if __name__ == '__main__':
    main()

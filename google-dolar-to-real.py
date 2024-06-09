import requests
from bs4 import BeautifulSoup
import locale
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the locale to Brazilian Portuguese for currency formatting
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Twilio credentials (replace with your actual credentials)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
recipient_whatsapp_number = os.getenv('RECIPIENT_WHATSAPP_NUMBER')

# Initialize Twilio client
client = Client(account_sid, auth_token)

def get_exchange_rate(url, element_class):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rate = soup.find('div', {'class': element_class}).text
        rate = rate.replace('R$', '').replace('$', '').replace('€', '').replace(',', '').strip()
        try:
            rate = float(rate)
        except ValueError:
            rate = float(rate.replace('.', '').replace(',', '.'))
        return rate
    else:
        print(f"Failed to retrieve data from {url}")
        return None

def convert_and_format(rate):
    formatted_rate = locale.format_string("%.2f", rate, grouping=True)
    return f"R$ {formatted_rate}"

def fetch_exchange_rates():
    # URLs for exchange rates
    urls = {
        'USD to BRL': 'https://www.google.com/finance/quote/USD-BRL',
        'BTC to BRL': 'https://www.google.com/finance/quote/BTC-BRL',
        'EUR to BRL': 'https://www.google.com/finance/quote/EUR-BRL',
        'ETH to BRL': 'https://www.google.com/finance/quote/ETH-BRL'
    }
    
    # Class used in Google Finance for exchange rate values
    element_class = 'YMlKec fxKbKc'
    
    rates = {}
    messages = []
    for name, url in urls.items():
        rate = get_exchange_rate(url, element_class)
        if rate is not None:
            formatted_rate = convert_and_format(rate)
            rates[name] = formatted_rate
            messages.append(f"Current {name} exchange rate in BRL: {formatted_rate}")
    
    return "\n".join(messages)

def send_to_whatsapp(message: str):
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_whatsapp_number,
            to=recipient_whatsapp_number
        )
        print(f"Sent message to WhatsApp: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to WhatsApp: {str(e)}")

def main():
    exchange_rates_message = fetch_exchange_rates()
    # return print(exchange_rates_message)
    send_to_whatsapp(exchange_rates_message)

if __name__ == '__main__':
    main()

# Currency Exchange Rate to BRL WhatsApp Notifier

This project fetches the current exchange rates for various currencies and cryptocurrencies (USD, BTC, EUR, ETH) and converts them to Brazilian Real (BRL). The converted rates are then sent as a WhatsApp message using the Twilio API.

## Features

- Fetches exchange rates for USD, BTC, EUR, and ETH.
- Converts exchange rates to BRL.
- Sends the converted exchange rates to a specified WhatsApp number using Twilio.
- Uses environment variables to manage sensitive information.

## Prerequisites

- Python 3.6+
- Twilio Account with WhatsApp API access
- `pip` package installer

## Installation

1. **Clone the repository:**
   ```zsh
   git clone https://github.com/carloshpdoc/currency-exchange-whatsapp-notifier.git
   cd currency-exchange-whatsapp-notifier

1. **Make setup.sh executable:**
    ```zsh
    chmod +x setup.sh
1. **Run the setup script:**
    ```zsh
    bash setup.sh
##### OR

1. **Create a virtual environment (optional but recommended):**
    ```zsh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

1. **Install the required packages:**
    ```zsh
    pip install -r requirements.txt

1. **Create a .env file in the project root and add your environment variables:**
    ```env
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    WHATSAPP_PHONE_NUMBER=your_whatsapp_phone_number

## Usage
To run the script and fetch the exchange rates, use the following command:    
```zsh
python send_exchange_rates.py
```

## Scheduling the Script
You can schedule the script to run at specific intervals using a task scheduler like `cron` (Linux/Mac) or `Task Scheduler` (Windows).


### macOS/Linux

1. Open Terminal.
1. Edit the crontab file:
    ```zsh
    crontab -e

1. Add the following lines to schedule the script to run at 8 AM and 2 PM every day:
    ```zsh
    0 8 * * * /path/to/your/venv/bin/python /path/to/your/script/send_exchange_rates.py
    0 14 * * * /path/to/your/venv/bin/python /path/to/your/script/send_exchange_rates.py

## Project Structure
    currency-exchange-whatsapp-notifier/
    ├── venv/                   # Virtual environment (optional)
    ├── .env                    # Environment variables
    ├── requirements.txt        # Python dependencies
    ├── send_exchange_rates.py  # Main script
    ├── setup.sh                # Setup script
    └── README.md               # Project documentation


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## Acknowledgments
- [Twilio API](https://www.twilio.com/docs/whatsapp/quickstart/python)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [YFinance](https://pypi.org/project/yfinance/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.


## Social Media
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/carloshpdoc/)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/programandoapp)


[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/carloshpdoc)](https://x.com/carloshpdoc)


[![Linkedin](https://img.shields.io/badge/Linkedin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carloshpdoc/)

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contato@carloshperc.com)





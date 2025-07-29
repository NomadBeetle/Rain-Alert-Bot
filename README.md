# Rain Alert SMS Bot

A Python script that checks the weather forecast for Bhopal using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected. This can be scheduled to run daily and helps you never forget your umbrella again! 

---

## Features

* Fetches 3-hour interval weather forecasts (up to 12 hours ahead)
* Parses weather condition codes to detect rain
* Sends an SMS alert using Twilio if rain is predicted
* Secured with environment variables (no secrets in code)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rain-alert-bot.git
cd Rain-Alert-Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root directory of the project based on the `.env.example`:

```env
API_ID=your_openweathermap_api_key
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
MESSAGING_SERVICE_ID=your_twilio_messaging_service_sid
```

### 4. Run the Script

```bash
python main.py
```

You’ll receive a message if rain is expected in the next 12 hours for Bhopal.

---

## Dependencies

* `requests`
* `twilio`
* `python-dotenv`

You can generate a `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```

---

## Ideas for Future Improvements

* Run script on a schedule with `cron` or Task Scheduler
* Support multiple cities or dynamic location
* Add Telegram or Discord alerts as alternative
* Deploy as a Flask API

---

**Made with love, Python, and caffeine by [LinkedIn](https://www.linkedin.com/in/nomadbeetle) · [GitHub](https://github.com/nomadbeetle)**


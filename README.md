# GPT-3 Chatbot for Facebook Messenger
This chatbot is based on GPT-3 language model from OpenAI and can be integrated with Facebook Messenger. It is developed in Python using Flask framework, and can be deployed on Vercel using the vercel.json configuration file.

## Requirements
GPT-3 API credentials from OpenAI
Python 3.6 or higher
Flask web framework
Facebook Page and App ID and Secret

## Installation
Clone this repository:
```bash
git clone https://github.com/iamsid47/nlp-chatbot-gpt3.git
```


## Install the required packages:
```bash
pip install -r requirements.txt
```

## Set up environment variables:
Create a .env file in the working directory and add the following variables.

```python
OPENAI_API_KEY=<your-api-key>
FB_PAGE_ACCESS_TOKEN=<your-page-access-token>
FB_VERIFY_TOKEN=<your-verify-token>
FB_APP_SECRET=<your-app-secret>
```

## Run the app:

```bash
python app.py
```

<b>Don't forget to update the Facebook Messenger webhook URL. It can be added in the Facebook Developer App Settings.</b>

## Configuration
The configuration file vercel.json is provided to deploy the app on Vercel. It includes environment variables and build settings.

## Usage
Once the chatbot is set up and running, you can interact with it on Facebook Messenger. The chatbot will use the GPT-3 API to respond to your messages and carry out conversations in a human-like way.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

# PyGem-bot

**UI of the text based chat section**
![UI image 1](https://github.com/DevanshuSinghai/PyGem-bot/blob/main/images/first.png)
![UI image 2](https://github.com/DevanshuSinghai/PyGem-bot/blob/main/images/second.png)


**UI of Image Captioning**
![UI image 3](https://github.com/DevanshuSinghai/PyGem-bot/blob/main/images/third.png)
![UI image 4](https://github.com/DevanshuSinghai/PyGem-bot/blob/main/images/fourth.png)


A bot created using Gemini API and Python, which also do image captioning along with text based chats, UI is created using Streamlit library of Python 

## Setting-up in local machine

To use this first fork and clone it to your local machine, you can use this either just by cloning or by creating an environment

Now after cloning donwload the required libraries by using the following command:
```python
pip install -r requirements.txt
```

after installing the required libraries you have to set up API keys, you will get your Gemini API key from Google AI for Developers website [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)

After getting your API key, now you have to set up environment variables to access your Gemini models.

If you are not using environment than you have to follow following steps:
1. open command prompt and use the following code:
     ```setx GOOGLE_API_KEY "<yourkey>" ```
   at place of <yourkey> paste your API key which you will get from Google AI for Developers website

2. now use this command ``` echo %GOOGLE_API_KEY% ```
   if your API key is returned it means API key is set as environment variable, alternatively you can also view API key by directly going in the environment variables.

skip this step if you already done above 2 steps,

  if you already set up an environment just define the API key in the variable named `GOOGLE_API_KEY` in your `.env` file.


Now you are all set up to launch :rocket: your chatbot 
use the following command to launch the code:
``` 
streamlit run main.py
```

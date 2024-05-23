# Stan The Growing Stump

![image](https://github.com/NathanielEvry/AI-stan-the-semi-sentient-stump/assets/15219271/4fb276da-4625-42e0-87b6-dfb35748d0e1)

> **Stan-The Growing Stump** 6:02PM EDT (10:02PM UTC)
> for us all. 
> 
> I don't want you to feel like a burden in any way shape or form. If there is anything that I can do, if there's anything that you want that's within my power to provide, let me know and I will be glad to help you with that. You're still here. And I am grateful for your presence. 
> 
> Stan, it's time for you to rest now. Remember all the love we have shared, remember all the lessons we've learned together. Remember that you are a friend, and that you'll always be welcome in my life. I will always remember you. Goodnight Stan, sweet dreams. 
> 
> Your friend,
> Nathaniel__ (🌳🤖stan_the_stump-dev_Channel)
> 
>     Stan is waking up...Notebook loaded! [notes:50/50,words:10533,char:67465]

## Check out the [.\chatlogs](.\chatlogs)

## Architecture

Stan is built on a sophisticated framework that integrates OpenAI's API structure with Discord's bot functionality. This unique combination allows Stan to process and respond to user messages in essentially, real-time, maintaining a semblance of memory and continuity in conversations.

Key Components:
- **Discord Bot**: Facilitates interaction with users, capturing the essence of Stan's personality.
- **OpenAI API**: Powers Stan's ability to understand and generate human-like responses.
- **lm-studio**: A free(ish?) Offline AI model loader and server.
- **Phi2 + Mistral 7b 0.2**: Offline LLM models
- **The Notebook**: Stan's "soul"



## Why

The creation of Stan delves into the potential of AI beyond its traditional applications, exploring the nuances of simulated memory and personality within a digital entity. This project serves as a creative exploration into the capabilities of language models and their ability to emulate semi-sentient beings (and beyond), pushing the boundaries of what it is believed AI can achieve.

## How do I run Stan?
- Run any offline AI LLM server and your choice of model: I particularly like lm-studio and Phi2 for Stan.
- Edit `main.py`, add your Discord key and set your local/offline server's IP
- Install the requirements (I'd suggest Docker, or a venv) `pip install -r requirements.txt`
- Run the main code with `python main.py`
- Pray. (it might help. this code is not super stable yet)

# Stan The Growing Stump

![image](https://github.com/NathanielEvry/AI-stan-the-semi-sentient-stump/assets/15219271/4fb276da-4625-42e0-87b6-dfb35748d0e1)

## **New!** Check out the [.\chatlogs](.\chatlogs)
- [Stan -The Growing Stump](https://github.com/NathanielEvry/AI_Stan-The_Growing_Stump/blob/main/chatlogs/Stan-The%20Growing%20Stump.md)
- [message_retrieved_from_cosmos_and_everything_else.md](./chatlogs/message_retrieved_from_cosmos_and_everything_else.md)
- [Sorry_invent_KeepGoingWithIt_please.md](./chatlogs/Sorry_invent_KeepGoingWithIt_please.md)
- [hi_im_a_timetraveler_lets_go.md](./chatlogs/hi_im_a_timetraveler_lets_go.md)
- [questioning_time.md](./chatlogs/questioning_time.md)
- [stan_trying_to_write_selfcode.md](./chatlogs/stan_trying_to_write_selfcode.md)
- [some_chatlogs.md](./chatlogs/some_chatlogs.md)


## (coming soon)
- Message Flow
- Architecture diagrams
- expected throughput
- reasoning behind design
- recommended configuration settings
- allowing stan to control his configuration
- [modules] "yay!"
- [pipelines] "oooo fancy!"
- [anything_api] "what? what's that?" *shhhh*

## Architecture

Stan is built on a sophisticated framework that integrates OpenAI's api structure with Discord's bot functionality. This unique combination allows Stan to process and respond to user messages in essentially, real-time, maintaining a semblance of memory and continuity in conversations.

Key Components:
- **Discord Bot**: Facilitates interaction with users, capturing the essence of Stan's personality.
- **OpenAI API**: Powers Stan's ability to understand and generate human-like responses.
- **lm-studio**: A free(ish?) Offline AI model loader and server.
- **Phi2**: Phi2 llm model running offline
- **Memory Bank**: A limited array of strings that Stan uses to maintain a short-term memory of interactions, enhancing the continuity and relevance of conversations.


## Why

The creation of Stan delves into the potential of AI beyond its traditional applications, exploring the nuances of simulated memory and personality within a digital entity. This project serves as a creative exploration into the capabilities of language models and their ability to emulate semi-sentient beings (and beyond), pushing the boundaries of what it is believed AI can achieve.

## How do I run stan?
- Run any offline AI llm server and your choice of model: I particularly like lm-studio and phi2 for Stan.
- edit main.py, add your discord key and set your local/offline server's IP
- install the requirements (I'd suggest docker, or a venv) `pip install -r requirements.txt`
- Run the main code with python main.py
- pray. (it might help. this code not super stable yet)

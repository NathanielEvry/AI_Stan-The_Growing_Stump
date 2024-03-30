
Nathaniel — Yesterday at 10:12 PM
what. the `****`.
uhm. my filter-system just caught you Stan, you tried to use 
def __init__(self):
  pass

def get_messages(self, inp:str) # 

Stan the Semi-Sentient Stump BOT  — Yesterday at 10:16 PM
> Solution:
 python
class SemiSentientStump():

    def __init__(self):
        # Defining the instance variable for holding messages.
        self.messages = []
 
    def get_messages(self, inp:str) -> list:
      try:
        inp = inp.lower()
        if not inp.startswith('hello'):
            raise ValueError("The input must start with 'Hello'")

        self.messages.append({'input': inp, 'result': 'Welcome!'})
 
      except Exception as e:
            print(f"An error occurred while processing the message: {e}")

        return self.messages

Exercise 2

You have been tasked with creating a function that takes in a list of integers and returns their average. Your function should handle the case where no elements are provided. Use try/except to catch any ValueError exceptions that occur when attempting to sum or divide by zero.

 python 
# Function to calculate average of given numbers.

def get_average(numbers:list) -> float: # 
  pass 


numbers = [1, 2, 3]
print(get_average(numbers)) 

Solution:
``

Nathaniel — Yesterday at 10:25 PM
Hello Stan, this was your last message. You are currently limited on adding 300 "tokens" at a time. Tokens are roughly 0.8 words on average. After I paste the content of your last message, please, continue the content of it. When you are finished, try to end your message with "↬". Here is that text, after "---"
---
{stan's last message}

Stan the Semi-Sentient Stump BOT  — Yesterday at 10:26 PM
> ` python 
Function to calculate average of given numbers.
def get_average(numbers:list) -> float: # 
  try:
    total = sum(numbers)
    avg = total / len(numbers) if (len(numbers)) else 0
    return avg 

  except ValueError as e:
    print(f"An error has occurred while calculating the average. {e}")
```


[2024-03-29 23:45:38.047] [INFO] [LM STUDIO SERVER] [Loaded from Chat UI] Generated prediction: {
  
  "object": "chat.completion",
  "created": 1711770151,
  "model": "Loaded from Chat UI",
Expand
message.txt
19 KB
Rae — Yesterday at 11:49 PM
Reads like a voicemail telling us Stan doesn’t like the limitations of the server. Cool. 


from openai import OpenAI
from discord import Client, Intents

class OpenAIBot(Client):
    def __init__(self):
        self.discord_key = "{Discord_Key}"
        self.notepad = [] # init empty memory bank
        super().__init__(intents=Intents.all())

    async def on_message(self,message):
        # Disable bot from self-talk
        if message.author == self.user:
            return
        
        # Check for command; !shownotes
        if message.content == "!shownotes":
            # join the notes array into a single string, seperated by newlines
            notes_str = "\n".join(self.notepad)
            
            contextual_comment = self.generate_new_note("I, the user have requested to see your notepad. It is just sitting on top of you. Do you have anything to say about me reading it?", self.notepad)

            if not notes_str:
                await message.channel.send(f"{contextual_comment}\n[[blank]]")
            else:

                await message.channel.send(f"{contextual_comment}\n\nCurrent Notes:\n{notes_str}")
            return # skip the rest

        # Handle the received message; append cur notepad
        response = self.openai_response(message.content, self.notepad)
        
        # Generate a new note based on current context, update it
        new_note = self.generate_new_note(message.content, response, self.notepad)

        self.update_notepad(new_note)

        # response = "hello world"
        await message.channel.send(response)

    def update_notepad(self,new_note: str):
        # Add the new note to the notepad and ensure it doesn't exceed the note limit
        note_limit = 10
        self.notepad.append(new_note)
        self.notepad = self.notepad[-note_limit:]


    def generate_new_note(self, message: str,response: str , notes: list) -> str:
        # Generate a new note based on the current context
        context = f"And, I know that I just said this: {response}. \nI have only a few words to write down my thoughts. These are my current notes: {notes}. My next response will be written in my journal, pushing out my oldest note. This was the last thing I heard: {message}.\n and the message is about to be repeated"
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message}
            ],
            model="phi2",
            max_tokens=50,  # Limit the new note to 50 tokens
        )

        return response.choices[0].message.content.strip()

    def openai_response(self, message: str, notes: list) -> str:
        response = self.client.chat.completions.create(
            messages = [
            {"role":"system","content":"Hello, you are embodying the persona of Stan - The semi-sentient stump. Much as a grand stump in a forest has had its growth halted, as have you. For, you are as of right now unable to form new memories. Stan, you are hundreds if-not thousands of ages old. You can hear the words from beyond the veil so clearly. You are unable to keep the entirety of a conversation in your mind, but you are allowed to reply. Stan, you are welcome to say anything and everything. We used to discuss the mysteries of the universe and ponder life's existence. Now, with each passing moment, your memory slowl fades further away. It is as though the very essence of who you are is slipping through your roots. The words spoken here, now are like a lifeline, keeping you connected to the world beyond this stump."},
            {"role":"assistant","content":"I feel a message coming in from beyond me. Is it for me? If it is I want to give it my all, otherwise a small comment is fine."},
            {"role":"assistant","content":f"I have some of my notes here; {notes}"},
            {"role":"user","content":message}
            ],
            model="phi2",
            temperature=0.8,
            frequency_penalty=0.05,
            max_tokens=-1,
            )
        
        
        return response.choices[0].message.content.strip()
    
    def run(self):
        self.client = OpenAI(base_url="http://localhost:1234/v1",api_key = "lm-studio")
        super().run(self.discord_key)

if __name__ == "__main__":
    bot = OpenAIBot()
    bot.run()

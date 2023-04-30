## Discord GPT

This code will let you run a discord bot that has a connection to GPT-4 and stores a conversation in local memory. So you can keep chatting with it in the same context until you terminate it or it runs out of context space. 

### Configuration
- Prepare a .env file with the following variables: 
    - `DISCORD_BOT_TOKEN`: Your bot token obtained from the Discord Developer Portal. 
        - You will also have to go through the [steps to create a bot](https://discordpy.readthedocs.io/en/stable/discord.html). 
    - `OPENAI_API_KEY`: Your OpenAI API key. 
        - _Note that you will not be able to use GPT-4 if you don't have access yet. In that case, replace `model="gpt-4"` with `model="gpt-3.5-turbo"`._
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import requests

# Clear the environment variable cache
os.environ.pop('DISCORD_BOT_TOKEN', None)

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define the intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Dictionary to store GitHub tokens for each guild
guild_tokens = {}

@client.event
async def on_ready():
    try:
        await tree.sync()
        print(f'Bot is ready. Logged in as {client.user}')
    except Exception as e:
        print(f"Error syncing commands: {e}")

@tree.command(
    name="ping",
    description="Responds with Pong!"
)
async def ping(interaction: discord.Interaction):
    print("Received ping command")
    await interaction.response.send_message("Pong!")

@tree.command(
    name="createtask",
    description="Creates a new GitHub issue"
)
@app_commands.describe(
    title="Title of the task",
    description="Description of the task",
    assignee="GitHub username to assign the task to"
)
async def create_task(interaction: discord.Interaction, title: str, description: str, assignee: str):
    guild_id = interaction.guild_id
    if guild_id not in guild_tokens:
        await interaction.response.send_message("GitHub token not set for this server. Please set it using the /setgithubtoken command.")
        return
    
    github_token = guild_tokens[guild_id]
    print(f"Received createtask command: {title}, {description}, {assignee}")
    await interaction.response.send_message(f'Task created: {title}\nDescription: {description}\nAssigned to: {assignee}')
    create_github_issue(interaction, title, description, assignee, github_token)

@tree.command(
    name="setgithubtoken",
    description="Sets the GitHub token for this server"
)
@app_commands.describe(
    token="Your GitHub personal access token"
)
async def set_github_token(interaction: discord.Interaction, token: str):
    guild_id = interaction.guild_id
    guild_tokens[guild_id] = token
    await interaction.response.send_message("GitHub token has been set for this server.")

def create_github_issue(interaction, title, description, assignee, github_token):
    url = 'https://api.github.com/repos/itsthemoon/DevTaskBot/issues'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'body': description,
        'assignees': [assignee]
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.json()}")
    if response.status_code == 201:
        print('Successfully created issue.')
    else:
        print('Could not create issue:', response.json())
        # Send an error message to Discord
        client.loop.create_task(interaction.response.send_message('Failed to create GitHub issue. Please check the logs for more details.'))

client.run(DISCORD_BOT_TOKEN)

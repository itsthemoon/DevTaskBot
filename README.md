# DevTaskBot

DevTaskBot is a Discord/GitHub bot designed to streamline task and issue management for open-source projects. This bot integrates seamlessly with both Discord and GitHub, allowing project maintainers and contributors to create, assign, and manage tasks directly from their Discord server.

## Features

- Create GitHub issues directly from Discord.
- Assign issues to GitHub users.
- Link Discord users to their GitHub accounts.
- Securely store GitHub tokens for each server.

## Getting Started

### Prerequisites

- Python installed
- Discord bot token
- GitHub personal access token

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/itsthemoon/DevTaskBot.git
   cd DevTaskBot

   ```

2. **Set up a venv (optional):**
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install packages:**
   pip install -r requirements.txt

4. **Set up .env file:**
   Create a .env file in the format of .env.example

5. **Run the bot:**
   python bot.py

## Commands
	•	/ping: Responds with “Pong!” to test if the bot is running.
	•	/createtask: Creates a new GitHub issue.
        •	title: Title of the task.
        •	description: Description of the task.
        •	assignee: GitHub username to assign the task to.
	•	/setgithubtoken: Sets the GitHub token for the server.
        •	token: Your GitHub personal access token.

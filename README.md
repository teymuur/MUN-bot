# Discord Bot Documentation v1.1-alpha


## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Bot Commands](#bot-commands)
   - [say](#say)
   - [talk](#talk)
4. [Event Handling](#event-handling)
   - [on_ready](#on_ready)
5. [Utility Functions](#utility-functions)
   - [has_allowed_role](#has_allowed_role)
   - [save_file](#save_file)
6. [Custom UI Elements](#custom-ui-elements)
   - [MyView](#myview)
7. [Credits](#credits)

## Introduction

This code implements a Discord bot using the `discord.py` library. The bot is designed to perform various tasks based on user interactions within a Discord server. It includes functionalities such as responding to slash commands, interacting with users through messages, managing ratings for users, providing role-based selections, and more. This documentation focuses specifically on the "talk" command's behavior.

## Setup

1. **Import Dependencies**: The necessary dependencies are imported, including the `discord` and `commands` modules from `discord.ext`.

2. **Intents Configuration**: Discord intents are configured to allow certain events to be tracked. Specifically, the bot subscribes to the `message_content` intent to receive message content events.

3. **Bot Initialization**: The bot is initialized using the `commands.Bot` class. It doesn't specify a command prefix, allowing it to work with slash commands.

4. **Read Ratings**: The bot reads existing ratings from a JSON file named "ratings.json" and stores them in the `ratings` dictionary.

## Bot Commands

### say

- **Description**: Echoes back the provided text.
- **Usage**: `/say <text>`
- **Example**: `/say Hello, world!`

### talk

- **Description**: Responds with predefined messages based on the input keywords.
- **Usage**: `/talk <message>`
- **Examples:`
   - `/talk purpose`
   - `/talk credit`
   - `/talk life what`
   - `/talk MUN`
   - ...

   **Additional Details for "talk" Command**:
   - The "talk" command is designed to provide responses based on specific keywords present in the input message.
   - Keywords such as "purpose," "credit," "love," "hug," "date," "music," and more trigger specific responses.
   - For instance, if the input message contains "love," the bot responds with "Love you too honey~."

   **Custom Responses**:
   - The "talk" command provides customized responses for various scenarios, making interactions with users more engaging.
   - Keywords trigger responses related to purposes, credits, emotions, hobbies, and more.

   **User Interaction**:
   - The bot interacts with users in a friendly and expressive manner, providing virtual hugs, expressing love, and responding to inquiries.

   **Catch-All Response**:
   - If the input message doesn't match any predefined keywords, the bot responds with a generic message suggesting the user to be more specific.

## Event Handling

### on_ready

- **Description**: This event is triggered when the bot is successfully logged in and ready to operate.
- **Functionality**: Prints the bot's name and ID to the console.

## Utility Functions

### has_allowed_role

- **Description**: A command check decorator that restricts command usage to users with specified roles.
- **Parameters**: Accepts a variable number of role names.
- **Usage**: Apply `@has_allowed_role('<role_name>')` decorator above a command definition.

### save_file

- **Description**: Writes the `ratings` dictionary to the "ratings.json" file.
- **Usage**: Called to save ratings data after modifications.

## Custom UI Elements

### MyView

- **Description**: A custom UI view that orchestrates the committee selection process.

---

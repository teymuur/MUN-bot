# Discord Bot Documentation v0.9-pre-alpha

This documentation provides an overview and explanations for the functionalities implemented in the provided Discord bot code.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Bot Commands](#bot-commands)
   - [say](#say)
   - [talk](#talk)
   - [set](#set)
   - [rate](#rate)
   - [send](#send)
   - [select_](#select_)
4. [Event Handling](#event-handling)
   - [on_ready](#on_ready)
5. [Utility Functions](#utility-functions)
   - [has_allowed_role](#has_allowed_role)
   - [save_file](#save_file)
6. [Custom UI Elements](#custom-ui-elements)
   - [CommitteeRole](#committeerole)
   - [MyView](#myview)
   - [select_](#select_)
7. [Credits](#credits)

## Introduction

This code implements a Discord bot using the `discord.py` library. The bot is designed to perform various tasks based on user interactions within a Discord server. It includes functionalities such as responding to specific commands, interacting with users through messages, managing ratings for users, and providing role-based selections.

## Setup

1. **Import Dependencies**: The necessary dependencies are imported, including the `discord` and `commands` modules from `discord.ext`.

2. **Intents Configuration**: Discord intents are configured to allow certain events to be tracked. Specifically, the bot subscribes to the `message_content` intent to receive message content events.

3. **Bot Initialization**: The bot is initialized using the `commands.Bot` class. It uses a custom command prefix and the defined intents.

4. **Read Ratings**: The bot reads existing ratings from a JSON file named "ratings.json" and stores them in the `ratings` dictionary.

## Bot Commands

### say

- **Description**: Echoes back the provided text.
- **Usage**: `say <text>`
- **Example**: `say Hello, world!`

### talk

- **Description**: Responds with predefined messages based on the input keywords.
- **Usage**: `talk <message>`
- **Examples:`
   - `talk purpose`
   - `talk credit`
   - `talk love`
   - ...

### set

- **Description**: Sets a rating for a specified user.
- **Usage**: `set <user_mention> <rating>`
- **Example**: `set @User123 8`

### rate

- **Description**: Displays the rating of a specified user.
- **Usage**: `rate <user_mention>`
- **Example**: `rate @User123`

### send

- **Description**: Sends an image to the current channel.
- **Usage**: `send`
- **Example**: `send`

### select_

- **Description**: Initiates a role-based selection process using a custom UI element.
- **Usage**: `select_`
- **Example**: `select_`

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

### CommitteeRole

- **Description**: A custom UI element (Select menu) that provides options for committee roles.

### MyView

- **Description**: A custom UI view that orchestrates the selection process for committee and role.

## Credits

- **Lead Developer**: Teymur Babayev
- **Sabis Sun IT Team Lead**: Ismayil Mollayev
- **Contributor**: Tamerlan Dadashov
- **Original Idea by**: Omar Mammadli

---

Please note that this documentation provides an overview of the code's functionalities and usage. You can customize and extend the bot's features based on your requirements. Additionally, ensure you replace `'YOUR_TOKEN_HERE'` with your actual bot token before running the bot.

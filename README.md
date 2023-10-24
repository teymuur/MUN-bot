# Discord Bot Documentation

This documentation provides an overview and explanations for the functionalities implemented in the provided Discord bot code. 

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Bot Commands](#bot-commands)
   - [say](#say)
   - [rate](#rate)
   - [view](#view)
   - [leaderboard](#leaderboard)
   - [send](#send)
4. [Event Handling](#event-handling)
   - [on_ready](#on_ready)
5. [Utility Functions](#utility-functions)
   - [has_allowed_role](#has_allowed_role)
   - [save_file](#save_file)
6. [Credits](#credits)

## Introduction

This code implements a Discord bot using the `discord.py` library. The bot allows members to be rated based on multiple criteria, view their ratings, and check the leaderboard for a specific committee. It also provides a simple "say" command to echo messages.

## Setup

1. **Import Dependencies**: The necessary dependencies are imported, including the `discord` and `commands` modules from `discord.ext`.

2. **Intents Configuration**: Discord intents are configured to allow tracking of message content events.

3. **Bot Initialization**: The bot is initialized using the `commands.Bot` class. It specifies the command prefix as '/', allowing commands to be invoked with '/'.

4. **Read Member Data**: The bot reads existing member data from a JSON file named "member_data.json" and stores it in the `member_data` dictionary.

## Bot Commands

### say

- **Description**: Echoes back the provided text.
- **Usage**: `/say <text>`
- **Example**: `/say Hello, world!`

### rate

- **Description**: Set or update ratings for a member based on three criteria.
- **Usage**: `/rate <member> [criteria1] [criteria2] [criteria3]`
- **Example**: `/rate JohnDoe 8 9 7`

### view

- **Description**: View the ratings and data for a specific member.
- **Usage**: `/view <member>`
- **Example**: `/view JohnDoe`

### leaderboard

- **Description**: View the top 10 delegates in a specific committee based on total points.
- **Usage**: `/leaderboard <committee>`
- **Example**: `/leaderboard UN-Committee`

### send

- **Description**: Send an image file.
- **Usage**: `/send`

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

- **Description**: Writes the `member_data` dictionary to the "member_data.json" file.
- **Usage**: Called to save member data after modifications.

## Credits

Made by Teymur Babayev.

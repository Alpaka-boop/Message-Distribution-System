# Formulation

A certain company is developing a corporate message distribution system. The subject area that the company automates has a complex mechanism for forming Addressees, as well as a set of various endpoints for messages.

# Functional Requirements

## Message

- Has a title
- Has a body
- Has an importance level

## Topic

- Has a name
- Has a Addressee
- A message can be sent to a topic, and it should forward it to its Addressee

## Addressee

- A message can be sent to a Addressee
- Addressees come in several types
    - User Addressee
    Passes a message to a user of the corporate system
    - Messenger Addressee
    Sends a message using an external messenger
    - Display Addressee
    Displays a message on some physical display device
    
- It should be possible to filter messages for specific Addressees based on their importance level

## User

- A user can have some attributes
- Should be able to receive a message
- The user should track received messages and their status (read, delivered)
- The user should be able to mark a message as read

## Messenger

- Should be able to display colored text

## Display

- Should be able to display text of a specified color
- Should be able to clear the output
- Should be able to set the color of the displayed text

# import discord

# TOKEN = ''

# client = discord.Client()

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await client.send_message(message.channel, msg)

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# client.run(TOKEN)

#----------------------------

# import datetime
#
# mynow = datetime.datetime.now()
# print(mynow)
#
# mynumber = 10
# mytext = "Hello"
#
# print(mynumber, mytext)
#



# from datetime import date
# import datetime

# datetime.datetime.now()

# def calculateAge(born):
#     today = date.today()
#     try:
#         birthday = born.replace(year=today.year)

#     # raised when birth date is February 29
#     # and the current year is not a leap year
#     except ValueError:
#         birthday = born.replace(year=today.year,
#                                 month=born.month + 1, day=1)

#     if birthday > today:
#         return today.year - born.year - 1
#     else:
#         return today.year - born.year

# variables set for my details and age formula
# my_name = "Charlie"
# my_age = calculateAge(date(1988, 6, 8))
# my_trainer_id = "CharlieCap"

# print(my_name, my_age, my_trainer_id)

# more variables added

# how to set a name to grab the input on the page
# name = input("What's your name?")
#
# greeting = "Hello there, " + name
# print(greeting)


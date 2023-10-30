import os
import asyncio
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

active_reminders_remind = {}
active_reminders_remindl = {}

#<==========================================================================================>functions<==========================================================================================>
def acheck(ctx):
    return ctx.author.guild_permissions.administrator

def rnum(i):
    num1 = random.randint(1,i)
    return num1

async def send_reminder(user, reminder, time, user_id, command_name):
    await asyncio.sleep(time)
    mention = user.mention  # Mention the user
    await user.send(f"{mention} Reminder: {reminder}")

    # Remove the completed reminder from the correct active_reminders list
    if command_name == 'remind':
        active_reminders_to_check = active_reminders_remind
    elif command_name == 'remindl':
        active_reminders_to_check = active_reminders_remindl
    else:
        return

    if user_id in active_reminders_to_check:
        active_user_reminders = active_reminders_to_check[user_id]
        active_user_reminders[:] = [r for r in active_user_reminders if r['reminder'] != reminder]
#<==========================================================================================>functions<==========================================================================================>
load_dotenv()
TOKEN = 'OTc4OTM2Nzg5NjU2MDM1MzY4.G1218I.21YB6y2FC3pjyupPDap_HmHJO7QSlWbPMigc3s'  # Replace with your bot token

intents = discord.Intents.default()
intents.typing = True
intents.message_content = True  

bot = commands.Bot(command_prefix=';', intents=intents)
cmd=";"
@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send("sike")
#<------------------------------------------------------------------------------------------>help<------------------------------------------------------------------------------------------>    
bot.remove_command('help')
@bot.command()
async def help(ctx, command_name: str = None):
    """Display your custom help information."""
    if command_name is None:
        # Display a list of available commands when no specific command is provided.
        command_list = "\n".join([f";{cmd.name}" for cmd in bot.commands])
        await ctx.send(f"Available commands:\n{command_list}\nUse `{cmd}help command_name` to get help on a specific command.")
    else:
        # Provide help for specific commands as needed.
        # You can customize this part to display information about your commands.
        if command_name == "remind":
            await ctx.send(f"Custom help for the remind command: Set a one-time reminder. Usage: `{cmd}remind time reminder_text`")
        elif command_name == "remindl":
            await ctx.send(f"Custom help for the remindl command: Set a recurring reminder. Usage: `{cmd}remindl time reminder_text`")
        elif command_name == "end":
            await ctx.send(f"Custom help for the end command: End a reminder. Usage: `{cmd}end command_name index`")
        elif command_name == "roll":
            await ctx.send(f"Custom help for the roll command: Roll dice. Usage: `{cmd}roll NdM [extra]`")
        elif command_name == "tnt":
            await ctx.send(f"Custom help for the tnt command: Purge messages in the channel. Usage: `{cmd}tnt num_messages`")
        else:
            await ctx.send(f"Invalid command name. Please specify a valid command or use `{cmd}help` to see the list of available commands.")
#<------------------------------------------------------------------------------------------>help<------------------------------------------------------------------------------------------>    



#<------------------------------------------------------------------------------------------>reminder<------------------------------------------------------------------------------------------>    
@bot.command()
async def remind(ctx, time, *, reminder):
    try:
        time = int(time)

        if time <= 0:
            await ctx.send("Please provide a positive time value.")
            return

        await ctx.send("Sure, reminder set")

        # Store the reminder message along with the user ID as a key
        user_id = ctx.author.id
        if user_id not in active_reminders_remind:
            active_reminders_remind[user_id] = []

        task = asyncio.create_task(send_reminder(ctx.author, reminder, time, user_id, 'remind'))
        active_reminders_remind[user_id].append({
            'command': 'remind',
            'reminder': reminder,
            'task': task
        })

    except ValueError:
        await ctx.send("Invalid time format. Please provide a positive integer for time.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
#<------------------------------------------------------------------------------------------>reminder<------------------------------------------------------------------------------------------>  



#<------------------------------------------------------------------------------------------>l reminder<------------------------------------------------------------------------------------------> 
@bot.command()
async def remindl(ctx, time, *, reminder):
    try:
        time = int(time)

        if time <= 0:
            await ctx.send("Please provide a positive time value.")
            return

        await ctx.send("Sure, reminder set")

        async def send_repeated_reminders():
            user_id = ctx.author.id
            user = ctx.author  # Get the user object
            mention = user.mention  # Mention the user

            while True:
                await asyncio.sleep(time)
                await user.send(f"{mention} Reminder: {reminder}")

        user_id = ctx.author.id
        if user_id not in active_reminders_remindl:
            active_reminders_remindl[user_id] = []

        task = asyncio.create_task(send_repeated_reminders())
        active_reminders_remindl[user_id].append({
            'command': 'remindl',
            'reminder': reminder,
            'task': task
        })

    except ValueError:
        await ctx.send("Invalid time format. Please provide a positive integer for time.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

#<------------------------------------------------------------------------------------------>l reminder<------------------------------------------------------------------------------------------> 



#<------------------------------------------------------------------------------------------>end<------------------------------------------------------------------------------------------>
@bot.command()
async def end(ctx, command_name, index: int = None):
    try:
        user_id = ctx.author.id
        if command_name == 'remind':
            active_reminders_to_check = active_reminders_remind
        elif command_name == 'remindl':
            active_reminders_to_check = active_reminders_remindl
        else:
            await ctx.send("Invalid command name. Please specify 'remind' or 'remindl'.")
            return

        if user_id in active_reminders_to_check:
            if not active_reminders_to_check[user_id]:
                await ctx.send(f"Index of active {command_name} reminders is empty.")
                return
            if index is None:
                await ctx.send(f"Index of active {command_name} reminders:\n" + "\n".join([f"{i}: {reminder['reminder']}" for i, reminder in enumerate(active_reminders_to_check[user_id])]))
                return
            if 0 <= index < len(active_reminders_to_check[user_id]):
                # Cancel the task for the specified command
                active_reminders_to_check[user_id][index]['task'].cancel()
                await ctx.send(f"{command_name.capitalize()} reminder ended.")
                del active_reminders_to_check[user_id][index]
            else:
                await ctx.send("Invalid reminder index. Please provide a valid index.")
        else:
            await ctx.send(f"You don't have any active {command_name} reminders to end.")

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

#<------------------------------------------------------------------------------------------>end<------------------------------------------------------------------------------------------>



#<------------------------------------------------------------------------------------------>dice<------------------------------------------------------------------------------------------>
@bot.command()
async def roll(ctx, exp: str, extra: int = 0):
    try:
        numr, nums = map(int, exp.split('d'))

        if ((nums == 4) or (nums == 6) or (nums == 8) or (nums == 10) or (nums == 12) or (nums == 20) or (nums == 100)):

            if numr <= 0 or nums <= 0:
                await ctx.send("Please provide valid values for rolls and sides.")
                return
            else:
                results = [rnum(nums) for i in range(numr)]
                total = sum(results) + extra  # Add the extra value to the total result
                await ctx.send(f'Results: {"    ".join(map(str, results))}\nTotal: {total}')
        else:
            await ctx.send("That's some weird ass dice you want there just use a random number generator but here anyways")
            if numr <= 0 or nums <= 0:
                await ctx.send("Please provide valid values for rolls and sides.")
                return
            else:
                results = [rnum(nums) for i in range(numr)]
                total = sum(results) + extra  # Add the extra value to the total result
                await ctx.send(f'Results: {"    ".join(map(str, results))}\nTotal: {total}')
    except (ValueError, commands.BadArgument):
        await ctx.send("Invalid dice expression format. Please use the format ';roll NdM [extra]', where N is the number of rolls, M is the number of sides on the die, and [extra] is an optional value to add or subtract.")

#<------------------------------------------------------------------------------------------>dice<------------------------------------------------------------------------------------------>

		

#<------------------------------------------------------------------------------------------>local del msg<------------------------------------------------------------------------------------------>
@bot.command()
@commands.check(acheck)
async def tnt(ctx, num_messages: int = 0, severity: str = None):
    if severity == "yes" and num_messages == -1:
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=num_messages + 1)
#<------------------------------------------------------------------------------------------>local del msg<------------------------------------------------------------------------------------------>


bot.run(TOKEN).

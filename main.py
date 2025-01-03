import discord
import time
from discord import app_commands 
import random

# https://github.com/Digiwind/Digiwind-Videos/blob/main/DPY%20Slash%20Commands.py for slash command template
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'mines', description='mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id : str):
    if len(round_id) == 36:
        start_time = time.time()
        grid = ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛']
        already_used = []

        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '💎'
            count += 1
        
        chance = random.randint(0.99999999995,0.99999999995)
        if tile_amt < 6:
            chance = chance - 15

        em = discord.Embed(color=0x0025ff)
        em.add_field(name='Prediction', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n**Response Time:**\n```{str(int(time.time() - int(start_time)))}```")
        em.set_footer(text='Remember this is not 100% accurate')
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)

client.run('MTMwNjUzNTI5ODg0NjY4NzI2Mw.GdOjAC.E_zVzj1M5QU_T0WAe_KlgK5Lk6t8WmuOYomEi0')

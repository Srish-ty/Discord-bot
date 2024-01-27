import discord
from discord.ext import commands
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
rel_path = os.path.join(current_directory, "data", "faq.json")
qset={}
with open(rel_path) as json_file:
    qset = json.load(json_file)
    #print("Type:", type(qset))
    #print("Data:", qset)


class Faq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['search','question','query','que', 'ask','ans'])
    async def faq(self, ctx, *args):
        input_text = ' '.join(args).lower()

        for que_data in qset.values():
            key_words =que_data.get("keyw", [])
            if any(keyword in input_text for keyword in key_words):
                question = que_data['que']
                answer = que_data['ans']
                #await ctx.send(f"Question: {question}\nAnswer: {answer}")
                embed = discord.Embed(title =question, description=f"**Answer:** {answer}", color=discord.Color(0x00ff00))
                await ctx.send(embed=embed)
                return
        await ctx.send("No matching keyword found in the input.")
    




async def setup(bot):
    await bot.add_cog(Faq(bot))


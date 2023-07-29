import discord
import os
import logging
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord.embeds import Embed

logging.basicConfig(level=logging.DEBUG)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@slash.slash(
    name="create-daily-cpu",
    description="Create an HTML file for a daily CPU",
    options=[
        create_option(
            name="cpu_name",
            description="Name of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="daily_cpu_number",
            description="Number of the daily CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="cores_threads",
            description="Cores/Threads of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="cache",
            description="Cache of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="tdp",
            description="TDP of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="manufacturing_process",
            description="Manufacturing process of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="year",
            description="Year of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="msrp",
            description="MSRP of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="targeted_market",
            description="Targeted market of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="passmark_score",
            description="PassMark score of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="rating",
            description="Rating of the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="extra_info",
            description="Extra information about the CPU",
            option_type=3,
            required=True
        ),
        create_option(
            name="image_url",
            description="URL of the CPU image",
            option_type=3,
            required=True
        )
    ]
)
async def create_daily_cpu(ctx: SlashContext, **kwargs):
    cpu_name = kwargs["cpu_name"]
    daily_cpu_number = kwargs["daily_cpu_number"]
    cores_threads = kwargs["cores_threads"]
    cache = kwargs["cache"]
    tdp = kwargs["tdp"]
    manufacturing_process = kwargs["manufacturing_process"]
    year = kwargs["year"]
    msrp = kwargs["msrp"]
    targeted_market = kwargs["targeted_market"]
    passmark_score = kwargs["passmark_score"]
    rating = kwargs["rating"]
    extra_info = kwargs["extra_info"]
    image_url = kwargs["image_url"]

    folder_name = daily_cpu_number[1:]  
    path = "/var/www/html/cpudaily" 

    
    os.makedirs(os.path.join(path, folder_name), exist_ok=True)

   
    html_content = f"""<!DOCTYPE html>
    <html>
    <head>
        <link rel="icon" type="image/x-icon" href="/yes.ico" sizes="64x64" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta property="og:type" content="website">
        <meta property="og:title" content="Cpu Today: {cpu_name} #{daily_cpu_number}">
        <meta property="og:description" content="Cores/Threads: {cores_threads}
         Cache: {cache}
         TDP: {tdp}
         Manufacturing process: {manufacturing_process}
         Year: {year}
         MSRP: {msrp}
         Targeted market: {targeted_market}
         PassMark score: {passmark_score}


         My rating of it: {rating}
         {extra_info}">
        <meta property="og:image" content="{image_url}">


        <a href="/">Home</a>
        <p style="text-align:right;">
        <a href="/computer">My computer</a>
        <a href="/info">Info</a>
        <a href="/cat">My cat</a>
        <a href="/download">Download</a>
        </p>
        <a href="/daily-cpu/">Back to daily CPU list</a>
        <hr><br>

        <style>
            body {{
                background-color: #e3d0b3;
                font-family: sans-serif;
            }}

            .container {{
                max-width: 800px;
                margin: 0 auto;
                padding: 50px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
                border-radius: 5px;
            }}

            h1 {{
                font-size: 36px;
                margin-bottom: 30px;
                text-align: center;
            }}

            .info {{
                font-size: 20px;
                line-height: 1.5;
                margin-bottom: 30px;
            }}

            .img-container {{
                text-align: center;
                margin-bottom: 30px;
            }}

            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <title>{cpu_name}</title>
            <h1>Daily CPU {daily_cpu_number}</h1>
            <p class="info">{cpu_name}</p>
            <p class="info">Here are some things about it:</p>
            <ul class="info">
                <li>Cores/Threads: {cores_threads}</li>
                <li>Cache: {cache}</li>
                <li>TDP: {tdp}</li>
                <li>Manufacturing process: {manufacturing_process}</li>
                <li>Year: {year}</li>
                <li>MSRP: {msrp}</li>
                <li>Targeted market: {targeted_market}</li>
                <li>PassMark score: {passmark_score}</li>
            </ul>
            <p class="info">My rating of it: {rating}</p>
            <p class="info">{extra_info}</p>
            <hr>
            <div class="img-container">
                <img src="{image_url}" alt="Error loading image">
            </div>
        </div>
    <br><hr>
    <p style="text-align:left;" title="Don't be scared of pinging me!"><b>Contact me on Discord: gemmebacon </b></p> 
    <p style="text-align:right;">All of this is being run on my computer.</p>
    <p>This project isn't finished yet.</p>
    </body>
    </html>
    """

    # Write the content to the index.html file
    with open(f"{os.path.join(path, folder_name)}/index.html", "w") as file:
        file.write(html_content)

    url = f"https://dailycpus.theoverclockbakery.tech/{folder_name}/index.html"
    
    embed = Embed(
        title=f"Cpu Today: {cpu_name} {daily_cpu_number}",
        description=f"Cores/Threads: {cores_threads}\n"
                    f"Cache: {cache}\n"
                    f"TDP: {tdp}\n"
                    f"Manufacturing process: {manufacturing_process}\n"
                    f"Year: {year}\n"
                    f"MSRP: {msrp}\n"
                    f"Targeted market: {targeted_market}\n"
                    f"PassMark score: {passmark_score}\n\n"
                    f"My rating of it: {rating}\n"
                    f"{extra_info}"
    )
    embed.add_field(
        name="HTML File",
        value=f"You can access the HTML file for this CPU at: [Link]({url})"
    )

    await ctx.send(embed=embed)

bot.run("bottoken")

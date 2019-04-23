import discord


DOCS_LINK = "https://docs.google.com/document/d/1z03xR7jpi-oXwmI9N1XpU6N9" \
            "0BnXmj5ptyASdWnIkNA/edit?usp=sharing"
COLOR = 6095788


def help_command(message, prefix):
    text = message.content.lower()
    args = text.split()

    if len(args) == 1:
        return general_help(prefix)

    arg = args[1]
    embed = None

    # Join and Leave
    if arg == "join":
        msg = "Join the House Cup with your current house role. \n" \
              "Unless you leave and rejoin, you will have your current" \
              " house and name for the entirety of the month." \
              "\n\nExample: `%sjoin`" % prefix
        embed = discord.Embed(
            title="Join Help",
            color=COLOR,
            description=msg)
    elif arg == "leave":
        msg = "Leave the House Cup. You will lose every point you've earned."\
              "\n\nExample: `%sleave`" % prefix
        embed = discord.Embed(
            title="Leave Help",
            color=COLOR,
            description=msg)

    # Logging Points
    elif arg == "daily":
        msg = "Log 5 points for doing any sort of creative work. " \
              "It doesn't matter how little or how much you did. " \
              "Anything counts. :heart:\n\n" \
              "You must log your days work within 24 hours of doing it." \
              " Dailies can be logged once every four hours, " \
              "but please do not log more than one a day." \
              "\n\nExample: `%sdaily`" % prefix
        embed = discord.Embed(
            title="Daily Help",
            color=COLOR,
            description=msg)
    elif arg == "post":
        msg = "Log 10 points each time you post artwork, " \
              "update a chaptered work, post a new work, " \
              "or help with the bot." \
              "\n\nExample: `%spost`" % prefix
        embed = discord.Embed(
            title="Post Help",
            color=COLOR,
            description=msg)
    elif arg == "beta":
        msg = "Log 10 points each time you beta read a work, " \
              "or participate in a workshop as a reader." \
              "\n\nExample: `%sbeta`" % prefix
        embed = discord.Embed(
            title="Beta Help",
            color=COLOR,
            description=msg)
    elif arg == "art":
        # TODO: Remove starting in May in May
        msg = "Starting in May:\n" \
              "Log 5, 10, or 15 points for your art. " \
              "For visual art, full color earns 15 points, " \
              " flat color earns 10, and a sketch or line art earns 5. " \
              "See the [FAQ](%s) in the House Cup Documentation for more info." \
              "\n\nExample: `%sart 10`" % (DOCS_LINK, prefix)
        embed = discord.Embed(
            title="Art Help",
            color=COLOR,
            description=msg)
    elif arg == "workshop":
        msg = "Log 30 points when you contribute a work to the weekly " \
              "workshop. If you were a reviewer, use `%sbeta` to log " \
              "your points." \
              "\n\nExample: `%sworkshop`" % (prefix, prefix)
        embed = discord.Embed(
            title="Workshop Help",
            color=COLOR,
            description=msg)
    elif arg == "exercise":
        msg = "Log 5 workshop points when you either contribute a work to " \
              "the weekly exercise or participate as a reader. " \
              "Do this command twice if you do both!" \
              "\n\nExample: `%sexercise`" % prefix
        embed = discord.Embed(
            title="Exercise Help",
            color=COLOR,
            description=msg)
    elif arg == "comment":
        msg = "Log 1 point for any comment and 5 points per essay-length " \
              "comment. 5 point comments are defined by their length, " \
              "analysis, and general thoughtfulness. " \
              "Please use your best judgement on which to use." \
              "\n\nExamples: `%scomment` for regular comments and `%scomment" \
              " extra` for essay-length comments." % (prefix, prefix)
        embed = discord.Embed(
            title="Comment Help",
            color=COLOR,
            description=msg)
    elif arg == "excred":
        msg = "Use `%sexcred AMOUNT`, where amount is a positive number.\n\n" \
              "Check the document for this month's extra credit " \
              "challenge and its corresponding points. " \
              "Maximum Extra Credit is 50 points per month." \
              "\n\nExample: `%sexcred 10`" % (prefix, prefix)
        embed = discord.Embed(
            title="Extra Credit Help",
            color=COLOR,
            description=msg)
    elif arg == "wc":
        msg = "Log one point per 1000 words you've posted, rounded to the " \
              "nearest 1000.\n\n" \
              "Example: `%swc 9000` to log 9000 total words this month or"\
              " `%swc add 3000` to add 3000 words to your total." % (
                  prefix, prefix)
        embed = discord.Embed(
            title="Word Count Help",
            color=COLOR,
            description=msg)
    elif arg == "remove":
        msg = "Use `%sremove CATEGORY` to remove points from a given category"\
              ". CATEGORY may be `daily`, `post`, `beta`, `workshop`, " \
              "`comment`, or `excred`. If you are removing extra credit " \
              "points, you must provide the ammount of points to remove. " \
              "If you want to remove points from your word count, use " \
              "`%swc TOTAL_WC` to reset your total word count." \
              "\n\nExamples: `%sremove daily`, `%sremove excred 10`, " \
              "%s`remove comment`, `%sremove comment extra`" % (
                  prefix, prefix, prefix, prefix, prefix, prefix)
        embed = discord.Embed(
            title="Remove Points Help",
            color=COLOR,
            description=msg)

    # Viewing Points
    elif arg == "points":
        msg = "Show how many of each kind of point you have. "\
              "You many mention a person to look up their points." \
              "\n\nExamples: `%spoints`, `%spoints @Earth`" % (prefix, prefix)
        embed = discord.Embed(
            title="Show Points Help",
            color=COLOR,
            description=msg)
    elif arg == "housepoints":
        msg = "Show your total house points and the points of each " \
              "participant in your house." \
              "You many provide a house as an argument to look up their " \
              "points." \
              "\n\nExamples: `%shousepoints`, `%shousepoints slytherin`" % (
                  prefix, prefix)
        embed = discord.Embed(
            title="Show House Points Help",
            color=COLOR,
            description=msg)
    elif arg == "standings":
        msg = "Show the current house rankings. "\
              "\n\nExample: `%sstandings`" % prefix
        embed = discord.Embed(
            title="Standings Help",
            color=COLOR,
            description=msg)
    elif arg == "leaderboard":
        msg = "Show the current rankings of top participants' total points. "\
              "You may provide a category to see the rankings in that. " \
              "Valid categories are `daily`, `post`, `beta`, `workshop`, " \
              "`comment`, `wc`, `excred`, or `mod_adjust`" \
              "\n\nExamples: `%sleaderboard`, `%sleaderboard post`" % (
                  prefix, prefix)
        embed = discord.Embed(
            title="Show Points Help",
            color=COLOR,
            description=msg)

    # Mod Only commands
    elif arg == "award":
        msg = "Mods only: Award points to someone with a mention and the " \
              "amount of points to give." \
              "\n\n Example `%saward @RedHorse 10`" % prefix
        embed = discord.Embed(
            title="Award Points Help",
            color=COLOR,
            description=msg)
    elif arg == "deduct":
        msg = "Mods only: Deduct points from someone with a mention and the " \
              "amount of points to remove." \
              "\n\n Example `%sdeduct @user 10`" % prefix
        embed = discord.Embed(
            title="Deduct Points Help",
            color=COLOR,
            description=msg)
    elif arg == "pingeveryone":
        msg = "Mods only: Ping everyone currently in the House Cup." \
              "\n\n Example `%spingeveryone`" % prefix
        embed = discord.Embed(
            title="Ping Everyone Help",
            color=COLOR,
            description=msg)
    elif arg == "winnings":
        msg = "Mods only: Show the winners of this month's House Cup. " \
              "This will end and restart the competition. " \
              "This command should only be used at midnight UTC. " \
              "This command will be deleted after Stuffle codes timed announcements." \
              "\n\n Example `%swinnings`" % prefix
        embed = discord.Embed(
            title="Ping Everyone Help",
            color=COLOR,
            description=msg)

    # Fun Commands
    elif arg == "dumbledore":
        msg = "Try it and see. Example: `%sdumbledore`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nWritten and coded by The Amazing CHRain." % prefix
        embed = discord.Embed(
            title="Dumbledore Help",
            color=COLOR,
            description=msg)
    elif arg == "snape":
        msg = "Try it and see. Example: `%ssnape`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nWritten and coded by The Amazing CHRain." % prefix
        embed = discord.Embed(
            title="Snape Help",
            color=COLOR,
            description=msg)
    elif arg == "sneak":
        msg = "Try it and see. Example: `%ssneak`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nQuotes written by The Great Earth." % prefix
        embed = discord.Embed(
            title="Sneak Help",
            color=COLOR,
            description=msg)
    elif arg == "hermione":
        msg = "Try it and see. Example: `%shermione`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nQuotes written by Batsutousai." % prefix
        embed = discord.Embed(
            title="Hermione Help",
            color=COLOR,
            description=msg)
    elif arg == "ron":
        msg = "Try it and see. Example: `%sron`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nResponse written by Caty Pie." % prefix
        embed = discord.Embed(
            title="Ron Help",
            color=COLOR,
            description=msg)
    elif arg == "mcgonagall":
        msg = "Try it and see. Example: `%smcgonagall`\n" \
              "Don't worry though, the command is just for fun." \
              "\n\nQuotes written by Batsutousai." % prefix
        embed = discord.Embed(
            title="McGonagall Help",
            color=COLOR,
            description=msg)

    # Writing Commands
    elif arg == "prompt":
        msg = "Get a randomly generated prompt. Example: `%sprompt`" \
              "\n\nPrompt options written by RedHorse." % prefix
        embed = discord.Embed(
            title="Prompt Help",
            color=COLOR,
            description=msg)
    elif arg == "inspireme":
        msg = "Get some inspiration from stufflebot. Example: `%sinspireme`" \
              "\n\nResponses written by Caty, Dorea, and Stuffle." % prefix
        embed = discord.Embed(
            title="InspireMe Help",
            color=COLOR,
            description=msg)
    elif arg == "shouldikillharry":
        msg = "Have stufflebot decide if you should kill Harry. " \
              "Example: `%sshouldikillharry`"
        embed = discord.Embed(
            title="ShouldIKillHarry Help",
            color=COLOR,
            description=msg)

    elif embed is None:
        msg = "Sorry! This command is unrecognized. View the general help " \
              "for a list of commands with `%shelp`." % prefix
        embed = discord.Embed(
            title="Unrecognized Command",
            color=COLOR,
            description=msg)

    return embed


def general_help(prefix):
    msg = "Commands list. For help on a specific command, run " \
          "`%shelp COMMAND`.\n" \
          "Documentation on how the bot and competition work are " \
          "available [here](%s)." % (prefix, DOCS_LINK)

    embed = discord.Embed(
        title="StuffleBot Help",
        color=COLOR,
        description=msg)

    embed.add_field(
        name="Participating:",
        value="`join`, `leave`",
        inline=False)
    embed.add_field(
        name="Logging Points:",
        value="`daily`, `post`, `beta`, `art`, `comment`, `workshop`, `exercise`, `excred`, `wc` (total), `wc add`, `remove`",
        inline=False)
    embed.add_field(
        name="Viewing Points:",
        value="`points`, `standings`, `housepoints`, `leaderboard`",
        inline=False)
    embed.add_field(
        name="Mod Only Commands:",
        value="`award`, `deduct`, `pingeveryone`, `winnings`",
        inline=False)
    embed.add_field(
        name="Fun Commands:",
        value="`dumbledore`, `snape`, `mcgonagall`, `hermione`, `ron`, `sneak`",
        inline=False)
    embed.add_field(
        name="Inspiration Commands:",
        value="`prompt`, `inspireme`, `shouldikillharry`",
        inline=False)

    return embed

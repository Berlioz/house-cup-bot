import discord
import random
import asyncio
import apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
from calendar import monthrange
import datetime

from humor_commands import *


def get_random_embed_same_quote(quote, gif_and_caption, colour):
    """
    gif_and_caption is a list of tuples
    """
    gif, caption = random.sample(gif_and_caption, 1)[0]

    embed = discord.Embed(
        color=colour,
        description=quote)
    embed.set_image(url=gif)
    embed.set_footer(text="Gif Caption: " + caption)
    return embed


def get_mention(mentions, text, default="Harry Potter"):
    person_mention = default
    str_mentions = [m.mention for m in mentions]
    text_people = text.split(" ")[1:]

    if len(text_people) > len(mentions):
        person_mention = ", ".join(text_people)
    elif len(mentions) > 0:
        person_mention = ", ".join(str_mentions)
    return person_mention


def kidnap(kidnapper, mentions, text):
    """Inspiration and gif contributions from Dorea"""
    victim = get_mention(mentions, text, "Dorea")
    quote = "%s has kidnapped %s!!!" % (kidnapper, victim)
    gif_to_caption = [
        ("https://cdn.discordapp.com/attachments/539932855845781530/569529962034626610/weee_kidnap.gif",
            "Woman lets go of doorway as a man in a black mask pulls her away with the caption “Okay! Weeeeeeee!”"),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569548311523098654/cat_kidnap_gif.gif",
            "Two hands reach in from off screen and grab a calm, black cat. As it is pulled away, the cat is unruffled as it slides across a tile floor."),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569548870271369244/orange_cat_kidnapped.gif",
            "A person pulls with all their might to remove an orange cat from a room, but the cat successfully holds onto the doorway."),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569550008928698369/oh_no_kidnap.gif",
            "Two masked men grab a man who says, \"Oh no, I'm being kidnapped!\""),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569550813954048060/monster-kidnapping-girl.gif",
            "A woman is standing by a blue door with a small window when suddenly an arm breaks the window and drags her through.")
    ]
    return get_random_embed_same_quote(quote, gif_to_caption, 0)


def group_hug(hugger, mentions, text):
    """Inspiration and gif contributions from Caty Pi"""
    victim = get_mention(mentions, text, "Everyone")
    quote = "%s: you have been hugged by %s!" % (victim, hugger)
    gif_to_caption = [
        ("https://cdn.discordapp.com/attachments/565884495023177728/573523732652359686/image0.gif",
            "My Litttle Pony-Pinky Pie impossibly reaching off screen and pulling Twilight Sparkle, Fluttershy, Apple Jack, Rainbow Dash and Rarity into a hug."),
        ("https://cdn.discordapp.com/attachments/565884495023177728/573523907064233996/image0.gif",
            "1st shot-Five girls jump onto screen and hug (their teacher?)  2nd shot-Five girls hug a classmate  3rd shot-Two girls are hugged by five other students who all pile onto hug one by one"),
        ("https://cdn.discordapp.com/attachments/565884495023177728/573523944469168168/image0.gif",
            "The Simpsons-Homer Simpson being hugged by lots of children, including Rod and Tod, all eight of Apu’s children, Ralph Wiggum, and others. Another child, Üter, jumps on top of pile, hugging Homer’s face and squishing the other children."),
        ("https://cdn.discordapp.com/attachments/565884495023177728/573523959446765578/image0.gif",
            "Disney’s Aladdin-Genie hugging Aladdin and Jasmine when they run up to each other, then pulling in Abu, Aladdin’s monkey-in-crime, then the Sultan and Raja, who are Jasmine’s father and pet tiger respectively, and then the magic carpet, before squeezing and cuddling them all tightly."),
        ("https://media.discordapp.net/attachments/553382529521025037/588586381786480640/hug-Hy4hxRKtW.gif",
            "Korra, from Avatar, picks up the air bending family in a hug, then is nuzzled by a giant dog.")
    ]
    return get_random_embed_same_quote(quote, gif_to_caption, 15761808)


def hug(hugger, mentions, text):
    text_people = text.split(" ")[1:]
    if len(mentions) > 1 or len(text_people) > 1:
        return group_hug(hugger, mentions, text)
    victim = get_mention(mentions, text, "Friend")
    quote = "%s: you have been hugged by %s!" % (victim, hugger)
    gif_to_caption = [
        ("https://cdn.discordapp.com/attachments/592480821890514944/594587388219490331/f95e1e9bc953789b72d2a900cc00b9d75cd19fa3.gif",
            "A gray kitten with a white nose sinks onto its sibling, deepening their hug."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594476754140397568/image0.gif",
            "A monkey jumps into the waiting arms of its friend."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594475503302213632/image0.gif",
            "A human hand weaves its hand between a cat’s arms to rub its belly. The cat tightens its arms, drawing the human arm towards itself."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594475025575444490/image0.gif",
            "A guy embraces a lion, scratching its chin and resting his head on its."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594474506240655380/image0.gif",
            "A dog puts its arm around another dog. They shift onto their hind legs to fully embrace."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594474143848595456/image0.gif",
            "The rabbit from Zootopia peppily hugs the Fox, who sighs."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594472225428602882/image0.gif",
            "Two primates walk towards each other, then embrace in a deep hug."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594471466792255489/image0.gif",
            "A cat embraces a dog three times its size, standing so that they can rub their cheeks together. The dogs tail wags quickly."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594470674786025482/image0.gif",
            "Two dogs sit next to each other. The one on the left puts its arms around the other, patting its chest."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594469134193131521/image0.gif",
            "Two cats cuddle on a bed. The little spoon cat gets up and climbs atop the other, laying back down in an adorable embrace."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594468549779521536/image0.gif",
            "Two dogs sit happily side by side when one suddenly grabs the other in a tight hug."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594468330811817985/image0.gif",
            "A chicken walks into the waiting arms of a toddler, who embraces it fully."),
        ("https://thumbs.gfycat.com/EachAridBellfrog-size_restricted.gif",
            "A duck with drawn-on stick figure arms hugs a dog, rubbing its hand nub through the fur. Then, with its “hand” still on the dog, they walk away together."),
        ("https://cdn.discordapp.com/attachments/592480821890514944/594466674216927232/image0.gif",
            "A baby polar bear smiles as it rubs its face against an adult polar bear’s while hugging.")
    ]
    return get_random_embed_same_quote(quote, gif_to_caption, 15761808)


def pillage(person):
    """Inspiration and gif contributions from Dorea"""
    quote = "%s is on a pillaging spree!!!" % person
    gif_to_caption = [
        ("https://medievalkarl.files.wordpress.com/2015/02/7vh0ndg.gif",
            "A couple stand, peacefully framed by a stone window with vines. They scream when suddenly, the vikings charge."),
        ("https://www.eclectech.co.uk/b3ta/vikingbunny.gif",
            "A rabbit viking pillages a lawn by eating the grass."),
        ("https://66.media.tumblr.com/3ad6158c2bae0cf726539d6974ed6d5a/tumblr_o8s37xqzTF1tdy0nco1_500.gif",
            "Vikings cheer in front of a flaming wreckage."),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569555567685664775/viking_battlefield.gif",
            "Vikings fight on an open field."),
        ("https://cdn.discordapp.com/attachments/539932855845781530/569556428092866648/viking_woman_strikes.gif",
            "A viking woman strikes down a man in front of her ship.")
    ]
    return get_random_embed_same_quote(quote, gif_to_caption, 13632027)

from pyrogram import filters, Client
from Geez import cmds


def geez(command: str, prefixes: cmds):
    def wrapper(func):
        @Client.on_message(filters.command(command, prefixes) & filters.me)
        async def wrapped_func(client, message):
            await func(client, message)

        return wrapped_func

    return wrapper

from geezlibs.geez.autobot import *
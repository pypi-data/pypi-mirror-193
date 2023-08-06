import readline

def start():

    # This doesn't work
    readline.parse_and_bind('"\C-s": beginning-of-line')

    # This does work
    readline.insert_text("Hello")

# readline.set_startup_hook(start)
# try:
#     x = input("> ")
# finally:
#     readline.set_startup_hook()
# print(x)
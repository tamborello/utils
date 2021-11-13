# Whoopsie
# A Library to print & record error messages



import asyncio

# Synchronous
def whoopsie(msg=''):
    print(msg)
    with open('whoopsie.oops', 'a') as f:
        f.write(msg + '\n')

# Asynchronous
async def asWhoopsie(msg=''):
    print(msg)
    with open('whoopsie.oops', 'a') as f:
        f.write(msg + '\n')


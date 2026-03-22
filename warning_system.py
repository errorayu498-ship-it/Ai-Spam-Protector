warnings = {}

async def add_warning(member):

    user = member.id

    if user not in warnings:
        warnings[user] = 0

    warnings[user] += 1

    return warnings[user]

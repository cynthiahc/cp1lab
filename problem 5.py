def transfer_air(source, target, amount):
    old_bar = source.get_bar()

    source.release(amount)

    new_bar = source.get_bar()

    if old_bar - new_bar == amount:
        target.fill(amount)

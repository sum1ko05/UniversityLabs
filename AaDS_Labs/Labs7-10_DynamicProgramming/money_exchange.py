def exchange_money(nominals: list, total: int) -> int:
    data = [float('inf')] * (total + 1) # float('inf') - not defined yet
    data[0] = 0 # Init value

    for i in range(1, total + 1): # Calculating values for other totals
        for nominal in nominals:
            if nominal <= i: # Ignore if nominal is more than total - this can't be exchanged
                data[i] = min(data[i], data[i - nominal] + 1)

    return data[total] if data[total] != float('inf') else -1 # -1 - failed to exchange
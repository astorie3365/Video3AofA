def Inside_trader(G):
    n = len(G)
    actions = [] 
    holding = False
    buy_day = None

    for i in range(n - 1):
        if not holding and G[i] < G[i + 1]:
            # Buy if price is going up
            actions.append((i, 'buy', G[i]))
            holding = True
            buy_day = i
        elif holding and G[i] > G[i + 1]:
            # Sell if price is going down
            actions.append((i, 'sell', G[i]))
            holding = False
            buy_day = None

    # Final Stock Sale
    if holding:
        actions.append((n - 1, 'sell', G[-1]))

    return actions

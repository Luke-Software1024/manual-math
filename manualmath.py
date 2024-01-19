def manmult(victim, change):
    cv = victim
    for i in range(change):
        cv += victim
    return cv
def mansqu(victim):
    cv = victim
    cv += cv
    return cv
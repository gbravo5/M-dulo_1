def esDecimalPositivo(nb_str):
    try:
        nb = float(nb_str)
        if nb >= 0:
            return True
    except:
        return False

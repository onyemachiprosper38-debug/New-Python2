def temperature_advisory(temp, unit='C', threshold=30):

   
    if unit == 'C':
        converted = (temp * 9/5) + 32
    else:
        converted = (temp - 32) * 5/9

    if converted < threshold:
        return "Cold advisory"
    else:
        return "Heat alert"

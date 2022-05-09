rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

def rainy_month(rainfallData:str, maxRain:float) -> list:
    '''From rainfall data find if a month had more than `maxRain` inches of rain.'''
    moreRain=[]
    for num in rainfall_mi.split():
        rainfall= float(num.strip(','))
        if rainfall > maxRain:
            moreRain.append(rainfall)
    return moreRain

num_rainy_months = len(rainy_month(rainfall_mi, 3))
print(f"There was {num_rainy_months} very rainy months.")

"""conditionals practice"""


def get_weather_report() -> str:
    """display weather instructions"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a Jacket")
    elif weather == "hot":
        print("Keep Cool out their")
    else:
        print("I don't recognize this weather")
    return weather

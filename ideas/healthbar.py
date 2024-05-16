from colorama import Fore, Style, init

init(autoreset=True)

max_health = 100
current_health = 100
bars = 30

remaining_health_symbol = "▮"
lost_health_symbol = "⠿"

while True:
    remaining_health_bars = round(current_health / max_health * bars)
    lost_health_bars = bars - remaining_health_bars

    print(f"Health: {current_health}/{max_health}")
    remaining_health_colored = f"{Fore.GREEN}{remaining_health_symbol * remaining_health_bars}{Style.RESET_ALL}"
    lost_health_colored = (
        f"{Fore.RED}{lost_health_symbol * lost_health_bars}{Style.RESET_ALL}"
    )
    print(f"|{remaining_health_colored}{lost_health_colored}|")
    input("")
    current_health -= 5
    if current_health < 0:
        current_health = 0

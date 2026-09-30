food = str(input("Введите категорию: ")).strip().lower()

match food: 
    case "напиток": 
        print(f"Чай", "Кофе", "Сок")
    case "суп": 
        print(f"Борщ", "Щи", "Cуп-пюре")
    case "десерт":
        print(f"Торт", "Мороженое", "Фрукты")
    case _:
        print(f"Данной категории нет")
        exit()

dish = input("Введите название блюда: ").strip().lower()


match dish:
    case "чай":
        print(f"Цена '{dish}': 100 рублей.")
    case "кофе":
        print(f"Цена '{dish}': 150 рублей.")
    case "сок":
        print(f"Цена '{dish}': 120 рублей.")
    case "борщ":
        print(f"Цена '{dish}': 250 рублей.")
    case "щи":
        print(f"Цена '{dish}': 200 рублей.")
    case "суп-пюре":
        print(f"Цена '{dish}': 230 рублей.")  
    case "торт":
        print(f"Цена '{dish}': 180 рублей.")
    case "мороженое":
        print(f"Цена '{dish}': 130 рублей.")
    case "фрукты":
        print(f"Цена '{dish}': 160 рублей.")
    case _:
        print("К сожалению, этого блюда нет в прайс-листе.")
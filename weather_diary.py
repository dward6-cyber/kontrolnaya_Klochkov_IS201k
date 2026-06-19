import json
import os
from datetime import datetime, timedelta

FILE_NAME = 'weather.json'

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            print("Ошибка чтения файла. Создаю новый дневник.")
            return []
    return []

def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_record():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    
    try:
        temperature = float(input("Введите температуру: "))
    except ValueError:
        print("Ошибочка!). Температура должна быть числом!)")
        return
    
    description = input("Введите описание погоды: ").strip()
    if not description:
        print("Ошибочка!). Описание погоды не может быть пустым!")
        return
    
    data.append({
        "date": today,
        "temperature": temperature,
        "description": description
    })
    
    save_data(data)
    print("Запись добавлена!")

def show_all():
    data = load_data()
    
    if not data:
        print("Записей пока нет.")
        return
    
    print("\n=== Все записи ===")
    for record in data:
        print(f"{record['date']} | {record['temperature']}°C | {record['description']}")

def show_last_week():
    data = load_data()
    if not data:
        print("Записей пока нет.")
        return
    
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    
    print(f"\n=== Записи за неделю ({week_ago.strftime('%d.%m')} - {today.strftime('%d.%m')}) ===")
    
    found = False
    for record in data:
        record_date = datetime.strptime(record["date"], "%Y-%m-%d")
        if week_ago <= record_date <= today:
            print(f"{record['date']} | {record['temperature']}°C | {record['description']}")
            found = True
    
    if not found:
        print("За последнюю неделю записей нет.")

def show_menu():
    while True:
        print("\n=== Дневник погоды ===")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Показать записи за неделю")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_record()
        elif choice == '2':
            show_all()
        elif choice == '3':
            show_last_week()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == '__main__':
    show_menu()
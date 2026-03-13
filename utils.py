import pandas as pd

def add_new_transaction(filepath):
    print("\n--- Добавление новой записи ---")
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    description = input("Описание: ")
    
    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Ошибка: Сумма должна быть числом!")
        return

    new_row = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
    
    new_row.to_csv(filepath, mode='a', header=False, index=False, lineterminator='\n')
    print("Запись успешно добавлена!")
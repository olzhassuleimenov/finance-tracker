import processor
import classifier
import utils

def main():
    filename = 'data.csv'
    config = 'categories.json'

    df = processor.load_and_clean_data(filename)
    rules = classifier.open_json(config)

    if not df.empty:
        df['Category'] = df['Description'].apply(lambda x: classifier.transaction(rules, x))
    
    while True:
        print("\n=== FINANCE TRACKER ===")
        print("1. Показать траты по категориям")
        print("2. Показать все транзакции")
        print("3. Добавить запись")
        print("4. Выйти")
        
        choice = input("Выберите действие: ")

        if choice == '1':
            if df.empty:
                print("Данных пока нет.")
            else:
                report = df.groupby('Category')['Amount'].sum()
                print("\nСумма по категориям:")
                print(report)
        
        elif choice == '2':
            print("\n", df)
            
        elif choice == '3':
            utils.add_new_transaction(filename)
            df = processor.load_and_clean_data(filename)
            df['Category'] = df['Description'].apply(lambda x: classifier.transaction(rules, x))
            
        elif choice == '4':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()
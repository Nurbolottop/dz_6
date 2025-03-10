def main():
    todo_list = []
    print("Введите свои дела (нажмите Enter без ввода для завершения):")
    
    while True:
        task = input("- ")
        if task == "":
            break
        todo_list.append(task)
    
    print("\nВаш список дел:")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

if __name__ == "__main__":
    main()

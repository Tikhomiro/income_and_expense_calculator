import json


#В этом классе мы будем обращаться к json используя контекстный менеджер 
class WorkWithJson:


    def get_json() -> dict:
        try:
            with open('db.json') as f:
                templates = json.load(f)

            return templates
        except:
            print(f"Что то пошло не так с получением информации из json")


    def add_to_json(date: str, category: str, sum: float, desctiption: str):
        try:
            json_data = {
                "date" : date,
                "category" : category,
                "sum" : sum,
                "description" : desctiption
            }
            data = json.load(open("db.json"))
            data.append(json_data)
            with open("db.json", "w") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Произошла ошибка с добавлением новой записи, {e}")



#В этом классе прописаны все основные функции для работы с пользователем
class WordToUser:


    def out_balance() -> str:
        expenses = 0
        income = 0
        balance = 0
        lis = WorkWithJson.get_json()
        for value in lis:
            if value['category'] == 'Расходы':
                expenses += value['sum']
            else: 
                income += value['sum']
        
        balance = income - expenses
        return print(f"Ваш баланс состовляет {balance}, суммарные доходы {income}, суммарные расходы {expenses}")

    
    def join_new_entry() -> None:
        try:
            date = str(input("Введите дату: "))
            category = str(input("Выберете категорию 1 : Доходы, 2 : Расходы "))
            if category == "1":
                category = "Доходы"
            else:
                category = "Расходы"
            sum = float(input("Введите сумму: "))
            description = str(input("Напишите описание: "))
            WorkWithJson.add_to_json(date, category, sum, description)
        except:
            print("Вы что то ввели не так")


    def change_entry() -> None:
        lis = WorkWithJson.get_json()
        for i in range(len(lis)):
            print(f"Номер записи {i+1}, дата {lis[i]['date']}, категория {lis[i]['category']}, сумма {lis[i]['sum']}, описание {lis[i]['description']}")

        try:
            num = int(input("Введите номер записи, которую хотите изменить: ")) - 1
            lis[num]['sum'] = int(input("На какую сумму вы меняете: "))
            update = json.dumps(lis)
            with open("db.json", "w") as json_file:
                json_file.write(update)
        except IndexError:
            print("Вы ввели не то число")
        else:
            print("Что то пошло не так")


    def find() -> None:
        lis = WorkWithJson.get_json()
        how = int(input("Как мы будем искать:\n1 : Категория\n2 : Дата\n3 : Сумма\n"))
        if how == 1:
            categ = str(input("Введите категорию: "))
            for value in lis:
                if value['category'] == categ:
                    print(f"Дата {value['date']}, категория {value['category']}, сумма {value['sum']}, описание {value['description']}")
        if how == 2:
            date = str(input("Введите дату: "))
            for value in lis:
                if value['date'] == date:
                    print(f"Дата {value['date']}, категория {value['category']}, сумма {value['sum']}, описание {value['description']}")
        if how == 3:
            sum = int(input("Введите сумму: "))
            for value in lis:
                if value['sum'] == sum:
                    print(f"Дата {value['date']}, категория {value['category']}, сумма {value['sum']}, описание {value['description']}")
    

#Этот класс сделан для обращения с user и выполнением функций класса WordToUser
class Interface:


    def __init__(self):
        while True:
            func_num = int(input("Введите номер функции\n1 : Вывод баланса\n2 : Добавление записи\n3 : Редактирование записи\n4 : Поиск по записям\n5 : Выйти из программы\n"))
            if func_num == 1: WordToUser.out_balance()
            if func_num == 2: WordToUser.join_new()
            if func_num == 3: WordToUser.change_entry()
            if func_num == 4: WordToUser.find()
            if func_num == 5: break




clas = Interface()
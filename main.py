name = input("Ведеите свое имя")        #Начало
print("Здравствуйте," , name )          #Приветствие

while True:

    act = input("Выберите действие: (+,-,*,/,): ")      #Действия калькулятора
    if act in ('+', '-', '*', '/' ):                    #Знаки действий
        number1 =float(input("x= "))                    #Переменная один
        number2 = float(input("y= "))                   #Переменная вторая
        if act == '+':                                  #действие сложение
            print("Ответ:", (number1 + number2))        #Результат
        elif act == '-':                                #действие вычитание
            print("Ответ:", (number1 - number2))        #Результат
        elif act == '*':                                #действие уиножение
            print("Ответ:", (number1 * number2))        #Результат
        elif act == '/':                                #действие деление
                print("Ответ:", (number1 / number2))    #Результат

1.	Вы работаете над модулем внутрикорпоративной системы учета данных сотрудников компании.  

**_Программа должна:_**  
•	Найти сотрудника с минимальным возрастом;  
•	Вычислить медианный возраст всех сотрудников.  
•	Найти сотрудника с максимальным возрастом.  

Медиана — число, которое находится в середине этого набора, если его упорядочить по возрастанию. Если набор чисел четный, то берется среднее между двумя средними числами и округляется до целого.  

**Формат ввода:**  
Первая строка содержит данные сотрудников. Данные включают имя, возраст и отдел, разделенные запятой, без пробелов. Информация о каждом сотруднике отделена от других через точку с запятой. Количество сотрудников — от 2 до 100.

**Формат вывода:**  
Вторая строка содержит три целых числа, разделенные пробелом: минимальный возраст, медианный возраст и максимальный возраст.  

**Пример 1:**  
- _Входные данные:_  
Иван,28,Инженер;Олег,34,HR;Денис,45,Маркетинг;Анна,30,Инженер;Борис,24,HR  
- _Выходные данные:_  
24 30 45  

**Пример 2:**  
- _Входные данные:_  
Павел,28,Инженер;Елена,34,Маркетинг  
- _Выходные данные:_   
28 31 34

**Макет кода:**
``` 
def process_employee_data(input_string: str) -> str:  
    """Ваш код"""

input_data = input()  
output_data = process_employee_data(input_data)  
print(output_data)
```

2. Вы работаете над системой управления продуктами в магазине. Вам нужно обработать данные о продуктах, их категориях и ценах, и вывести список категорий продуктов, отсортированный в алфавитном порядке, а затем, внутри каждой категории — список продуктов по возрастанию цены. Если цена совпадает, сортировка выполняется в алфавитном порядке.  

**Формат ввода:**  
Каждая строка содержит название продукта, категорию и цену, разделенные запятыми, без пробелов. Всего продуктов в списке не больше 100.   

**Формат вывода:**  
Список категорий и продуктов. Сначала называется категория, затем через двоеточие — товары в этой категории, отсортированные по цене. Вывод построчный: на одну строку приходится одна категория или товар. Если цена совпадает у нескольких товаров, расположите их относительно друг друга в алфавитном порядке. Выводите цены с одной цифрой после точки (в том числе целые числа, например, «‎10.0»).   

**Пример 1**  
-_Входные данные:_  
Яблоко,Фрукты,225 Банан,Фрукты,500 Морковь,Овощи,100 Брокколи,Овощи,200 Курица,Мясо,1200 Говядина,Мясо,2000  

-_Выходные данные:_  
Мясо: Курица,1200.0 Говядина,2000.0 Овощи: Морковь,100.0 Брокколи,200.0 Фрукты: Яблоко,225.0 Банан,500.0

**Макет функции:**
```
def sort_products(input_strings):
   """Ваш код"""

lines = []  
while True:  
   try:  
      line = input()  
      if line == "":  
         break  
   except EOFError:  
      break  
   lines.append(line)  

for string in sort_products(lines):  
   print(string)
```

3. Вы разрабатываете программу для анализа временного ряда цен акций. Вам нужно написать программу, которая позволит выявлять максимальные значения на определенном временном промежутке, то есть выводить максимальные значения среди пройденных элементов на каждом шаге.  

**Формат ввода**  
Одна строка, в которой чередуются целые числа, разделенные пробелами. Длина списка — не больше 100 элементов.  

**Формат вывода**  
Одна строка, в которой чередуются целые числа, разделенные пробелами. В строке содержатся максимальные значения среди пройденных элементов на каждом шаге.

**Пример 1**
- _Входные данные:_  
1 3 2 5 4  
- _Выходные данные:_  
1 3 3 5 5  

**Пример 2**  
- _Входные данные:_  
7 1 5 3 6 4  
- _Выходные данные:_  
7 7 7 7 7 7  

**Пример 3**  
- _Входные данные:_  
10 20 15 25 30 5  
- _Выходные данные:_  
10 20 20 25 30 30  

**Пример 4**  
- _Входные данные:_  
5 5 5 5 5  
- _Выходные данные:_  
5 5 5 5 5  

``` 
def solve(input_string: str) -> str:  
    """Ваш код"""  

input_string = input()  
result = solve(input_string)  
print(result)
```

4. **Поиск почтовых адресов**    
Вы разрабатываете модуль для обработки текстовых данных. Вам необходимо извлечь из текста список всех уникальных email-адресов. 

**Email-адрес считается допустимым, если он:** 
- Содержит только латинские буквы (в любом регистре), цифры, символы «.», «-» и «_»;
Начинается с буквы или цифры;
- Содержит один символ «@»;
- Завершается одним из следующих способов: .ru, .com, .org или .net

**Формат ввода:**  
Одна строка текста произвольной длины до 1000 символов.  

**Формат вывода:**  
Если найдены email-адреса, каждый найденный адрес выводится на отдельной строке. Если адресов не найдено, выводится «‎Не найдено».  

**Пример 1**  
•	_Входные данные_:  
Это текст с email user123@example.com и user456@mail.ru, но не example.com

•	_Выходные данные:_  
user123@example.com user456@mail.ru  

**Пример 2**  
•	_Входные данные:_  
Это пример текста с невалидными адресами: user@, @domain.com

•	_Выходные данные:_  
Не найдено

**Макет решения:**
```
import re  
class TextProcessor:    
    def __init__(self, text):    
        self.text = text

    def extract_emails(self):
        """Ваш код"""
        pass

input_text = input()
"""Ваш код"""
``` 

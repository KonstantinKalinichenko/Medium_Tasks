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
-_Входные данные:_  
Иван,28,Инженер;Олег,34,HR;Денис,45,Маркетинг;Анна,30,Инженер;Борис,24,HR  
-_Выходные данные:_  
24 30 45  

**Пример 2:**  
_Входные данные:_  
Павел,28,Инженер;Елена,34,Маркетинг  
_Выходные данные:_   
28 31 34

**Макет кода:**  
`def process_employee_data(input_string: str) -> str:  
    """Ваш код"""

input_data = input()  
output_data = process_employee_data(input_data)  
print(output_data)`

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

`def sort_products(input_strings):
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
   print(string)`

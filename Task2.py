def sort_products(input_strings) -> list:


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

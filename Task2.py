from collections import defaultdict


def sort_products(input_strings) -> list:
    splitted = input_strings[0].split()
    products = [item.split(',') for item in splitted]
    dict_products  = defaultdict(list)
    for product in products:
        dict_products[product[1]].append([product[0],
                                          str(float(product[2]))])
    sorted_products = dict(sorted(dict_products.items()))
    for category in sorted_products:
        sorted_products[category] = sorted(
            sorted_products[category],
            key=lambda x: (x[1], x[0])
        )
    print(sorted_products)


lines = []
while True:
   try:
      line = input()
      if line == "":
         break
   except EOFError:
      break
   lines.append(line)

print(sort_products(lines))
# for string in sort_products(lines):
#    print(string)

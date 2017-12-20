# any.py
# Reference: w_pacb43.pdf, page 89

items = [0, None, 0.0, True, 0, 7]
#items = [0, None, 0.0, False, 0, not 7]
found = False
for item in items:
    print('scanning item', item)
    if item:
        # print("DEBUG: item", item, "evaluates to True")
        found = True
        break

if found:
    print('At least one item evaluates to True')
else:
    print('All items evaluate to false')

# print("items=", items)
# x = any(items)
# print("DEBUG: x=", x)

# EOF

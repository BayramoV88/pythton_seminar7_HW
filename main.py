import sys
from init_pb import init_pb
from menu import menu
from add_contact import add_contact
from search import search

print('Добро пожаловать!')
print('')
ch = menu()
pb = init_pb()
while ch in (1, 2, 9):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = search(pb)
    elif ch == 9:
        sys.exit('До скорых встреч!')
from colorama import Fore, Back, Style

print ('Texto normal')
print (Fore.BLUE + 'Texto em azul')
print (Back.BLUE + Fore.WHITE + 'Texto em branco com fundo azul')
print (Style.RESET_ALL + 'Texto normal')
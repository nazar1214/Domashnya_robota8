from colorama import Fore, Back, Style

print(Fore.RED +"зміна коліру текста")  # сам смисли colorama зміну коліру тексту 
print(Back.GREEN + 'задній фон')
print(Style.RESET_ALL) #щоб видалити всі еффекти від colorama
print("перевірка")
print(Style.BRIGHT +"щоб текст був підзвічений")
print(f"{Fore.RED}можна ще зробити таким способом{Style.RESET_ALL}") # шоб після зроблоного не було пустого пропуска
print("перевірка")


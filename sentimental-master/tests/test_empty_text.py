from sentimental import Sentimental
from googletrans import Translator
sent = Sentimental()
translator = Translator()
sentence = input("Введите ваш комментарий: ")
result1 = translator.translate(sentence, src='ru', dest='en')
result = sent.analyze(result1.text)
x = result.get('score')
if x > 5: print("Комментарий слишком положительный")
if x == 5: print("Комментарий положительный на - 100%\n"
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░██100%██▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 '░████████▒░░\n'
                 )
if x == 4: print("Комментарий положительный на - 80%\n"
                 '░░░░░░░░░░░░\n'
                 '░░▒▒▒▒▒▒▒▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░██80%██▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 )
if x == 3: print("Комментарий положительный на - 60%\n"
                 '░░░░░░░░░░░░\n'
                 '░░░░░░░░░░░░\n'
                 '░░░░░░░░░░░░\n'
                 '░░▒▒▒▒▒▒▒▒░░\n'
                 '░░██60%██▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 '░░███████▒░░\n'
                 )
if x == 2: print("Комментарий положительный на - 40%\n"
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░40%░░░░\n'
                 '░░▒▒▒▒▒▒▒░░\n'
                 '░░██████▒░░\n'
                 '░░██████▒░░\n'
                 '░░██████▒░░\n'
                 '░░██████▒░░\n'
                 )
if x == 1: print("Комментарий положительный на - 20%\n"
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░20%░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░░░░░░░░░░\n'
                 '░░▒▒▒▒▒▒▒░░\n'
                 '░░██████▒░░\n'
                 '░░██████▒░░\n'
                 )
if x == 0: print("Комментарий нейтрален\n"
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒0%▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 '▒▒▒▒▒▒▒▒▒▒\n'
                 )
if x == -1: print("Комментарий отрицательный на - 20%\n"
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░20%░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░▒▒▒▒▒▒▒░░\n'
                  '░░██████▒░░\n'
                  '░░██████▒░░\n'
                  )
if x == -2: print("Комментарий отрицательный на - 40%\n"
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░░░░░░░░\n'
                  '░░░░40%░░░░\n'
                  '░░▒▒▒▒▒▒▒░░\n'
                  '░░██████▒░░\n'
                  '░░██████▒░░\n'
                  '░░██████▒░░\n'
                  '░░██████▒░░\n'
                  )
if x == -3: print("Комментарий отрицательный на - 60%\n"
                  '░░░░░░░░░░░░\n'
                  '░░░░░░░░░░░░\n'
                  '░░░░░░░░░░░░\n'
                  '░░▒▒▒▒▒▒▒▒░░\n'
                  '░░██60%██▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  )
if x == -4: print("Комментарий отрицательный на - 80%\n"
                  '░░░░░░░░░░░░\n'
                  '░░▒▒▒▒▒▒▒▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░██80%██▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  '░░███████▒░░\n'
                  )
if x == -5: print("Комментарий отрицательный на - 100%\n"
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░██100%██▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  '░████████▒░░\n'
                  )
if x < -5: print("Комментарий слишком отрицательный")
timeout = input("")
#print(result1.text)
#print(result)
#print(x)
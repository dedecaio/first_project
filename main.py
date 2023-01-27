import time

import pyautogui
import pyperclip

# time.sleep(3)
# print(pg.position())

functions = '''
    trolar zap \r
    etc
'''
print(functions)

question1 = input('O que desejas fazer? ')
msg = input("Qual a mensagem que desejas passar? ")
howmuch = int(input("Quantas vezes deseja mandar a mensagem? ")) or None


def troll_zap():
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyperclip.copy('chrome.exe')
    app = pyperclip.paste()
    pyautogui.write(app)
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(579, 473)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(192, 294)
    pyautogui.click()


def write(msg):
    pyperclip.copy(msg)
    mensagem = pyperclip.paste()
    pyautogui.write(mensagem)


if question1 == 'trolar zap' and howmuch:
    print('Ok, processando...')
    troll_zap()
    time.sleep(1)

    for i in range(howmuch):
        write(msg)
        pyautogui.press('enter')

    print('Processo realizado com sucesso, desde já obrigado e volte sempre')
else:
    print('Error ', 'Função inexistente, favor utilizar somente as citadas \
          acima')

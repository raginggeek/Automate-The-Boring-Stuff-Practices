import pyautogui

print(pyautogui.position())
pyautogui.moveTo(10, 1900, duration=1.5)
pyautogui.click(10, 1900)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('n')
pyautogui.press('o')
pyautogui.press('t')
pyautogui.press('e')
pyautogui.press('p')
pyautogui.press('a')
pyautogui.press('d')
pyautogui.press('enter')
pyautogui.typewrite('I have control of your system, fully automated control!!!!', interval=.2)
pyautogui.hotkey('alt', 'f')
pyautogui.press('x')
pyautogui.press('n')

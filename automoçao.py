import pyautogui as pag
import time
import pandas as pd
pag.PAUSE = 1
pag.press('win')
pag.write('google chrome')
pag.press('enter')
pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.press('enter')
time.sleep(2)
pag.press('tab')
pag.write('emailficticio@gmail.com')
pag.press('tab')
pag.write('senhaficticia')
pag.press('enter')
time.sleep(2)
linha = pd.read_csv('produtos.csv')
for i in linha.index:
    pag.click(x=836, y=261)
    pag.write(str(linha.loc[i, 'codigo']))
    pag.press('tab')
    pag.write(str(linha.loc[i, 'marca']))
    pag.press('tab')
    pag.write(str(linha.loc[i, 'tipo']))
    pag.press('tab')
    pag.write(str(linha.loc[i, 'categoria']))
    pag.press('tab')
    pag.write(str(linha.loc[i, 'preco_unitario']))
    pag.press('tab')
    pag.write(str(linha.loc[i, 'custo']))
    pag.press('tab')
    obs = str(linha.loc[i, 'obs'])
    if obs != 'nan':
        pag.write(obs)
    pag.press('enter')
    pag.scroll(50000)
    
# Passo a passo do projeto
# Passo 1: entrar no site da empresa 
# Passo 2: fazer login
# Passo 3: importar dados 
# Passo 4: cadastrar os produtos
# Passo 5: Repetir o passo 4 ate cadastrar todos os produtos 

import pyautogui
import time

# Comando do pyautogui
# pyautogui.click - clicar com o mouse TELG000524   
# pyautogui.press - pressionar um tecla
# pyautogui.hotkey - combinação de teclas (ctrl c)
# pyautogui.scroll - rolar a tela para cima ou para baixo 
# pyautogui.pause - configuração de pause para cada comando 
# pyautogui.position - posicao da tela para dar o click

pyautogui.PAUSE = 0.3

# Passo 1: entrar no site da empresa 
# abri o navegador  
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

# escrever o site da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep (3)

#passo 2: fazer login 
pyautogui.click(x=827, y=412)
pyautogui.hotkey("ctrl", "a")
pyautogui.write ("viniciussouza@gmail.com")

#colocar senha
pyautogui.press ("tab")
pyautogui.write ("minhasenha")

pyautogui.click (x=956, y=573)

time.sleep(3) 

#passo 3: importar dados 
import pandas

tabela = pandas.read_csv ("produtos.csv")

print (tabela)

#Passo 4: cadastrar produtos
for linha in tabela.index:
    #codigo
    pyautogui.click (x=760, y=291)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preco_unitario
    preco= str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.press(obs)

    #clicar no botar de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")  

    pyautogui.scroll(1000)

# Passo 5: repetir o passo 4 para cadastrar todos os produtos     
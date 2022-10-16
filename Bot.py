from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date, datetime

navegador = webdriver.Chrome()
navegador.get('https://coinmarketcap.com/pt-br/')

sleep(5)
#fechando mensagem de cookies
navegador.find_element(By.XPATH, '//*[@id="cmc-cookie-policy-banner"]/div[2]').click()

#capturando o valor do dolar atual
navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[3]/td[3]/div/a/div/div/p').click()
usdt = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
print(usdt)

sleep(3)
#capturando o valor do bitcoin
navegador.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
btc = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
print(btc)

sleep(3)
#capturando o valor do etherum
navegador.get('https://coinmarketcap.com/pt-br/currencies/ethereum/')
eth = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
print(eth)

#pegando a data atual
data_atual = datetime.now()
data_string = data_atual.strftime('%d / %m / %Y às %H:%M')
print(data_string)

#Criando Relatorio
with open('Relatorio.txt', 'w') as arquivo:
    arquivo.write(f'# Cotacao em: {data_string} \n')
    arquivo.write('\n')
    arquivo.write('Dolar: ' + usdt + '\n')
    arquivo.write('Bitcoin: ' + btc + '\n')
    arquivo.write('Etherum: ' + eth + '\n')







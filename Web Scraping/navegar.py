
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')

#Buscar na barra de pesquisa e escrever relogio e clicar 
write = navegador.find_element(By.NAME,'q').send_keys('relogio masculino' + Keys.RETURN)



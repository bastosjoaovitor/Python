from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

try:
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://feiradecienciaseducacaofinanceira.my.canva.site/apresentacao')
    sleep(5)
    print('\n\033[32mO site está disponivel.\033[m\n')
except:
    print('\n\033[31mO site não está disponivel.\033[m\n')
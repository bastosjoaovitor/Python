import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://feiradecienciaseducacaofinanceira.my.canva.site/apresentacao')
except:
    print('\n\033[31mO site não está disponivel.\033[m\n')
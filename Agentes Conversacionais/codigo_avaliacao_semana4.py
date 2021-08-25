#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-
"""
WhatsApp Web Bot
@author: Lucas Oliveira
"""
# Importar bibliotecas
import time
import random
from selenium import webdriver #Automatizador de acesso ao navegador
from webdriver_manager.chrome import ChromeDriverManager #Driver específico do Chrome
from selenium.webdriver.common.keys import Keys #Quando precisamos simular alguma tecla especial

# Navegar até WhatsApp Web
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Acessando o WhatsApp Web...")
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
print("Escaneie o QR Code, e então pressione ENTER")
input()

while True:  
    print("Buscando novas mensagens...")
    time.sleep(2)
    
    try:
        # Todos contatos que estão sinalizados com novas mensagens tem o atributo aria-label
        # Aqui buscamos todos eles
        contatos = driver.find_elements_by_css_selector("span[aria-label]")
        
        # Percorre contatos com novas mensagens
        for contato in contatos:
            
            # Clica no contato para que possamos acessar o campo de mensagem
            contato.click()
            
            
            
            todasMensagens = driver.find_elements_by_css_selector(".copyable-text")            
            ultimaMensagem = todasMensagens[-2]     #[ len(todasMensagens) - 2 ]
            print('Mensagem do usuário: ', ultimaMensagem.text)
            
            
            ## CÓDIGO ##
            
            
            resposta = funcao(ultimaMensagem.text)  # função customizável     
 
            ####

            campoMensagem = driver.find_elements_by_css_selector("div[contenteditable='true']")[1]
            campoMensagem.click()
            time.sleep(2)
            campoMensagem.send_keys(resposta) # texto resposta para o bot
            time.sleep(2)
            campoMensagem.send_keys(Keys.ENTER)

    except:
        print("Sem mensagens novas...")
        # Coloca um timer para continuar depois de X segundos
        time.sleep(5)
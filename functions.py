from webdriver import Robo
import time

def totalUnidades():
    totalDeElementosLista = Robo.driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__item").length')

    # remove os itens não necessários da lista

    listaDeUnidades = totalDeElementosLista - 10 

    return listaDeUnidades

def iniciaBuscas():
        total = totalUnidades()

        for i in range(1, total):

                # abre o menu dropdown
        
                openMenu()
                time.sleep(10)
                
                # busca o primeiro elemento da lista e clica para carregar
                buscaUnidade(i)
                time.sleep(10)

                # pega a url atual e adiciona a extensão necessária do settings
                Robo.driver.get(openSettings())
                time.sleep(10)
                
                nomeUnidade = getNomeUnidade()

                # pega a url atual e adiciona a extensão necessária para abrir as configs da lan
                Robo.driver.get(openWlans())
                time.sleep(10)

                # Verifica quantidade de elementos da tabela de ssid's para tomar ação

                txt = open("senhas.txt","a+")
                txt.write("Unidade: " + nomeUnidade + "\n" + "\n") 
                txt.close()

                # verifica se existe a rede tablet e bike 
                capturaSSidPass()

                txt = open("senhas.txt","a+")
                txt.write("----------------------------------------------------------------------------------"+ "\n" + "\n") 
                txt.close()

def main():
        Robo.driver.get('xxxxxxxxx') # site a ser adicionado
        time.sleep(5) # Esperar o site ser carregado
        search_box = Robo.driver.find_element_by_name('username')
        search_box.send_keys('xxxxxxx') # seu usuário para login
        search_box = Robo.driver.find_element_by_name('password')
        search_box.send_keys('xxxxxxx') # sua senha para login
        search_box.submit()
        time.sleep(10)    

def openSettings():
    url = Robo.driver.current_url
    ir = url[:60]
    config = ir + '/settings/site'
    return config

def openWlans():
    url = Robo.driver.current_url
    ir = url[:60]
    config = ir + '/settings/wlans'
    return config

def openMenu():
    elemento = Robo.driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__arrow icon ubnt-icon--pointer-down")')[0]
    elemento.click()

def reiniciaUnidades():
    entra = Robo.driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__item").item(1)')
    entra.click()

def buscaUnidade(i):
    entra = Robo.driver.execute_script(f'return document.getElementsByClassName("appOrgSwitcher__item").item([{i}])')
    entra.click()
  
def getNomeUnidade():
    site_unidade = Robo.driver.execute_script('return document.getElementsByName("siteName").item(0).value')
    return site_unidade

def totalLans():
    verificaQtdSSid = Robo.driver.execute_script('return document.getElementsByClassName("wlanName").length')
    return verificaQtdSSid

def voltar():
    voltar = Robo.driver.find_element_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/div/div/button[2]')
    voltar.click()    

def ssidPassword():
    ssid = Robo.driver.execute_script('return document.getElementsByName("wirelessNetworkName").item(0).value')
    senha = Robo.driver.execute_script('return document.getElementsByName("wirelessNetworkWpaPskKey").item(0).value')
    return ssid, senha

def capturaSSidPass():
        result = totalLans()
        for i in range (1, result):
                rede1 = Robo.driver.find_elements_by_xpath(f'//*[@id="wirelessNetworksTable"]/tbody/tr[{i}]/td[5]/button[1]')[0]
                rede1.click()
                time.sleep(10)

                ssid, password = ssidPassword()

                time.sleep(10)
                        
                voltar()
                time.sleep(10)
            
                txt = open("senhas.txt","a+")
                txt.write("SSID: " + ssid + " Senha: " + password + "\n" + "\n") 
                txt.close()

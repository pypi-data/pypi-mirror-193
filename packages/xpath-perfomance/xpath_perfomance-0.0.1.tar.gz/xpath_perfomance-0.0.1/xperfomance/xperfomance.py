import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

#NOTE - Xperfomance Class
class Xpath_Perfomance:
    def __init__(self):
        self.driver = webdriver.Chrome(service=servico)
        self.tentar = Tentar(max_tentativas=3, intervalo=1)
        
    def executar_metodo(self, metodo, xpath, *args, **kwargs):
        while True:
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                metodo = getattr(element, metodo)
    
                return metodo(*args, **kwargs)
                
            except NoSuchElementException:
                time.sleep(0.01)

    def click(self, xpath, use_tentar=False):
        if use_tentar:
            self.tentar.run(self.executar_metodo, 'click', xpath)
        else:
            self.executar_metodo('click', xpath)

    def enviar_texto(self, xpath, text, use_tentar=False):
        
        if use_tentar:
            self.tentar.run(self.executar_metodo, 'send_keys', xpath, text)
        else: 
            self.executar_metodo('send_keys', xpath, text)
        
    def pressionar_tecla(self, xpath, tecla, use_tentar=False):
        tecla = getattr(Keys, tecla)
        
        if use_tentar:
            self.tentar.run(self.executar_metodo, 'send_keys', xpath, tecla)
        else:
            self.executar_metodo('send_keys', xpath, tecla)
        
    def mouse_em_cima(self, xpath, use_tentar=False):
        if use_tentar:
            self.tentar.run(self.executar_metodo, 'move_to_element', xpath)
        else:    
            self.executar_metodo('move_to_element', xpath)
            
    def click_direito(self, xpath, use_tentar=False):
        elemento = self.driver.find_element(By.XPATH, xpath)
        acao = ActionChains(self.driver)
        
        if use_tentar:
            self.tentar.run(acao.move_to_element(elemento).context_click().perform())
        else:
            while True:
                try:
                    acao.move_to_element(elemento).context_click().perform()
                    break
                except NoSuchElementException:
                    time.sleep(0.01)

    def selecionar_texto(self, xpath, use_tentar=False):
        element = self.driver.find_element(By.XPATH, xpath)
        action = ActionChains(self.driver)
        
        if use_tentar:
            self.tentar.run(action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform())
        else:
            while True:
                try:    
                    texto_selecionado = action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    return texto_selecionado
                
                except NoSuchElementException:
                    time.sleep(0.01)
        
    def click_duplo(self, xpath, use_tentar=False):
        element = self.driver.find_element(By.XPATH, xpath)
        action = ActionChains(self.driver)
    
        if use_tentar:
            self.tentar.run(action.double_click(element).perform)
        else:
            while True:
                try:
                    action.double_click(element).perform()
                    break
                except NoSuchElementException:
                    time.sleep(0.01)
                    
    def aba_indice(self, indice):
        self.driver.window_handles[indice]
        
    def trocar_aba(self, indice):
        self.driver.switch_to.window(self.aba_indice(indice))
        
    def maximar_janela(self):
        self.driver.maximize_window()
    
    def abrir_site(self, url):
        self.driver.get(url)



class Tentar:
    def __init__(self, max_tentativas=3, intervalo=1):
        self.max_tentativas = max_tentativas
        self.intervalo = intervalo
    
    def run(self, func, *args, **kwargs):
        for tentativa in range(1, self.max_tentativas + 1):
            try:
                resultado = func(*args, **kwargs)
                return resultado
            except Exception:
                print(f'Erro ao executar o método {func.__name__}, Tentativa {tentativa} de {self.max_tentativas}')
                time.sleep(self.intervalo)
        
        raise Exception(f"Excedeu o número máximo de tentativas ({self.max_tentativas})")



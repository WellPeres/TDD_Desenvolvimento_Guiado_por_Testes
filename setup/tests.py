from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By 
from animais.models import Animal


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/wellinton-dev/TDD_busca_animal/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def tearDown(self):
        self.browser.quit()


    def test_buscando_um_novo_animal(self):
        """ Teste se um usuário encontra um animal pesquisando """
        #Vini, deseja encontrar um novo animal, para adotar.
        #Ele encontra o Busca Animal e decide usar o site,
        self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele ve um campo para pesquisar animais pelo nome
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertAlmostEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo : leão, urso...')

        # Ele pesqiosa por Leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 características do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # ele desiste de adotar um leão.




    



from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Charger le .feature
scenarios("../features/search_on_duck.feature")


@given("je suis sur la page d'accueil de DuckDuckGo 'https://www.duckduckgo.com'")
def open_duckduckgo_homepage(browser):
    browser.get('https://www.duckduckgo.com')
    # Attente explicite pour être sûr que la page soit complètement chargée
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'searchbox_input'))
    )

@when("je saisis 'Panda' dans la barre de recherche")
def search_query(browser):
    # Attente explicite que le champ de recherche soit présent
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'searchbox_input'))
    )
    search_input.send_keys('Panda')

@when("je clique sur le bouton de recherche")
def click_search(browser):
    # Attente explicite que le bouton de recherche soit cliquable
    search_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    search_button.click()

@then("je devrais voir les résultats de la recherche pour 'Panda'")
def verify_results(browser):
    # Attente explicite que le titre de la page contient le mot 'Panda'
    WebDriverWait(browser, 10).until(
        EC.title_contains("Panda")
    )
    # Vérification du contenu de la page
    assert 'Panda' in browser.title or 'Panda' in browser.page_source
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Feature correspondante
scenarios("../features/search_on_duck.feature")

TIMEOUT = 5

@given(parsers.parse("je suis sur la page d'accueil de DuckDuckGo \'{url}\'"))
def open_duckduckgo_homepage(browser, url):
    browser.get(url)
    # Attente explicite pour être sûr que la page soit complètement chargée
    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "searchbox_input"))
    )

@when(parsers.parse("je saisis \'{search}\' dans la barre de recherche"))
def search_query(browser, search):
    # Attente explicite que le champ de recherche soit présent
    search_input = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "searchbox_input"))
    )
    search_input.send_keys(search)


@when(parsers.parse("je clique sur le bouton de recherche"))
def click_search(browser):
    # Attente explicite que le bouton de recherche soit cliquable
    search_button = WebDriverWait(browser, TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    search_button.click()


@then(parsers.parse("je devrais voir les résultats de la recherche pour \'{search}\'"))
def verify_results(browser, search):
    # Attente explicite que le titre de la page contient le mot SEARCH
    WebDriverWait(browser, TIMEOUT).until(EC.title_contains(search))
    # Vérification du contenu de la page
    assert search in browser.title or search in browser.page_source

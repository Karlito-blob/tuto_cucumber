Feature: Recherche sur DuckDuckGo

  En tant qu’utilisateur, je peux effectuer une recherche

  Scenario: Un utilisateur effectue une recherche
    Given je suis sur la page d'accueil de DuckDuckGo 'https://www.duckduckgo.com'
    When je saisis 'Panda' dans la barre de recherche
    And je clique sur le bouton de recherche
    Then je devrais voir les résultats de la recherche pour 'Panda'

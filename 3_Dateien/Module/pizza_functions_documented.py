#Importieren von benötigen Modulen
import re
import time

def yn_validator(prompt, yes_regex, no_regex):
    """Funktion nimmt 'prompt' sowie reguläre Ausdrücke für 'Ja' und 'Nein' und
    gibt dem/r User:in solange 'prompt' aus, bis der darauffolgende Input (der 'answer' zugewiesen wird)
    entweder vollständig die 'Ja'- oder 'Nein'-RegEx matcht ('re.fullmatch'). Matcht er die 'Ja'-Regex,
    wird ein normalisiertes 'yes' zurückgegeben, matcht er die 'Nein'-RegEx,
    wird ein normalisiertes 'no' zurückgegeben, andernfalls wird 'reaction_to_invalid_input'
    ausgegeben, gefolgt von der nächsten Iteration beginnend mit der Ausgabe von 'prompt'."""
    
    #diese Ausgabe wird hier innerhalb der Funktion definiert und nicht als Argument übergegeben, da sie unabhängig vom Kontext des Funktionsaufrufs immer diesselbe ist
    reaction_to_invalid_input = "\nBitte antworte entweder mit 'Ja' oder 'Nein'."
    
    while True: 
        
        answer = input(prompt)
    
        if re.fullmatch(yes_regex, answer, re.I):
            return "yes" 
        elif re.fullmatch(no_regex, answer, re.I):
            return "no"
        else:
            time.sleep(1)
            print(reaction_to_invalid_input)

def choose_pizza(first_prompt, alternative_prompt, reaction_to_invalid_input, pizzas):
    """Funktion gibt dem/r User:in einmalig 'first_prompt' aus, da 'choice' initial auf 'None' gesetzt ist und
    die Bedingung 'if not choice' True ergibt. Antwort wird 'choice' zugewiesen.
    Anschließend wird über das als Argument übergebene dictionary 'pizzas' iteriert,
    und 'choice' nach der RegEx jeder Pizza abgesucht. Liegt ein vollständiger match vor (re.fullmatch), wird der Name
    der Pizza zurückgegeben. Andernfalls startet die while-Schleife von neuem, wobei 'choice' jetzt nicht mehr 'None'
    ist und entsprechend die Bedingung 'if not choice' False ergibt. Folglich tritt 'else' ein und 'alternative_prompt'
    wird ausgegeben, 'choice' wird mit neuem Input überschrieben. 'choice' wird wieder auf match mit den alternativen
    Schreibweisen abgeglichen. Liegt ein match vor, wird die jeweilige Pizza zurückgegeben, anderfalls startet eine neue Iteration."""

    choice = None
    
    while True:
        
        if not choice: 
            choice = input(first_prompt)
        
        else:
            time.sleep(1)
            print(reaction_to_invalid_input)
            choice = input(alternative_prompt)
            
        for pizza in pizzas.keys():
            if re.fullmatch(pizzas[pizza]["alternative_names"], choice, re.I):
                return pizza

def remove_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, ingredients, confirmation, yes_regex, no_regex):
    """Funktion gibt solange 'first_prompt' (Frage nach zu entfernender Zutat) aus, 
    wie User:in auf den am Ende der 'while'-Schleife ausgegebenen 'alternative_prompt' mit (über 'yn_validator' normalisiertem) 'yes' antwortet.
    Solange das der Fall ist, wird die auf 'first_prompt' erhaltene Antwort kleingeschrieben 'ingredient_to_be_removed' zugewiesen.
    Befindet sich 'ingredient_to_be_removed' unter den ebenfalls als Argument übergebenen (und initial kleingeschriebenen) Zutatenliste ('ingredients_lower'), 
    wird 'confirmation' ausgegeben und entsprechende Zutat von der Liste entfernt. Befindet sich 'ingredient_to_be_removed' nicht auf der Zutatenliste, 
    wird 'reaction_to_invalid_input' ausgegeben. Nun wird 'alternative_prompt' ausgegeben: User:in muss sich entscheiden,
    ob (noch) eine Zutat entfernt werden soll. Bei Zustimmung beginnt die nächste Iteration, andernfalls (bei normalisiertem 'no')
    wird die neue Liste mit Zutaten (mit großen Anfangsbuchstaben) zurückgegeben."""
    
    #Kleinschreibung erleichtert Überprüfung, ob gegebenes Element bereits in der Liste ist
    ingredients_lower = [ingredient.lower() for ingredient in ingredients]
    
    while True:
    
        ingredient_to_be_removed = input(first_prompt).lower()

        if ingredient_to_be_removed in ingredients_lower:
            print(confirmation)
            ingredients_lower.remove(ingredient_to_be_removed)
        else: 
            time.sleep(1)
            print(reaction_to_invalid_input)
        
        remove_another_ingredient = yn_validator(alternative_prompt, yes_regex, no_regex)
        
        if remove_another_ingredient == "no":
            return [ingredient.capitalize() for ingredient in ingredients_lower]
        
def add_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, ingredients, extra_ingredients, confirmation, yes_regex, no_regex):
    """Funktion gibt solange 'first_prompt' (Frage nach hinzuzufügender Zutat) aus, 
    wie User:in auf den am Ende der 'while'-Schleife ausgegebenen 'alternative_prompt' mit (über 'yn_validator' normalisiertem) 'yes' antwortet.
    Solange das der Fall ist, wird die auf 'first_prompt' erhaltene Antwort kleingeschrieben 'new_ingredient' zugewiesen.
    Befindet sich 'new_ingredient' nicht bereits unter den ebenfalls als Argument übergebenen (und initial kleingeschriebenen) Zutatenliste ('ingredients_lower') UND
    gleichzeitig auf der (auch initial kleingeschriebenen) Liste der Extrazutaten ('extra_ingredients_lower'), 
    wird 'confirmation' ausgegeben und entsprechende Zutat 'ingredients_lower' angehängt. Andernfalls (falls mind. eine der Bedingungen nicht zutrifft),
    wird 'reaction_to_invalid_input ausgegeben. Nun wird 'alternative_prompt' ausgegeben: User:in muss sich entscheiden,
    ob (noch) eine Zutat hinzugefügt werden soll. Bei Zustimmung beginnt die nächste Iteration, andernfalls (bei normalisiertem 'no')
    wird die neue Liste mit Zutaten (mit großen Anfangsbuchstaben) zurückgegeben."""

    #Kleinschreibung erleichtert Überprüfung, ob gegebenes Element bereits in der Liste ist
    ingredients_lower = [ingredient.lower() for ingredient in ingredients]
    extra_ingredients_lower = [ingredient.lower() for ingredient in extra_ingredients]
    
    while True:
    
        new_ingredient = input(first_prompt).lower()

        if new_ingredient in extra_ingredients_lower and new_ingredient not in ingredients_lower:            
            print(confirmation)
            ingredients_lower.append(new_ingredient)
        else:
            time.sleep(1)            
            print(reaction_to_invalid_input)
        
        add_another_ingredient = yn_validator(alternative_prompt, yes_regex, no_regex)
        
        if add_another_ingredient == "no":
            return [ingredient.capitalize() for ingredient in ingredients_lower]
        
def request_address(first_prompt, alternative_prompt, reaction_to_invalid_input, w3w_regex):
    """Funktion gibt dem/r User:in einmalig 'first_prompt' aus, da 'pizza_destination' initial auf 'None' gesetzt ist und
    die Bedingung 'if not pizza_destination' True ergibt. Antwort wird 'pizza_destination' zugewiesen.
    Anschließend wird geprüft, ob 'w3w_regex' vollständig 'pizza_destination' matcht (re.fullmatch). 
    Wenn ja, wird 'pizza_destination' zurückgegeben, andernfalls 'reaction_to_invalid_input' ausgegeben 
    und die nächste Iteration der 'while'-Schleife beginnt, wobei 'pizza_destination' jetzt nicht mehr 'None'
    ist und entsprechend die Bedingung 'if not pizza_destination' False ergibt. Folglich tritt 'else' ein und 'alternative_prompt'
    wird ausgegeben, 'pizza_destination' wird mit neuem Input überschrieben. 'pizza_destination' wird wieder auf match mit 'w3w-regex' abgeglichen. 
    Liegt ein match vor, wird 'pizza_destination' zurückgegeben, anderfalls startet eine neue Iteration."""

    pizza_destination = None
    
    while True:
    
        if not pizza_destination:
            pizza_destination = input(first_prompt)
        else:
            pizza_destination = input(alternative_prompt)
            
        if re.fullmatch(w3w_regex, pizza_destination, re.I):
            return pizza_destination
        else:
            time.sleep(1)            
            print(reaction_to_invalid_input)
#Importieren von benötigen Modulen sowie allen Funktionen des Moduls 'pizza_functions_documented'
import re
import time
from pizza_functions_documented import *

#------------> REGEX PATTERNS <------------ 

"""diese RegEx werden unten in 'order_pizza' bzw. 'choose_pizza' benutzt,
um alternative Schreibweisen der bestellbaren Pizzen zu validieren und normalisieren"""
margherita_regex = r"m(a|e)rg(h)?(e|a)rita"
prosciutto_regex = r"pro(s)?cc?(i|h)?utt?o|schinken"
vegetariana_regex = r"veg(etari((an)?(a|o)|sch)|i)"


"""diese RegEx werden unten in div. Funktionen benutzt, um alternative Schreibweisen von
'Ja' und 'Nein' zu validieren und normalisieren"""
yes_regex = r"j(a|o|u)a?p?( klar| bitte| danke)?|klar(o)?|y(e|a)s?(ah)?( please)?|m(m?)hm|si|oui"
no_regex = r"n(e|ö|o|i)(e|ö)?(in|t|ne|pe|ver)?( danke| thanks)?|niemals|(bitte )?nicht"

#diese RegEx wird benutzt, um unten in 'order_pizza' bzw. 'request_addresss' w3w-addressen zu validieren
w3w_regex = r"[a-zäöüß]+\.[a-zäöüß]+\.[a-zäöüß]+"

#------------> AVAILABLE PIZZAS <------------ 

"""dieses dictionary besteht aus den verfügbaren Pizzen als Schlüssel,
sowie ein weiteres dictionary als Wert, mit weiteren Daten zur jeweiligen Pizza;
jedes innere dictionary besteht aus alternativen Namen (Schlüssel) bzw. Pizza-RegEx (Wert)
sowie Zutaten (Schlüssel) bzw. Zutatenliste (Wert)"""
pizzas = {"Margherita": {"alternative_names": margherita_regex, "ingredients": ["Mozzarella", "Tomatensauce", "Oregano"]}, 
          "Prosciutto": {"alternative_names": prosciutto_regex, "ingredients": ["Mozzarella", "Schinken", "Tomatensauce"]}, 
          "Vegetariana": {"alternative_names": vegetariana_regex, "ingredients": ["Mozzarella", "Tomatensauce", "Aubergine", "Zucchini", "Champignons"]}}

#Liste mit verfügbaren zusätzlichen Zutaten
extra_ingredients = ["Ananas", "Schinken", "Aubergine", "Mais", "Kirschtomaten", "Parmesan", "Kapern", "Rucola"]

#Hauptfunktion (wird in JupyterLab importiert und ausgeführt)
def order_pizza():
	"""Funktion leitet durch Bestellprozess, indem für einzelne Schritte relevante Funktionen aus dem Modul 'pizza_functions_documented' aufgerufen werden.
	Die den Funktionen zu übergebenden Argumente (prompts an User:in) werden jeweils direkt vor Funktionsaufruf definiert. 
	Grober Ablauf: 
	1) User:in wird gegrüßt. 
	2) 'choose_pizza' wird aufgerufen, um eine valide Pizzawahl zu erhalten.
	3) Bestätigung der Pizzawahl sowie Auflistung der Zutaten wird ausgegeben.
	4) 'yn_validator' wird aufgerufen, um abzufragen, ob User:in eine Zutat verändern will. Wenn ja > 5), wenn nein > 9)
	5) 'yn_validator' wird aufgerufen, um abzufragen, ob User:in eine Zutat entfernen will. Wenn ja > 6), wenn nein > 7)
	6) 'remove_ingredient' wird aufgerufen, um eine aktualisierte Zutatenliste zu erhalten.
	7) 'yn_validator' wird aufgerufen, um abzufragen, ob User:in eine Zutat hinzufügen will. Wenn ja > 8), wenn nein > 9) 
	8) 'add_ingredient' wird aufgerufen, um eine aktualisierte Zutatenliste zu erhalten.
	9) Validität der Bestellung wird überprüft. Wenn invalide endet der Bot, wenn valide > 10)
	10) Bestätigung der Pizzawahl sowie Auflistung der aktualisierten Zutaten wird ausgegeben.
	11) 'request_address' wird aufgerufen, um valide Lieferadresse zu erhalten.
	12) Bestellbestätigung inkl. Pizzawahl und Lieferadresse wird ausgegeben. Bot endet."""

	#------------> CHOOSE PIZZA <------------ 

	#User:in wird initial nach Name gefragt; Name wird in 'user_name' gespeichert
	user_name = input("Hallo, ich bin der Pizzabot 🍕🤖\nWie heißt Du?\n")

	#um eine authentischere Interaktion zu simulieren fügt diese Zeile eine Sekunde Latenz ein (gilt auch für alle folgenden gleichlautenden Zeilen)
	time.sleep(1)

	"""Definition der Argumente für die unten aufgerufene Funktion 'choose_pizza' aus dem Modul 'pizza_functions_documented',
	inkl. persönlicher Ansprache und einer Auflistung verfügbarer Pizzen bei falschem Input ('pizza'-Schlüssel zu string konkateniert mittels 'join')."""
	first_prompt = "\nSuper " + user_name + ", welche Pizza möchtest Du bestellen?\n"
	reaction_to_invalid_input = "\nDiese Pizza biete ich leider nicht an. 🫤\nBitte wähle zwischen " + ", ".join(pizzas) + ".\n"
	alternative_prompt = "Welche Pizza möchtest Du bestellen, " + user_name + "?\n"

	"""Aufruf von 'choose_pizza' und Übergabe der oben definierten Argumente,
	'choose_pizza' gibt gewählte Pizza zurück, sobald eine korrekte Wahl getroffen wurde 
	(Details siehe Dokumentation in 'pizza_functions_documented.py'),
	gewählte Pizza wird 'pizza' zugewiesen"""
	pizza = choose_pizza(first_prompt, alternative_prompt, reaction_to_invalid_input, pizzas)
	"""User:in wird über Zutaten der gewählten Pizza informiert,
	Zutaten werden im inneren dictionary abgerufen und mittels 'join' zu einem string konkateniert""" 
	print("\nSuper Wahl! 😋\nDiese Pizza bereite ich mit " + ", ".join(pizzas[pizza]["ingredients"]) + " zu.")

	time.sleep(1)

	#Zutaten der ausgewählten Pizza werden zusätzlich der Variablen 'pizza_ingredients' zugewiesen
	pizza_ingredients = pizzas[pizza]["ingredients"]

	#------------> CHANGE INGREDIENTS? <------------ 

	#Definition eines Prompts, der unten als Argument der Funktion 'yn_validator' übergeben wird
	prompt = "\nMöchtest Du an den Zutaten etwas ändern?\n"
	"""Aufruf von 'yn_validator', Übergabe von 'prompt' sowie der regulären Ausdrücke für "Ja" und "Nein",
	'yn_validator' gibt validiertes/normalisiertes 'yes' oder 'no' zurück sobald User:in eine validierbare/normalisierbare 
	Antwort gegeben hat (Details siehe Dokumentation in 'pizza_functions_documented.py'),
	'yes' bzw. 'no' wird 'change_yn' zugewiesen"""
	change_yn = yn_validator(prompt, yes_regex, no_regex)

	#wenn User:in Zutaten anpassen will...
	if change_yn == "yes":

	    #------------> REMOVE INGREDIENTS? <------------ 

	    time.sleep(1)

	    #Definition eines Prompts, der unten als Argument der Funktion 'yn_validator' übergeben wird
	    prompt = "\nMöchtest Du eine Zutat entfernen?\n"
	    """Aufruf von 'yn_validator', Übergabe von 'prompt' sowie der regulären Ausdrücke für "Ja" und "Nein",
		'yn_validator' gibt validiertes/normalisiertes 'yes' oder 'no' zurück (Details siehe Dokumentation in 'pizza_functions_documented.py'), 
		sobald User:in eine validierbare/normalisierbare Antwort gegeben hat,
		'yes' bzw. 'no' wird 'remove_yn' zugewiesen"""
	    remove_yn = yn_validator(prompt, yes_regex, no_regex)

	    #wenn User:in eine Zutat entfernen will...
	    if remove_yn == "yes":

	        time.sleep(1)

	        #Definition von Argumenten, die unten der Funktion 'remove_ingredient' übergeben werden
	        first_prompt = "\nWelche Zutat möchtest Du entfernen?\n"
	        alternative_prompt = "\nMöchtest Du eine andere Zutat entfernen?\n"
	        reaction_to_invalid_input = "\nDiese Zutat ist nicht auf Deiner Pizza. 🫤"
	        confirmation = "\nKlar doch! 👌"

	        """Aufruf von 'remove_ingredients', Übergabe der oben definierten Argumente, der Liste mit Zutaten sowie der regulären Ausdrücke für 'Ja' und 'Nein',
	        'remove_ingredients' gibt Liste mit aktualisierten Zutaten zurück (Details siehe Dokumentation in 'pizza_functions_documented.py'),
	        neue Liste wird 'pizza_ingredients' zugewiesen (befindliche Liste wird überschrieben)"""
	        pizza_ingredients = remove_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, pizza_ingredients, confirmation, yes_regex, no_regex)

	    #------------> ADD INGREDIENTS? <------------ 

	    time.sleep(1)

	   	#Definition eines Prompts, der unten als Argument der Funktion 'yn_validator' übergeben wird
	    prompt = "\nMöchtest Du eine Zutat hinzufügen?\n"
	    """Aufruf von 'yn_validator', Übergabe von 'prompt' sowie der regulären Ausdrücke für "Ja" und "Nein",
		'yn_validator' gibt validiertes/normalisiertes 'yes' oder 'no' zurück (Details siehe Dokumentation in 'pizza_functions_documented.py'), 
		sobald User:in eine validierbare/normalisierbare Antwort gegeben hat,
		'yes' bzw. 'no' wird 'add_yn' zugewiesen"""
	    add_yn = yn_validator(prompt, yes_regex, no_regex)

	    #wenn User:in eine Zutat hinzufügen will...
	    if add_yn == "yes":

	        time.sleep(1)

	        """Definition von Argumenten, die unten der Funktion 'add_ingredient' übergeben werden inkl. Auflistung
	        verfügbarer Zutaten, falls nicht verfügbare Zutat gewünscht wird ('extra_ingredients zu string konkateniert mittels 'join')"""
	        first_prompt = "\nWelche Zutat möchtest Du hinzufügen?\n"
	        alternative_prompt = "\nMöchtest Du eine weitere Zutat hinzufügen?\n"
	        reaction_to_invalid_input = "\nDiese Zutat kann ich leider nicht hinzufügen. 🫤\n Sofern nicht bereits auf Deiner Pizza, hast Du die Wahl zwischen " + ", ".join(extra_ingredients) + "."
	        confirmation = "\nKlar doch! 👌"

	        """Aufruf von 'add_ingredients', Übergabe der oben definierten Argumente, der (mittlerweile potentiell aktualisierten) Liste mit Zutaten sowie der regulären Ausdrücke für 'Ja' und 'Nein',
	        'add_ingredients' gibt Liste mit aktualisierten Zutaten zurück (Details siehe Dokumentation in 'pizza_functions_documented.py'),
	        neue Liste wird 'pizza_ingredients' zugewiesen (befindliche Liste wird überschrieben)"""
	        pizza_ingredients = add_ingredient(first_prompt, alternative_prompt, reaction_to_invalid_input, pizza_ingredients, extra_ingredients, confirmation, yes_regex, no_regex)

	time.sleep(1)

	#------------> VALID ORDER? <------------ 

	#Überprüfen ob die Bestellung noch gültig ist
	#Wenn weniger als eine Zutat übrig (also keine)...
	if len(pizza_ingredients) < 1:

		#User:in wird über ungültige Bestellung informiert, der Bot endet.
	    print("\nDiese Bestellung ist leider ungültig, da Du sämtliche Zutaten von der Pizza entfernt hast. Bitte bestelle erneut.")

	#sonst...
	else:

		#Bestätigung inkl. Wahl der Pizza und (ggf. modifizierter) Zutatenlist (mittels 'join' zu string konkateniert) wird ausgegeben
	    print("\nSuper, Du kriegst also eine Pizza " + pizza + " mit " + ", ".join(pizza_ingredients) + ".\n")

	    #------------> REQUEST DELIVERY ADDRESS <------------ 

	    time.sleep(1)

	    #Definition von Argumenten, die unten der Funktion 'request_address' übergeben werden
	    first_prompt = "Wohin darf ich Deine Pizza liefern?\nIch liefere nicht nur zu Dir nach Hause, sondern auch zu Deiner liebsten Bank im Park oder direkt an Dein Strandtuch.\nGib also eine addresse von www.what3words.com an.\n"
	    alternative_prompt = "Diesmal klappt's. Wohin darf ich Deine Pizza liefern?\n"
	    reaction_to_invalid_input = "\nSorry, diese addresse verstehe ich nicht. Ich verstehe z.B. 'falschen.fliegen.beliebten'.\n"

	    """Aufruf von 'request_address', Übergabe der oben definierten Argumente sowie des regulären Ausdrucks für die w3w-Adresse,
	    'request_address' gibt validierte Adresse zurück, sobald User:in eine solche gegeben hat (Details siehe Dokumentation in 'pizza_functions_documented.py'),
	    Adresse wird 'pizza_destination' zugewiesen"""
	    pizza_destination = request_address(first_prompt, alternative_prompt, reaction_to_invalid_input, w3w_regex)

	    time.sleep(1)

	    #User:in wird über geglückte Bestellung informiert, bestellte Pizza und Lieferadresse werden mitausgegeben
	    print("\nPerfekt, " + user_name + ". Ich liefere Deine Pizza " + pizza + " an " + pizza_destination + "! 🍕")

"""Fortgeschritten: Gängiger Codeblock in Skripts, der sicherstellt, dass der Code sowohl als Modul importiert werden kann, 
als auch über das Terminal/die Eingabeaufforderung aufgerufen werden kann:
Wenn das Skript als Modul importiert wird, wird seinem '__name__'-Attribut automatisch der Name des Moduls verliehen (Bedingung unten trifft also nicht zu, und es geschieht nichts weiter).
Wenn das Skript im Terminal/der Eingabeaufforderung ausgeführt wird, wird dem '__name__'-Attribut '__main__' zugewiesen und die Bedingung trifft zu,
folglich wird 'order_pizza' aufgerufen und der obige Code damit innerhalb des Terminals/der Eingabeaufforderung ausgeführt."""
if __name__ == "__main__":

    order_pizza()

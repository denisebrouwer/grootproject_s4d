from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import database
import pickle
from tkinter import *

root = Tk()
root.geometry("400x500")


urls_allerhande = []

def urls_ophalen():
    pickle_in = open("urls_allerhande_lijst", "rb")
    global urls_allerhande
    urls_allerhande = pickle.load(pickle_in)


# DEZE FUNCTIE ZORGT ERVOOR DAT DE URLS WORDEN TOEGEVOEGD AAN HET BESTAND
def urls_toevoegen():
    pickle_out = open("urls_allerhande_lijst", "wb")
    pickle.dump(urls_allerhande, pickle_out)
    pickle_out.close()


def scraper():
    door_te_zoeken_urls = ["https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vqZ26v8/pasta?Nrpp=1500",
                           "https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vqZ26x9/salade?Nrpp=1500",
                           "https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vqZ26v9/rijst?Nrpp=1500",
                           "https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vqZ26xa/soep?slug=&Nrpp=1500",
                           "https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vqZ26xc/stamppot?slug=&Nrpp=1500"]

    try:
        urls_ophalen()
    except:
        print("Er is nog geen URL bestand, die wordt nu aangemaakt")

    try:
        database.database_ophalen()
        from database import recepten
    except:
        print("Er is nog geen recept bestand, die wordt nu aangemaakt")

    for url in door_te_zoeken_urls:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")

        content_container = page_soup.find("div", {"id": "items-wrapper"})
        containers = content_container.findAll("section")

        for container in containers:
            url_recept_half = container.figure.a["href"]
            url_recept_heel = "https://www.ah.nl" + url_recept_half
            print(url_recept_heel)

            if url_recept_heel not in urls_allerhande:
                urls_allerhande.append(url_recept_heel)

                if url == door_te_zoeken_urls[0]:
                    categorie = "Pasta"
                if url == door_te_zoeken_urls[1]:
                    categorie = "Salade"
                if url == door_te_zoeken_urls[2]:
                    categorie = "Rijst"
                if url == door_te_zoeken_urls[3]:
                    categorie = "Soep"
                if url == door_te_zoeken_urls[4]:
                    categorie = "Stamppot"

                url_recepten = url_recept_heel

                uClient_recept = uReq(url_recepten)
                page_recept_html = uClient_recept.read()
                uClient_recept.close()
                page_soup_recept = soup(page_recept_html, "html.parser")

                # ONDERSTAAND IS VOOR DE TITEL UIT TE PRINTEN VAN HET GERECHT
                content_container_recept = page_soup_recept.find("div", {"id": "body-container"})
                titel_recept = content_container_recept.find("h1", {"itemprop": "name"}).text.replace("­", "")

                # ONDERSTAAND IS VOOR DE INGRIEDIËNTENLIJST IN EEN ARRAY TE ZETTEN
                content_container_ingredieenten = content_container_recept.findAll("span", {"class": "js-label label"})
                ingredieenten = content_container_ingredieenten

                ingredieenten_lijst = []

                for ingredieent in ingredieenten:
                    losse_ingredieenten = ingredieent.text.replace("\xa0", " ")
                    ingredieenten_lijst.append(losse_ingredieenten)

                # ONDERSTAAND IS OM DE BEREIDING TE WEERGEVEN
                try:
                    content_bereidingswijze = page_soup_recept.find("ol")
                    bereidings_stappen = content_bereidingswijze.findAll("li")
                    bereidingswijze = []

                    for bereidings_stap in bereidings_stappen:
                        losse_bereidings_stap = bereidings_stap.text
                        bereidingswijze.append(losse_bereidings_stap)
                except:
                    try:
                        content_bereidingswijze = page_soup_recept.find("div", {"class", "content-wrapper"})
                        bereidingswijze_stappen = content_bereidingswijze.findAll("p")
                        bereidingswijze_stap = bereidingswijze_stappen[2].text
                        bereidingswijze = []
                        bereidingswijze.append(bereidingswijze_stap)
                    except:
                        content_bereidingswijze = page_soup_recept.find("div", {"class", "content-wrapper"})
                        bereidingswijze_stappen = content_bereidingswijze.findAll("p")
                        bereidingswijze_stap = bereidingswijze_stappen[1].text
                        bereidingswijze = []
                        bereidingswijze.append(bereidingswijze_stap)

                # ONDERSTAAND IS OM DE BEREIDINGSDUUR TE WEERGEVEN
                content_bereidingsduur = page_soup_recept.find("li", {"class", "cooking-time"})
                bereidings_tijden = content_bereidingsduur.findAll("li")

                bereidingsduur = []

                for bereidingstijd in bereidings_tijden:
                    losse_bereidingsduur = bereidingstijd.text
                    bereidingsduur.append(losse_bereidingsduur)

                # ONDERSTAAND IS OM DE KCAL WEER TE GEVEN
                content_voedingswaarden = page_soup_recept.find("ul", {"class", "short"})
                container_voedingswaarden_kcal = content_voedingswaarden.findAll("li")
                try:
                    voedingswaarden_kcal = container_voedingswaarden_kcal[2].span.text.replace("voedingswaarden", "")
                except:
                    voedingswaarden_kcal = ""

                print(categorie)
                print(titel_recept)
                print(ingredieenten_lijst)
                print(bereidingswijze)
                print(bereidingsduur)
                print(voedingswaarden_kcal)

                database.nieuw_recept(titel_recept, categorie, voedingswaarden_kcal, bereidingsduur,
                                      ingredieenten_lijst, 3, bereidingswijze,)

    urls_toevoegen()
    database.database_wegschrijven()


# EINDE SCRAPER FUNCTIE ------------------------------------------------------------------------------------------

def buttons():
    recepten_button = Button(text="check voor nieuwe recepten", command = scraper)
    recepten_button.pack()

    planner_button  = Button(text="weekplanner invullen", command = database.dagen_invullen)
    planner_button.pack()

# buttons()
# root.mainloop()

database.recepten_ingredieenten()
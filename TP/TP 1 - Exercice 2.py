import numpy as np
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
nom_sites = ["Site A", "Site B", "Site C", "Site D"]
# Chargement
siteA = np.random.randint(10, 201, size=(7, 24))
siteB = np.random.randint(10, 201, size=(7, 24))
siteC = np.random.randint(10, 201, size=(7, 24))
siteD = np.random.randint(10, 201, size=(7, 24))

liste_sites = [siteA, siteB, siteC, siteD]
for i in range(4):
    tab = liste_sites[i]
    nom = nom_sites[i]

print("Tableau", nom, ":")
print(tab)
print()
moyenne = np.mean(tab)
max_requetes_jour = -1
index_jour_actif = 0

for j in range(7):
    total_jour = np.sum(tab[j])
    if total_jour > max_requetes_jour:
        max_requetes_jour = total_jour
        index_jour_actif = j
jour_actif = jours[index_jour_actif]
print("📊 Analyse de", nom, ":")
print("🔹 Moyenne générale :", round(moyenne, 2))
print("🔹 Jour le plus actif :", jour_actif)

#Pics inhabituels
ecart_type = np.std(tab)
seuil = moyenne + ecart_type
print("🔹 Seuil pour pics inhabituels :", round(seuil, 2))
for j in range(7):
    for h in range(24):
        valeur = tab[j, h]
        if valeur > seuil:
            print("⚠️ Pic inhabituel détecté le", jours[j], "à", h, "h :", valeur, "requêtes")
print("\n" + "_"*50 + "\n")

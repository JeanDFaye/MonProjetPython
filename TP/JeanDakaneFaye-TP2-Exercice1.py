from enum import Enum, auto

# Classe pour les types de formation
class TypeFormation(Enum):
    RESEAU = auto()
    PYTHON = auto()
    SECURITE_WEB = auto()
    FORENSIQUE = auto()

# Classe pour les formations
class Formation:
    # Constructeur
    def __init__(self, code:str,titre:str,type_formation:TypeFormation,capacite_max:int):
        self.code = code
        self.titre = titre
        self.type_formation = type_formation
        self.capacite_max = capacite_max
        self.nombre_inscrits = 0

    # Methode pour s'inscrire
    def inscrire(self) -> bool:
        if self.nombre_inscrits < self.capacite_max:
            self.nombre_inscrits += 1
            return True
        return False

    # Methode pour s'inscrire
    def desinscrire(self) -> bool:
            if self.nombre_inscrits > 0:
                self.nombre_inscrits -= 1
                return True
            return False
    # Methode est complete
    def est_complete(self) -> bool:
        return self.nombre_inscrits == self.capacite_max

    # Methode pour les places restantes
    def places_restantes(self) -> int:
        return self.capacite_max - self.nombre_inscrits

    # Methode pour afficher les informations de la formation
    def afficher(self):
        print(f"Code : {self.code}")
        print(f"Titre : {self.titre}")
        print(f"Type : {self.type_formation.name}")
        print(f"Capacité maximale : {self.capacite_max}")
        print(f"Nombre d'inscrits : {self.nombre_inscrits}")
        print(f"Places restantes : {self.places_restantes()}")
        print("-" * 30)

# Classe du centre de formation
class CentreFormation:
    def __init__(self, nom: str):
        self.nom = nom
        self.formations = []

    def ajouter_formation(self, formation: Formation):
        self.formations.append(formation)

    def rechercher_formation(self, code: str):
        for f in self.formations:
            if f.code == code:
                return f
        return None

    def afficher_formations(self):
        for f in self.formations:
            f.afficher()

    def nombre_total_inscrits(self) -> int:
        total = 0
        for f in self.formations:
            total += f.nombre_inscrits
        return total

    def formation_plus_populaire(self) -> Formation:
        # Retourne l'objet de formation avec le plus grand nombre d'inscrptions
        return max(self.formations, key=lambda f: f.nombre_inscrits)

# Creation du centre
centre = CentreFormation("CyberFormation")
f1 = Formation("CYB101", "Sécurité des réseaux", TypeFormation.RESEAU, 3)
f2 = Formation("PYT201", "Python pour la cybersécurité", TypeFormation.PYTHON, 2)
f3 = Formation("WEB301", "Sécurité des applications Web", TypeFormation.SECURITE_WEB, 4)

# Ajout des formations au centre
centre.ajouter_formation(f1)
centre.ajouter_formation(f2)
centre.ajouter_formation(f3)

# Inscriptions
f1.inscrire()
f1.inscrire()
f1.inscrire()

f2.inscrire()
f2.inscrire()

f3.inscrire()

# Inscription a un cours deja plein
f2.inscrire()

# Consulter les informations
print("=== NOS FORMATIONS ===")
centre.afficher_formations()

print(f"Nombre total d’etudiants inscrits dans le centre: {centre.nombre_total_inscrits()}\n")

print("=== RECHERCHE DE LA FORMATION PYT201 ===")
recherche = centre.rechercher_formation("PYT201")
if recherche:
    recherche.afficher()

print(f"Nombre de places restantes dans f3 (WEB301): {f3.places_restantes()}\n")

print("=== FORMATION LA PLUS POPULAIRE ===")
populaire = centre.formation_plus_populaire()
populaire.afficher()

# --- Desinscription ---
f1.desinscrire()
print("=== F1 APRES DESINSCRIPTION ===")
f1.afficher()

# --- Tests de verification avec assert ---
assert len(centre.formations) == 3
assert f1.nombre_inscrits == 2
assert f2.nombre_inscrits == 2
assert f3.nombre_inscrits == 1
assert f2.est_complete() is True
assert f3.places_restantes() == 3
assert centre.rechercher_formation("PYT201") is f2
assert centre.rechercher_formation("ABC999") is None
assert centre.nombre_total_inscrits() == 5

print("✅ Tous les tests ont réussi.")
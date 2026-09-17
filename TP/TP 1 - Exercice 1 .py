from abc import ABC, abstractmethod

# Classe abstraite
class Utilisateur(ABC):

    def __init__(self, nom: str):
        self.nom = nom

    @abstractmethod
    def envoyer_message(self, destinataire: "Utilisateur", contenu: str):
        pass

# Sous-classes
class UtilisateurBasique(Utilisateur):

    def envoyer_message(self, destinataire: Utilisateur, contenu: str):
        message_transforme = contenu
        print(f"{self.nom} (UtilisateurBasique) → {destinataire.nom} : {message_transforme}")

class UtilisateurConfidentiel(Utilisateur):

    def envoyer_message(self, destinataire: Utilisateur, contenu: str):
        # Inversion de la chaîne de caractères
        message_transforme = contenu[::-1]
        print(f"{self.nom} (UtilisateurConfidentiel) → {destinataire.nom} : {message_transforme}")

class UtilisateurUltraSecurise(Utilisateur):

    def envoyer_message(self, destinataire: Utilisateur, contenu: str):
        resultat = []

        for caractere in contenu:
            # Conversion en minuscule
            char_lower = caractere.lower()

            # Vérification des caractères
            if "a" <= char_lower <= "z":
                numero_lettre = ord(char_lower) - ord("a") + 1
                resultat.append(str(numero_lettre))
            else:
                resultat.append(caractere)

        # Concaténation
        message_transforme = "".join(resultat)
        print(f"{self.nom} (UtilisateurUltraSecurise) → {destinataire.nom} : {message_transforme}")

# Programme principale
alice = UtilisateurBasique("Alice")
bob = UtilisateurConfidentiel("Bob")
charly = UtilisateurUltraSecurise("Charly")

# Messages
alice.envoyer_message(bob, "Bonjour")
bob.envoyer_message(charly, "Salut")
charly.envoyer_message(alice, "Message Secret")

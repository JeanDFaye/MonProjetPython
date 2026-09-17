def surveiller_port():
    sensitive_ports = [21, 23, 445]

    while True:
        saisie = input("Entrez un port à surveiller : ")
        try:
            port = int(saisie)
        except ValueError:
            print("❌ Erreur : Veuillez entrer un nombre entier valide. Réessayez.")
            continue

        if port < 1 or port > 65535:
            print("❌ Erreur : Le port doit être compris entre 1 et 65535. Réessayez.")
            continue
        break

    if port in sensitive_ports:
        print(f"⚠️ Port {port} détecté : souvent ciblé dans des attaques.")
    else:
        print(f"✅ Port {port} surveillé. Aucun risque immédiat détecté.")


# Appel a la fonction
surveiller_port()

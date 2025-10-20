import math

def addition(a: float, b: float) -> float:
    return a + b

def soustraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible.")
    return a / b

def puissance(a: float, b: float) -> float:
    return a ** b

def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Modulo par zéro impossible.")
    return a % b

def racine_carre(a: float) -> float:
    if a < 0:
        raise ValueError("Impossible de calculer la racine carrée d’un nombre négatif.")
    return math.sqrt(a)

operations = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division,
    "^": puissance,
    "%": modulo,
    "√": racine_carre
}

historique = []

def lire_nombre(message: str) -> float:
    while True:
        texte = input(message).strip().replace(",", ".")
        try:
            return float(texte)
        except ValueError:
            print("Saisie invalide. Entrez un nombre (ex: 3, 4.2, -7).")

def demander_decimales(message: str = "Nombre de décimales à afficher : ") -> int:
    while True:
        texte = input(message).strip()
        if texte == "":
            return 10
        try:
            n = int(texte)
            if n < 0:
                print("Le nombre de décimales doit être positif.")
                continue
            return n
        except ValueError:
            print("Saisie invalide. Entrez un entier (ex: 2, 5, 10).")

def afficher_menu() -> None:
    print("\n=== Calculatrice - TP Python ===")
    print("Choisissez une opération :")
    print("  1) Addition        (+)")
    print("  2) Soustraction    (-)")
    print("  3) Multiplication  (*)")
    print("  4) Division        (/)")
    print("  5) Puissance       (^)")
    print("  6) Modulo          (%)")
    print("  7) Racine carrée   (√)")
    print("  h) Historique")
    print("  e) Exporter l’historique")
    print("  s) Calculer une série")
    print("  q) Quitter")

def obtenir_operation() -> str:
    choix = input("Votre choix: ").strip().lower()
    if choix in ("1", "+"): 
        return "+"
    if choix in ("2", "-"): 
        return "-"
    if choix in ("3", "*"): 
        return "*"
    if choix in ("4", "/"): 
        return "/"
    if choix in ("5", "^"): 
        return "^"
    if choix in ("6", "%"): 
        return "%"
    if choix in ("7",): 
        return "√"
    if choix == "h": 
        return "h"
    if choix == "e": 
        return "e"
    if choix == "s": 
        return "s"
    if choix in ("q"): 
        return "q"
    print("Choix invalide. Réessayez.")
    return ""

def calculer(op: str, a: float, b: float = None) -> float:
    if op not in operations:
        raise ValueError(f"Opération inconnue: {op}")
    fonction = operations[op]
    if op == "√":
        return fonction(a)
    else:
        return fonction(a, b)

def exporter_historique(fichier: str = "historique.txt") -> None:
    if not historique:
        print("Aucun calcul à exporter.")
        return
    with open(fichier, "w", encoding="utf-8") as f:
        f.write("\n".join(historique))
    print(f"Historique exporté dans le fichier '{fichier}'.")

def calculer_serie() -> None:
    print("\n=== Mode Calcul en série ===")
    total = lire_nombre("Entrez le premier nombre : ")
    while True:
        op = obtenir_operation()
        if op not in operations or op == "√":
            print("Choisissez une opération binaire (+, -, *, /, ^, %).")
            continue
        b = lire_nombre("Entrez le nombre suivant : ")
        total = calculer(op, total, b)
        print(f"Résultat actuel : {total}")
        continuer = input("Continuer la série ? (o/n) : ").strip().lower()
        if continuer not in ("o", "oui", "y", "yes", ""):
            break
    historique.append(f"Série = {total}")
    print(f"Résultat final de la série : {total}")

def main() -> None:
    while True:
        afficher_menu()
        op = obtenir_operation()

        if op == "√":
            a = lire_nombre("Entrez le nombre : ")
            z = demander_decimales("Nombre de décimales à afficher (ex: 2,5,10) : ")
        elif op in ("+", "-", "*", "/", "^", "%"):
            a = lire_nombre("Entrez le premier nombre: ")
            b = lire_nombre("Entrez le second nombre: ")
            z = demander_decimales("Nombre de décimales à afficher (ex: 2,5,10) : ")
        elif op == "h":
            if not historique:
                print("Aucun calcul effectué pour l’instant.")
            else:
                print("\n--- Historique ---")
                for ligne in historique:
                    print(ligne)
            continue
        elif op == "e":
            exporter_historique()
            continue
        elif op == "s":
            calculer_serie()
            continue
        elif op == "q":
            print("Au revoir.")
            break
        else:
            continue

        try:
            if op == "√":
                resultat = calculer(op, a)
                ligne = f"√{a} = {resultat:.{z}g}"
            else:
                resultat = calculer(op, a, b)
                ligne = f"{a} {op} {b} = {resultat:.{z}g}"

            print(f"Résultat: {ligne}")
            historique.append(ligne)

        except ZeroDivisionError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")

        continuer = input("Continuer ? (o/n) : ").strip().lower()
        if continuer not in ("o", "oui", "y", "yes", ""):
            print("Au revoir.")
            break

if __name__ == "__main__":
    main()

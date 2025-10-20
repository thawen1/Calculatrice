#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TP 1 — Calculatrice en Python (Première séance)

Objectifs pédagogiques:
- Entrées/sorties avec input() et print()
- Variables, types (int, float), conversions
- Fonctions et réutilisation de code
- Conditions (if/elif/else) et boucles (while)
- Gestion d'erreurs simples (division par zéro, saisie invalide)
- Formatage de chaînes (f-strings)

Consignes:
1) Lancez le programme: python calculatrice.py
2) Suivez le menu pour choisir une opération et saisir des nombres
3) Lisez les commentaires TODO pour des exercices supplémentaires
"""

# Fonctions de calcul de base
def addition(a: float, b: float) -> float:
    """Retourne la somme de a et b."""
    return a + b

def soustraction(a: float, b: float) -> float:
    """Retourne la différence a - b."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Retourne le produit a * b."""
    return a * b

def division(a: float, b: float) -> float:
    """Retourne le quotient a / b. Gère la division par zéro."""
    if b == 0:
        # Levée d'une exception pour montrer la gestion d'erreurs
        raise ZeroDivisionError("Division par zéro impossible.")
    return a / b

# Utilitaire: lecture robuste d'un nombre
def lire_nombre(message: str) -> float:
    """Demande un nombre à l'utilisateur jusqu'à obtenir une saisie valide."""
    while True:
        texte = input(message).strip().replace(",", ".")
        try:
            return float(texte)
        except ValueError:
            print("Saisie invalide. Entrez un nombre (ex: 3, 4.2, -7).")

# Affichage du menu
def afficher_menu() -> None:
    print("\n=== Calculatrice - TP Python (Séance 1) ===")
    print("Choisissez une opération :")
    print("  1) Addition        (+)")
    print("  2) Soustraction    (-)")
    print("  3) Multiplication  (*)")
    print("  4) Division        (/)")
    print("  q) Quitter")

# Sélection de l'opération à partir du choix utilisateur
def obtenir_operation() -> str:
    """Retourne le symbole d'opération choisi: '+', '-', '*', '/', ou 'q'."""
    choix = input("Votre choix: ").strip().lower()
    if choix in ("1", "+"):
        return "+"
    if choix in ("2", "-"):
        return "-"
    if choix in ("3", "*"):
        return "*"
    if choix in ("4", "/"):
        return "/"
    if choix in ("q", "quit", "exit"):
        return "q"
    print("Choix invalide. Réessayez.")
    return ""  # signaler un choix non valide

def calculer(op: str, a: float, b: float) -> float:
    """Applique l'opération op sur a et b."""
    if op == "+":
        return addition(a, b)
    if op == "-":
        return soustraction(a, b)
    if op == "*":
        return multiplication(a, b)
    if op == "/":
        return division(a, b)
    raise ValueError(f"Opération inconnue: {op}")

def main() -> None:
    # Boucle principale
    while True:
        afficher_menu()
        op = obtenir_operation()
        if op == "":
            continue  # mauvais choix, on ré-affiche le menu
        if op == "q":
            print("Au revoir.")
            break

        # Lecture des opérandes
        a = lire_nombre("Entrez le premier nombre: ")
        b = lire_nombre("Entrez le second nombre: ")

        # Calcul + affichage du résultat avec gestion d'erreurs
        try:
            resultat = calculer(op, a, b)
            # Formatage: limite l'affichage à 10 décimales utiles
            print(f"Résultat: {a} {op} {b} = {resultat:.10g}")
        except ZeroDivisionError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")

        # Option: demander si l'utilisateur veut continuer
        continuer = input("Continuer ? (o/n): ").strip().lower()
        if continuer not in ("o", "oui", "y", "yes", ""):
            print("Au revoir.")
            break

# ===========================
# TODO — Exercices supplémentaires (à faire pendant/à la fin du TP)
# 1) Ajoutez une opération puissance (a ** b) dans le menu:
#    - Ajoutez l'option 5) Puissance (^) et acceptez '^' comme saisie.
#    - Créez une fonction puissance(a, b) et adaptez calculer().
#
# 2) Ajoutez une opération modulo (a % b):
#    - Gérez le cas b == 0.
#
# 3) Opérations unaire (racine carrée):
#    - Ajoutez sqrt(a) nécessitant un seul nombre.
#    - Astuce: détectez les opérations à un seul opérande et ignorez la demande du second.
#
# 4) Historique:
#    - Conservez une liste des opérations effectuées (ex: ["3 + 2 = 5"]).
#    - Ajoutez un menu  h) Historique  pour l'afficher.
#
# 5) Validation avancée:
#    - Refusez la racine carrée des nombres négatifs (math.sqrt).
#    - Affichez des messages d'erreur plus précis.
#
# 6) Mise en forme:
#    - Permettez à l'utilisateur de choisir le nombre de décimales à afficher.
#
# 7) Tests rapides:
#    - Écrivez quelques assert, ex: assert addition(2, 3) == 5
#
# 8) Refactorisation:
#    - Remplacez les if/elif de calculer() par un dictionnaire d'opérations.
#
# 9) Bonus:
#    - Exportez l'historique dans un fichier texte.
#    - Ajoutez une option "Calculer une série" qui enchaîne plusieurs opérations.
# ===========================

if __name__ == "__main__":
    main()
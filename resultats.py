resultats = [
    {"id": "TC-001", "module": "panier", "statut": "PASS", "duree": 2.4},
    {"id": "TC-002", "module": "panier", "statut": "FAIL", "duree": 5.1},
    {"id": "TC-003", "module": "login", "statut": "PASS", "duree": 1.2},
    {"id": "TC-004", "module": "login", "statut": "SKIP", "duree": 0.0},
    {"id": "TC-005", "module": "paiement", "statut": "FAIL", "duree": 8.7},
]

piege = [
    {"id": "A", "duree": 1.0},
    {"id": "B", "duree": 9.0},
    {"id": "C", "duree": 3.0},
]


def percentage_success(list_resultats):
    succes_compteur = 0
    echecs_compteur = 0

    for resultat in list_resultats:
        if resultat["statut"] == "PASS":
            succes_compteur += 1
        elif resultat["statut"] == "FAIL":
            echecs_compteur += 1
        else:
            print("Counters must be > 0")
    return (succes_compteur / (succes_compteur + echecs_compteur)) * 100


def failed_ids(list_resultats):
    echecs = []
    for resultat in list_resultats:
        if resultat["statut"] == "FAIL":
            echecs.append(resultat["id"])
    return echecs

def count_by_module(list_resultats):
    compteur = {}
    for resultat in list_resultats:
        module = resultat["module"]
        if module in compteur:
            compteur[module] += compteur[module]
        else:
            compteur[module] = 1
    return compteur


def test_le_plus_long(list_resultats):
    test_id = list_resultats[0]
    for resultat in list_resultats:
        if resultat["duree"] > test_id["duree"]:
            test_id = resultat
    return test_id



STATUTS_VALIDES = {"PASS", "FAIL", "SKIP", "BLOQUE"}

def check_statuts(list_resultats):
    for resultat in list_resultats:
        if resultat["statut"] not in STATUTS_VALIDES:
            raise ValueError(f"Statut inconnu '{resultat["statut"]}' pour le test {resultat["id"]}")
    return True


assert count_by_module(resultats) == {"panier": 2, "login": 2, "paiement": 1}
assert test_le_plus_long(resultats)["id"] == "TC-005"
assert check_statuts(resultats) is True
assert test_le_plus_long(piege)["id"] == "B"
print("Tous les tests passent")










from difflib import SequenceMatcher as SM

def coincidenciasNombres(nombre_buscar,nombre_resultado,radio = 0.70):
    if nombre_resultado.lower() >= nombre_buscar.lower():
        return True
    elif SM(None,nombre_buscar, nombre_resultado).ratio()> radio:
        return True
    else:
        return False
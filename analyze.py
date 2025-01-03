import json_stream
import json
from datetime import datetime


# read sources/fr-en-indicateurs-valeur-ajoutee-colleges.json
# lazy loading to use less memory

# store etablissements (colleges + lycées)
etablissements = {}

annee_courante = datetime.now().year


def float_to_color(value, min_value=90, max_value=100):
    """
    Convertit un float en une couleur entre rouge sombre et vert clair.

    :param value: Valeur flottante entre min_value et max_value
    :param min_value: Valeur minimale (rouge sombre)
    :param max_value: Valeur maximale (vert clair)
    :return: Couleur en format hexadécimal (#RRGGBB)
    """
    # Clamping de la valeur entre min_value et max_value
    value = max(min_value, min(value, max_value))

    # Calcul du ratio de la valeur entre min_value et max_value
    ratio = (value - min_value) / (max_value - min_value)

    # Interpolation des couleurs (rouge sombre -> vert clair)
    red = int((1 - ratio) * 139)  # Rouge sombre (139, 0, 0)
    green = int(ratio * 255)      # Vert clair (0, 255, 0)
    blue = 0                      # Pas de composante bleue

    # Conversion en format hexadécimal
    return f"#{red:02x}{green:02x}{blue:02x}"


print('Loading college data ...')
with open('sources/fr-en-indicateurs-valeur-ajoutee-colleges.json') as f:
    data = json_stream.load(f)
    for line in data:
        converted = json_stream.to_standard_types(line)

        if 'session' not in converted:
            print('Missing session: ' + converted['uai'])
            print(converted)
            continue

        if converted['uai'] in etablissements and converted['session'] in etablissements[converted['uai']]:
            print('Duplicate UAI: ' + converted['uai'])
            print(converted)
            continue
        
        # remove null values
        converted = {k: v for k, v in converted.items() if v is not None}

        if converted['uai'] not in etablissements:
            etablissements[converted['uai']] = {}

        etablissements[converted['uai']][converted['session']] = converted

print('Loading lycée data ...')
with open('sources/fr-en-indicateurs-de-resultat-des-lycees-gt_v2.json') as f:
    data = json_stream.load(f)
    for line in data:
        converted = json_stream.to_standard_types(line)

        if converted['uai'] in etablissements and converted['annee'] in etablissements[converted['uai']]:
            print('Duplicate UAI: ' + converted['uai'])
            print(converted)
            continue
        
        # remove null values
        converted = {k: v for k, v in converted.items() if v is not None}


        if converted['uai'] not in etablissements:
            etablissements[converted['uai']] = {}

        etablissements[converted['uai']][converted['annee']] = converted

print('Merging with annuaire ...')
with open('sources/fr-en-annuaire-education.json') as f:
    data = json_stream.load(f)
    for line in data:
        converted = json_stream.to_standard_types(line)

        # remove all null values
        converted = {k: v for k, v in converted.items() if v is not None}

        # merge
        if converted['identifiant_de_l_etablissement'] in etablissements:
            etablissements[converted['identifiant_de_l_etablissement']].update(converted)
            continue
        else:
            #print('Missing UAI: ' + converted['identifiant_de_l_etablissement'])
            #print(converted)
            continue

print("Final size: " + str(len(etablissements)))

# prepare geojson data
geojson = []

for uai in etablissements:
    etablissement = etablissements[uai]

    if 'latitude' in etablissement and 'longitude' in etablissement:

        # cleanup object before saving
        etablissement.pop('position', None)

        # Calcul de la couleur. taux_de_reussite_g pour les colleges ; taux_reu_total pour les lycees.
        couleur = None
        for year in range(annee_courante, annee_courante - 6, -1):
            year = str(year)
            if year in etablissement and 'taux_de_reussite_g' in etablissement[year]:
                # compute "color", from dark red to bright green, with value between 90 and 100
                couleur = float_to_color(etablissement[year]['taux_de_reussite_g'])
                break
            if year in etablissement and 'taux_reu_total' in etablissement[year]:
                # compute "color", from dark red to bright green, with value between 90 and 100
                couleur = float_to_color(etablissement[year]['taux_reu_total'])
                break

        if couleur is not None:
            etablissement['color'] = couleur

        geojson.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [etablissement['longitude'], etablissement['latitude']]
            },
            'properties': etablissement
        })

with open('docs/etablissements.json', 'wt', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=0)

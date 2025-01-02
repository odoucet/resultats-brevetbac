import json_stream
import json

# read sources/fr-en-indicateurs-valeur-ajoutee-colleges.json
# lazy loading to use less memory

# store etablissements (colleges + lycées)
etablissements = {}

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
        
        # todo: supprimer les champs inutiles

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
        
        # todo: supprimer les champs inutiles

        if converted['uai'] not in etablissements:
            etablissements[converted['uai']] = {}

        etablissements[converted['uai']][converted['annee']] = converted

print('Merging with annuaire ...')
with open('sources/fr-en-annuaire-education.json') as f:
    data = json_stream.load(f)
    for line in data:
        converted = json_stream.to_standard_types(line)

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

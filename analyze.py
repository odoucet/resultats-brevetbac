import json_stream

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

testdump = False
print('Merging with annuaire ...')
with open('sources/fr-en-annuaire-education.json') as f:
    data = json_stream.load(f)
    for line in data:
        converted = json_stream.to_standard_types(line)

        # merge
        if converted['identifiant_de_l_etablissement'] in etablissements:
            etablissements[converted['identifiant_de_l_etablissement']].update(converted)
            if not testdump:
                print(converted)
                testdump = True
            continue
        else:
            #print('Missing UAI: ' + converted['identifiant_de_l_etablissement'])
            #print(converted)
            continue

print("Final size: " + str(len(etablissements)))

# write csv file with tab separator
with open('etablissements.csv', 'w') as f:
    for key, value in etablissements.items():

        f.write(key)
        f.write('\t')
        # value is a dict
        for k, v in value.items():
            f.write(str(v))
            f.write('\t')
        f.write('\n')
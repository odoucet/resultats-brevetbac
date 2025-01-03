Carte des collèges et lycées français avec scores de réussite Brevet / BAC
======================================

Version interactive : https://odoucet.github.io/cartescolaire/


Installation locale
-------------------
- Téléchargez les trois fichiers ci-dessous au format JSON et mettez les dans le répertoire `sources` sans changer leur nom.
- Installez les dépendances python : `pip install -r requirements.txt`
- Lancez `analyze.py` : cela va regénérer le fichier docs/etablissements.json

Pour un usage local, vous devrez lancer un mini serveur web car sinon la page docs/index.html refuse de charger le JSON : 
```
python -m http.server 8000 --directory docs
# go to http://localhost:8000
```


Sources de données
-----------------
- Colleges :  https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-valeur-ajoutee-colleges/export/?disjunctive.uai&disjunctive.nom_de_l_etablissement&disjunctive.commune&disjunctive.departement&disjunctive.academie
```
# Sample
{
    "session": "2023", 
    "uai": "0010005A", 
    "nom_de_l_etablissement": "COLLEGE ROGER POULNARD", 
    "commune": "BAGE DOMMARTIN", 
    "departement": "AIN", 
    "academie": "LYON", 
    "secteur": "PU", 
    "nb_candidats_g": 127, 
    "taux_de_reussite_g": 93.0, 
    "va_du_taux_de_reussite_g": -2.0, 
    "nb_candidats_p": null, 
    "taux_de_reussite_p": null, 
    "note_a_l_ecrit_g": 12.4, 
    "va_de_la_note_g": 0.3, 
    "note_a_l_ecrit_p": null, 
    "taux_d_acces_6eme_3eme": 95.0, 
    "part_presents_3eme_ordinaire_total": 98.0, 
    "part_presents_3eme_ordinaire_g": null, 
    "part_presents_3eme_ordinaire_p": null, 
    "part_presents_3eme_segpa_total": null, 
    "nb_mentions_ab_g": 20, 
    "nb_mentions_b_g": 31, 
    "nb_mentions_tb_g": 50, 
    "nb_mentions_global_g": 101
}
```

- https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-de-resultat-des-lycees-gt_v2/export/?disjunctive.uai&disjunctive.secteur&disjunctive.libelle_commune&disjunctive.libelle_departement&disjunctive.libelle_academie&disjunctive.libelle_region&sort=num_ligne
```
{'num_ligne': 10520, 'annee': '2012',
'uai': '0480680D',
'libelle_uai': 'LYCEE SACRE-COEUR (GENERAL ET TECHNO.)',
'secteur': 'privé sous contrat',
'code_commune': '48140',
'libelle_commune': 'ST CHELY D APCHER',
'code_departement': '48',
'libelle_departement': 'LOZERE',
'libelle_academie': 'MONTPELLIER',
'code_region': '76',
'libelle_region': 'OCCITANIE',
'presents_total': 23, 'taux_reu_total': 100.0, 'va_reu_total': 8.0, 'taux_acces_2nde': 70.0, 'va_acces_2nde': 5.0, 'taux_men_total': None, 'va_men_total': None, 'presents_l': None, 'presents_es': None, 'presents_s': None, 'presents_gnle': None, 'presents_sti2d': None, 'presents_std2a': None, 'presents_stmg': None, 'presents_stl': None, 'presents_st2s': None, 'presents_s2tmd': None, 'presents_sthr': 23, 'taux_reu_l': None, 'taux_reu_es': None, 'taux_reu_s': None, 'taux_reu_gnle': None, 'taux_reu_sti2d': None, 'taux_reu_std2a': None, 'taux_reu_stmg': None, 'taux_reu_stl': None, 'taux_reu_st2s': None, 'taux_reu_s2tmd': None, 'taux_reu_sthr': '100',
'va_reu_l': None, 'va_reu_es': None, 'va_reu_s': None, 'va_reu_gnle': None, 'va_reu_sti2d': None, 'va_reu_std2a': None, 'va_reu_stmg': None, 'va_reu_stl': None, 'va_reu_st2s': None, 'va_reu_s2tmd': None, 'va_reu_sthr': '8',
'eff_2nde': 45, 'eff_1ere': 39, 'eff_term': None, 'taux_acces_1ere': '76',
'taux_acces_term': None, 'va_acces_1ere': '-5',
'va_acces_term': None, 'taux_men_l': None, 'taux_men_es': None, 'taux_men_s': None, 'taux_men_gnle': None, 'taux_men_sti2d': None, 'taux_men_std2a': None, 'taux_men_stmg': None, 'taux_men_stl': None, 'taux_men_st2s': None, 'taux_men_s2tmd': None, 'taux_men_sthr': None, 'va_men_l': None, 'va_men_es': None, 'va_men_s': None, 'va_men_gnle': None, 'va_men_sti2d': None, 'va_men_std2a': None, 'va_men_stmg': None, 'va_men_stl': None, 'va_men_st2s': None, 'va_men_s2tmd': None, 'va_men_sthr': None, 'nb_mentions_tb_avecf_g': None, 'nb_mentions_tb_sansf_g': None, 'nb_mentions_b_g': None, 'nb_mentions_ab_g': None, 'nb_mentions_tb_avecf_t': None, 'nb_mentions_tb_sansf_t': None, 'nb_mentions_b_t': None, 'nb_mentions_ab_t': None}
```

- https://data.education.gouv.fr/explore/dataset/fr-en-annuaire-education/export/?disjunctive.type_etablissement&disjunctive.libelle_academie&disjunctive.libelle_region&disjunctive.ministere_tutelle&disjunctive.appartenance_education_prioritaire&disjunctive.nom_commune&disjunctive.code_postal&disjunctive.code_departement
```
{
    'identifiant_de_l_etablissement': '0783774D',
    'nom_etablissement': 'Nouveau collège André Chénier',
    'type_etablissement': 'Collège',
    'statut_public_prive': 'Public',
    'adresse_1': 'Marcel Doret',
    'adresse_2': None, 
    'adresse_3': None, 
    'code_postal': '78200',
    'code_commune': '78361',
    'nom_commune': 'Mantes-la-Jolie',
    'code_departement': '078',
    'code_academie': '25',
    'code_region': '11',
    'ecole_maternelle': None, 
    'ecole_elementaire': None, 
    'voie_generale': '0',
    'voie_technologique': '0',
    'voie_professionnelle': '0',
    'telephone': '01 30 63 61 63',
    'fax': None,
    'web': 'https://bv.ac-versailles.fr/rechetab/0783774D-college-andre-chenier-nouveau-college-mantes-la-jolie.html',
    'mail': 'ce.0783774D@ac-versailles.fr',
    'restauration': 1, 
    'hebergement': 0, 
    'ulis': 0, 
    'apprentissage': '0',
    'segpa': '0',
    'section_arts': '0',
    'section_cinema': '0',
    'section_theatre': '0',
    'section_sport': '1',
    'section_internationale': '0',
    'section_europeenne': '0',
    'lycee_agricole': '0',
    'lycee_militaire': '0',
    'lycee_des_metiers': '0',
    'post_bac': '0',
    'appartenance_education_prioritaire': 'REP+',
    'greta': '1',
    'siren_siret': '20009522200010',
    'nombre_d_eleves': 590, 
    'fiche_onisep': 'https://www.onisep.fr/http/redirection/etablissement/slug/ENS.14382',
    'position': {'lon': 1.682758327166094, 'lat': 49.00116716280137}, 
    'type_contrat_prive': 'SANS OBJET',
    'libelle_departement': 'Yvelines',
    'libelle_academie': 'Versailles',
    'libelle_region': 'Ile-de-France',
    'coordx_origine': 603621.7, 
    'coordy_origine': 6878720.4, 
    'epsg_origine': 'EPSG:2154',
    'nom_circonscription': None, 
    'latitude': 49.00116716280137, 
    'longitude': 1.682758327166094, 
    'precision_localisation': 'Numéro de rue',
    'date_ouverture': '2021-06-01',
    'date_maj_ligne': '2024-12-31',
    'etat': 'OUVERT',
    'ministere_tutelle': "MINISTERE DE L'EDUCATION NATIONALE", 
    'multi_uai': 0, 
    'rpi_concentre': 0, 
    'rpi_disperse': None, 
    'code_nature': 340, 
    'libelle_nature': 'COLLEGE',
    'code_type_contrat_prive': '99',
    'pial': '0781977A',
    'etablissement_mere': None, 
    'type_rattachement_etablissement_mere': None, 
    'code_circonscription': None, 
    'code_zone_animation_pedagogique': None, 
    'libelle_zone_animation_pedagogique': None, 
    'code_bassin_formation': '25027',
    'libelle_bassin_formation': '078H-MANTES-LES MUREAUX'
}
```

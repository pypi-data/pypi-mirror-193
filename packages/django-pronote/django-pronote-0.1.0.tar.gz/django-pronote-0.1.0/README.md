# django-pronote
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django 3.x](https://img.shields.io/badge/django-3.2-blue.svg)](https://docs.djangoproject.com/en/3.2/)
[![Python CI](https://github.com/briefmnews/django-pronote/actions/workflows/tests.yaml/badge.svg)](https://github.com/briefmnews/django-pronote/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/briefmnews/django-pronote/branch/main/graph/badge.svg?token=4VYHI0VP2N)](https://codecov.io/gh/briefmnews/django-pronote)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Handle CAS login for Pronote (index éducation)

## Installation
Install from [PyPI](https://pypi.org/):
```
pip install django-pronote
```

Or, install with [pip](https://pypi.org/project/pip/):
```
pip install -e git://github.com/briefmnews/django-pronote.git@main#egg=pronote
```

## Setup
In order to make `django-pronote` works, you'll need to follow the steps below.

## Settings
First you need to add the following configuration to your settings:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'pronote',
    ...
)
```

### Mandatory settings
Here is the list of all the mandatory settings:
```python
PRONOTE_API_KEY
PRONOTE_RESSOURCE_ID
PRONOTE_TERMS_AND_CONDITIONS_URL
PRONOTE_RESSOURCE_TITLE
PRONOTE_URL
```

### Optional settings
The optional settings with their default values:
```python
PRONOTE_RESSOURCE_OLD_ID (default: None)
PRONOTE_PUBLISHER (default: None)
PRONOTE_RESSOURCE_TYPE (default: None)
PRONOTE_FAMILY_ID = (default: None)
PRONOTE_FAMILY_LABEL = (default: None)
PRONOTE_FAMILY_JUSTIFICATION = (default: None)
PRONOTE_PERSONAL_INFORMATION_DEFINITION_DATA = (default: ())
PRONOTE_PERSONAL_INFORMATION_DEFINITION_JUSTIFICATION = (default: [])
PRONOTE_PUBLIC = (default: ())
PRONOTE_PUBLIC_QUOTAS = (default: [])
PRONOTE_DISCIPLINES = (default: ())
PRONOTE_MEFSTAT11 = (default: ())
PRONOTE_URL_MOBILE_APP = (default: None)
PRONOTE_API_SUPPORT = (default: ())
PRONOTE_DESCRIPTION = (default: None)
PRONOTE_KEYWORDS = (default: ())
```

## Usage
Here is an example of output when running a GET method on `/catalogue/1234?apiKey=test` with the following settings:
```python
PRONOTE_API_KEY = "test"
PRONOTE_RESSOURCE_ID = "briefme"
PRONOTE_TERMS_AND_CONDITIONS_URL = "https://www.brief.me/gar/cgu/"
PRONOTE_RESSOURCE_TITLE = "Brief.me"
PRONOTE_URL = "https://www.brief.me"
PRONOTE_PUBLISHER = "Brief.me"
PRONOTE_RESSOURCE_TYPE = "Manuel"
PRONOTE_FAMILY_ID = "1234"
PRONOTE_FAMILY_LABEL = "test label"
PRONOTE_FAMILY_JUSTIFICATION = "hello"
PRONOTE_PERSONAL_INFORMATION_DEFINITION_DATA = (["Nom", "Prenom"], ["Prenom"])
PRONOTE_PERSONAL_INFORMATION_DEFINITION_JUSTIFICATION = ["test 0", "test 1"]
PRONOTE_PUBLIC = ("Professeur", "Elèves")
PRONOTE_PUBLIC_QUOTAS = ["2", "3"]
PRONOTE_DISCIPLINES = ("041400", "040600")
PRONOTE_MEFSTAT11 = ("10010012110", "21110010012")
PRONOTE_URL_MOBILE_APP = "http://hello.com"
PRONOTE_API_SUPPORT = ("ajoutPanier", "renduPJTAF")
PRONOTE_DESCRIPTION = "Un test de description"
PRONOTE_KEYWORDS = ("key 1",)
```

### Output
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rn:catalogueEtab xmlns:rn="http://www.index-education.com/RessourcesNumeriques" xmlns:ex="http://www.index-education.com/RessourcesNumeriques/ExchangeTypes" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.index-education.com/RessourcesNumeriques http://www.index-education.com/contenu/telechargement/partenaires/InterconnexionRessourcesNumeriquesV1_1.xsd" schemaVersion="1.1">
   <ex:catalogueVersion>1.0</ex:catalogueVersion>
   <ex:etabId>0133478Z</ex:etabId>
   <ex:ressource>
      <ex:id>9782701181431</ex:id>
      <ex:oldId>15264836</ex:oldId>
      <ex:familleId libelle="Famille resssources" justification="Justification corrélation multi-ressources">18ZE</ex:familleId>
      <ex:editeur>EDITEUR</ex:editeur>
      <ex:urlCgu>http://urlcgu</ex:urlCgu>
      <ex:titre>Histoire</ex:titre>
      <ex:genre>Manuel</ex:genre>
      <ex:definitionDcp ident="0" justification="Justification transfert DCP">
         <ex:dcp>Nom</ex:dcp>
         <ex:dcp>Prenom</ex:dcp>
      </ex:definitionDcp>
      <ex:definitionDcp ident="1" justification="Justification transfert DCP">
         <ex:dcp>Nom</ex:dcp>
         <ex:dcp>Prenom</ex:dcp>
         <ex:dcp>Classes</ex:dcp>
      </ex:definitionDcp>
      <ex:public identDefinitionDcp="0" quota="2">Professeur</ex:public>
      <ex:public identDefinitionDcp="1">Eleve</ex:public>
      <ex:matiereEnseignee>041400</ex:matiereEnseignee>
      <ex:matiereEnseignee>040600</ex:matiereEnseignee>
      <ex:mefstat11>10010012110</ex:mefstat11>
      <ex:mefstat11>21110010012</ex:mefstat11>
      <ex:url responsive="true">http://monurlderessource.php?idRessource=9782701181431</ex:url>
      <ex:urlAppliMobile>http://monurlderessourceAppliMobile.php?idRessource=9782701181431</ex:urlAppliMobile>
      <ex:apiSupport>ajoutPanier</ex:apiSupport>
      <ex:apiSupport>renduPJTAF</ex:apiSupport>
      <ex:description>description de la ressource</ex:description>
      <ex:keyword>keyword1</ex:keyword>
      <ex:keyword>keyword2</ex:keyword>
   </ex:ressource>
</rn:catalogueEtab>
```


## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```
pip install -r test_requirements.txt
```

To run testing locally:
```
pytest
```
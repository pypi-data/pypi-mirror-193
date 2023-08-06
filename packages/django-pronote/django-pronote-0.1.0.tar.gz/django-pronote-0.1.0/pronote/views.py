from rest_framework.views import APIView
from rest_framework.response import Response

from .authentication import QueryStringAuthentication
from .renderers import XMLRenderer
from .settings import *


class PronoteCatalogue(APIView):
    authentication_classes = (QueryStringAuthentication,)
    renderer_classes = (XMLRenderer,)

    def get(self, request, uai, format=None):
        catalogue = {
            "catalogueVersion": "1.0",
            "etabId": uai,
            "ressource": {
                "id": RESSOURCE_ID,
                "urlCgu": TERMS_AND_CONDITIONS_URL,
                "titre": RESSOURCE_TITLE,
                "genre": RESSOURCE_TYPE,
                "url": URL,
            },
        }

        optional_fields = {
            "oldId": RESSOURCE_OLD_ID,
            "editeur": PUBLISHER,
            "familleId": FAMILY_ID,
            "definitionDcp": PERSONAL_INFORMATION_DEFINITION_DATA,
            "public": PUBLIC,
            "matiereEnseignee": DISCIPLINES,
            "mefstat11": MEFSTAT11,
            "urlAppliMobile": URL_MOBILE_APP,
            "apiSupport": API_SUPPORT,
            "description": DESCRIPTION,
            "keyword": KEYWORDS,
        }

        catalogue["ressource"] |= {
            key: val for key, val in optional_fields.items() if val
        }

        return Response(catalogue)

from django.conf import settings

# mandatory settings
RESSOURCE_ID = getattr(settings, "PRONOTE_RESSOURCE_ID")
TERMS_AND_CONDITIONS_URL = getattr(settings, "PRONOTE_TERMS_AND_CONDITIONS_URL")
RESSOURCE_TITLE = getattr(settings, "PRONOTE_RESSOURCE_TITLE")
URL = getattr(settings, "PRONOTE_URL")

# optional settings
RESSOURCE_OLD_ID = getattr(settings, "PRONOTE_RESSOURCE_OLD_ID", None)
RESSOURCE_TYPE = getattr(settings, "PRONOTE_RESSOURCE_TYPE")
FAMILY_ID = getattr(settings, "PRONOTE_FAMILY_ID", None)
FAMILY_ATTRIBUTES = {
    "libelle": getattr(settings, "PRONOTE_FAMILY_LABEL", None),
    "justification": getattr(settings, "PRONOTE_FAMILY_JUSTIFICATION", None),
}
PUBLISHER = getattr(settings, "PRONOTE_PUBLISHER", None)
PERSONAL_INFORMATION_DEFINITION_ATTRIBUTES = [
    {
        "ident": str(i),
        "justification": el,
    }
    for i, el in enumerate(
        getattr(settings, "PRONOTE_PERSONAL_INFORMATION_DEFINITION_JUSTIFICATION", None)
    )
]
PERSONAL_INFORMATION_DEFINITION_DATA = getattr(
    settings, "PRONOTE_PERSONAL_INFORMATION_DEFINITION_DATA", []
)
PUBLIC = getattr(settings, "PRONOTE_PUBLIC", ())
PUBLIC_ATTRIBUTES = [
    {"identDefinitionDcp": str(i), "quota": el}
    for i, el in enumerate(getattr(settings, "PRONOTE_PUBLIC_QUOTAS", []))
]
DISCIPLINES = getattr(settings, "PRONOTE_DISCIPLINES", ())
MEFSTAT11 = getattr(settings, "PRONOTE_MEFSTAT11", ())
URL_ATTRIBUTES = (
    {"responsive": "true"}
    if getattr(settings, "PRONOTE_RESPONSIVE_WEBSITE", True)
    else {}
)
URL_MOBILE_APP = getattr(settings, "PRONOTE_URL_MOBILE_APP", None)
API_SUPPORT = getattr(settings, "PRONOTE_API_SUPPORT", ())
DESCRIPTION = getattr(settings, "PRONOTE_DESCRIPTION", None)
KEYWORDS = getattr(settings, "PRONOTE_KEYWORDS", ())

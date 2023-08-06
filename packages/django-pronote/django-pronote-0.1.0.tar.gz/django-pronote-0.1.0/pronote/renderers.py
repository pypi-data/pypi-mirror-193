from io import StringIO

from django.utils.encoding import force_str
from django.utils.xmlutils import SimplerXMLGenerator
from rest_framework.renderers import BaseRenderer

from .settings import (
    FAMILY_ATTRIBUTES,
    PERSONAL_INFORMATION_DEFINITION_ATTRIBUTES,
    PUBLIC_ATTRIBUTES,
    URL_ATTRIBUTES,
)


class XMLRenderer(BaseRenderer):
    media_type = "application/xml"
    format = "xml"
    root_tag_name = "rn:catalogueEtab"
    item_tag_name = "ex:dcp"
    attributes_mapping = {
        "familleId": FAMILY_ATTRIBUTES,
        "definitionDcp": PERSONAL_INFORMATION_DEFINITION_ATTRIBUTES,
        "public": PUBLIC_ATTRIBUTES,
        "url": URL_ATTRIBUTES,
    }

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ""

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(
            self.root_tag_name,
            {
                "xmlns:rn": "http://www.index-education.com/RessourcesNumeriques",
                "xmlns:ex": "http://www.index-education.com/RessourcesNumeriques/ExchangeTypes",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": "http://www.index-education.com/RessourcesNumeriques http://www.index-education.com/contenu/telechargement/partenaires/InterconnexionRessourcesNumeriquesV1_1.xsd",
                "schemaVersion": "1.1",
            },
        )

        self._to_xml(xml, data)

        xml.endElement(self.root_tag_name)
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (tuple, list)):
            for item in data:
                xml.startElement(self.item_tag_name, {})
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)

        elif isinstance(data, dict):
            for key, value in data.items():
                prefixed_key = f"ex:{key}"
                if isinstance(value, tuple):
                    for i, item in enumerate(value):
                        xml.startElement(prefixed_key, self._add_attributes(key, i))
                        self._to_xml(xml, item)
                        xml.endElement(prefixed_key)
                else:
                    xml.startElement(prefixed_key, self._add_attributes(key))
                    self._to_xml(xml, value)
                    xml.endElement(prefixed_key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_str(data))

    def _add_attributes(self, key, index=None):
        if key in self.attributes_mapping.keys():
            if isinstance(self.attributes_mapping[key], list):
                return {
                    key: val
                    for key, val in self.attributes_mapping[key][index].items()
                    if val
                }
            else:
                return {
                    key: val for key, val in self.attributes_mapping[key].items() if val
                }
        return {}

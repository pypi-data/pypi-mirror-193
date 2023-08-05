from enum import Enum
from xml.etree import ElementTree
import pydantic

class LineUnitCode(Enum):
    ADET: str = "NIU"

class InvoiceLine(pydantic.BaseModel):
    sira_no: str
    hizmet_adi: str
    miktar_turu: LineUnitCode
    
    miktar: float
    birim_fiyat: float
    mal_hizmet_tutari: float
    
    para_birimi: str = "TRY"
    
    def xml(self) -> ElementTree.Element:
        parent = ElementTree.Element("cac:InvoiceLine")
        ElementTree.SubElement(parent, "cbc:ID").text = self.sira_no
        ElementTree.SubElement(parent, "cbc:InvoicedQuantity", attrib={"unitCode": self.miktar_turu.value}).text = str(self.miktar)
        ElementTree.SubElement(parent, "cbc:LineExtensionAmount", attrib={"currencyID": self.para_birimi}).text = str(self.mal_hizmet_tutari)
        
        item_element = ElementTree.SubElement(parent, "cac:Item")
        ElementTree.SubElement(item_element, "cbc:Name").text = self.hizmet_adi
        
        price_element = ElementTree.SubElement(parent, "cac:Price")
        ElementTree.SubElement(price_element, "cbc:PriceAmount", attrib={"currencyID":self.para_birimi}).text = str(self.birim_fiyat)
        
        return parent
    
    """def xml(self):
        with open("./xml_templates/invoice_line.xml") as f:
            template = f.read()
        new_xml_string = replace_all(
            template,
            {
                "__SIRA_NO__": self.sira_no,
                "__MIKTAR_TURU__": self.miktar_turu,
                "__MIKTAR__": self.miktar,
                "__PARA_BIRIMI__": self.para_birimi,
                "__MAL_HIZMET_TUTARI__": self.mal_hizmet_tutari,
                "__HIZMET_ADI__": self.hizmet_adi,
                "__BIRIM__FIYAT__": self.birim_fiyat
            }
        )
        return new_xml_string"""
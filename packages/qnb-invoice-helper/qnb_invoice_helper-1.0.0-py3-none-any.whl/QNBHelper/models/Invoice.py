import datetime
from enum import Enum
from typing import List, Optional
import uuid
from xml.etree import ElementTree
import pydantic
from QNBHelper.models.Accounting import Accounting, AccountingType
from QNBHelper.models.InvoiceLine import InvoiceLine
from QNBHelper.models.Note import Note
from QNBHelper.models.Tax import TaxTotal
from QNBHelper.models.LegalMonetaryTotal import LegalMonetaryTotal

class InvoiceType(Enum):
    SATIS: str = "SATIS"
    IHRAC_KAYITLI: str = "IHRACKAYITLI"
    TEVKIFAT: str = "TEVKIFAT"
    IADE: str = "IADE"
    ISTISNA: str = "ISTISNA"
    
class InvoiceSendingType(Enum):
    KAGIT: str = "KAGIT"
    ELEKTRONIK: str = "ELEKTRONIK"
    
class Invoice(pydantic.BaseModel):
    accounting_supplier: Accounting
    accounting_customer: Accounting
    tax_total: TaxTotal
    legal_monetary_total: LegalMonetaryTotal
    lines: List[InvoiceLine]
    notlar: List[Note]
    para_birimi: str
    
    fatura_turu: InvoiceType = InvoiceType.SATIS
    gonderim_sekli: InvoiceSendingType = InvoiceSendingType.ELEKTRONIK
    
    asil_veya_suret: bool = False
    
    fatura_no: Optional[str]
    uuid4: str = str(uuid.uuid4())
    _belgeFormati: str = "UBL"
    _date_now: datetime.datetime = datetime.datetime.now()
    
    @pydantic.root_validator
    def check_valid_accounting_types(cls, data):
        if data["accounting_supplier"].type != AccountingType.Supplier:
            raise ValueError("accounting_supplier type'ı Supplier Olan Accounting Class'ı Olmak Zorunda!")
        
        if data["accounting_customer"].type != AccountingType.Customer:
            raise ValueError("accounting_customer type'ı Customer Olan Accounting Class'ı Olmak Zorunda!")
        return data
    
    @property
    def xml_namespaces(self) -> dict:
        namespaces={
            "xmlns":"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
            "xmlns:cac":"urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "xmlns:cbc":"urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "xmlns:ccts":"urn:un:unece:uncefact:documentation:2",
            "xmlns:ds":"http://www.w3.org/2000/09/xmldsig#",
            "xmlns:ext":"urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "xmlns:qdt":"urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2",
            "xmlns:ubltr":"urn:oasis:names:specification:ubl:schema:xsd:TurkishCustomizationExtensionComponents", 
            "xmlns:udt":"urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2",
            "xmlns:xades":"http://uri.etsi.org/01903/v1.3.2#",
            "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation":"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 UBL-Invoice-2.1.xsd"
        }
        return namespaces
    
    @property
    def duzenleme_tarihi(self):
        duzenleme_tarihi = self._date_now.strftime("%Y-%m-%d")
        return duzenleme_tarihi
    
    @property
    def duzenleme_zamani(self):
        duzenleme_zamani = self._date_now.strftime("%H:%M:%S")
        return duzenleme_zamani
    

    def xml(self):
        namespaces = self.xml_namespaces
        root = ElementTree.Element("Invoice", attrib=namespaces)
        ElementTree.SubElement(root, "cbc:UBLVersionID").text = "2.1"
        ElementTree.SubElement(root, "cbc:CustomizationID").text = "TR1.2"
        ElementTree.SubElement(root, "cbc:ProfileID").text = "EARSIVFATURA"
        ElementTree.SubElement(root, "cbc:UUID").text = self.uuid4
        ElementTree.SubElement(root, "cbc:IssueDate").text = self.duzenleme_tarihi
        ElementTree.SubElement(root, "cbc:IssueTime").text = self.duzenleme_zamani
        ElementTree.SubElement(root, "cbc:InvoiceTypeCode").text = self.fatura_turu.value
        ElementTree.SubElement(root, "cbc:DocumentCurrencyCode").text = self.para_birimi
        ElementTree.SubElement(root, "cbc:LineCountNumeric").text = str(len(self.lines))
        ElementTree.SubElement(root, "cbc:Note").text = f"Gönderim Şekli: {self.gonderim_sekli.value}"
        ElementTree.SubElement(root, "cbc:CopyIndicator").text = str(self.asil_veya_suret).lower()
        
        for note in self.notlar:
            root.append(note.xml())
        
        root.append(self.accounting_supplier.xml())
        root.append(self.accounting_customer.xml())    
        root.append(self.tax_total.xml())
        root.append(self.legal_monetary_total.xml())
        for line in self.lines:
            root.append(line.xml())

        return root

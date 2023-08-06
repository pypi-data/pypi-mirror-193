
# from bundleb2b_api_management.bundleb2b_api_management.company import company_initalized_values
from dataclasses import dataclass
from bundleb2b_api_management.bundleb2b_api_management.dataclass_functions import Pagination, from_int, from_bool, from_datetime, from_dict, from_float, from_list, from_none, from_str, from_union, to_class, to_enum, to_float, is_type
from typing import List, Any, Optional
from enum import Enum
from bundleb2b_api_management.bundleb2b_api_management.settings import _bundleb2b_api_path
from bundleb2b_api_management.bundleb2b_api_management.user import User
from requests import Session, HTTPError, Response
from retry import retry
import logging

logger = logging.getLogger()





@dataclass
class ExtraField:
    fieldName: str
    fieldValue: str

    @staticmethod
    def from_dict(obj: Any) -> 'ExtraField':
        _fieldName = str(obj.get("fieldName"))
        _fieldValue = str(obj.get("fieldValue"))
        return ExtraField(_fieldName, _fieldValue)

class CompanyStatus(Enum):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2
    INACTIVE = 3
    DELETED = 4


@dataclass
class Company:
    company_id: Optional[int] = None
    company_name: Optional[str] = None
    bc_group_name: Optional[str] = None
    company_status: Optional[int] = None
    catalog_id: Optional[int] = None # Price List ID
    catalog_name: Optional[str] = None # Price List Name
    company_email: Optional[str] = None
    company_phone_number: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None
    extra_fields: Optional[List[ExtraField]] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    uuid: Optional[str] = None
    bc_group_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        assert isinstance(obj, dict)
        company_id = from_union([from_none, from_int], obj.get("companyId"))
        company_name = from_union([from_none, from_str], obj.get("companyName"))
        bc_group_name = from_union([from_none, from_str], obj.get("bcGroupName"))
        company_status = from_union([from_none, from_int], obj.get("companyStatus"))
        catalog_id = from_union([from_none, from_int], obj.get("catalogId"))
        catalog_name = from_union([from_str, from_none], obj.get("catalogName"))
        company_email = from_union([from_str, from_none], obj.get("companyEmail"))
        company_phone_number = from_union([from_str, from_none], obj.get("companyPhone"))
        address_line1 = from_union([from_str, from_none], obj.get("addressLine1"))
        address_line2 = from_union([from_str, from_none], obj.get("addressLine2"))
        city = from_union([from_str, from_none], obj.get("city"))
        state = from_union([from_str, from_none], obj.get("state"))
        country = from_union([from_str, from_none], obj.get("country"))
        zip_code = from_union([from_none, from_str], obj.get("zipCode"))
        extra_fields = from_union([lambda x: from_list(ExtraField.from_dict, x), from_none], obj.get("extraFields"))
        created_at = from_union([from_none, from_int], obj.get("createdAt"))
        updated_at = from_union([from_none, from_int], obj.get("updatedAt"))
        uuid = from_union([from_none, from_str], obj.get("uuid"))
        bc_group_id = from_union([from_none, from_str], obj.get("bcGroupId"))

        return Company(company_id=company_id
                       ,company_name=company_name
                       ,bc_group_name=bc_group_name,company_status=company_status,catalog_id=catalog_id
                       ,catalog_name=catalog_name,company_email=company_email
                       ,company_phone_number=company_phone_number,address_line1=address_line1
                       ,address_line2=address_line2,city=city,state=state,zip_code=zip_code,country=country
                       ,extra_fields=extra_fields
                       ,created_at=created_at,updated_at=updated_at, uuid=uuid,bc_group_id=bc_group_id
                    )

    def to_dict(self) -> dict:
        result: dict = {}
        if (self.company_id):
            result["companyId"] = from_union([from_str, from_none], self.company_id)
        if (self.company_name):
            result["companyName"] = from_union([from_str, from_none], self.company_name)
        if (self.bc_group_name):
            result["bcGroupName"] = from_union([from_str, from_none], self.bc_group_name)
        if (self.company_status):
            result["companyStatus"] = from_union([from_int, from_none], self.company_status)
        if (self.catalog_id):
            result["catalogId"] = from_union([from_int, from_none], self.catalog_id)
        if (self.catalog_name):
            result["catalogName"] = from_union([from_str, from_none], self.catalog_name)
        if (self.company_email):
            result["companyEmail"] = from_union([from_str, from_none], self.company_email)
        if (self.company_phone_number):
            result["companyPhone"] = from_union([from_str, from_none], self.company_phone_number)
        if (self.address_line1):
            result["addressLine1"] = from_union([from_str, from_none], self.address_line1)
        if (self.address_line2):
            result["addressLine2"] = from_union([from_str, from_none], self.address_line2)
        if (self.city):
            result["city"] = from_union([from_str, from_none], self.city)
        if (self.state):
            result["state"] = from_union([from_str, from_none], self.state)
        if (self.country):
            result["country"] = from_union([from_str, from_none], self.country)
        if (self.zip_code):
            result["zipCode"] = from_union([from_str, from_none], self.zip_code)
        if (self.extra_fields):
            result["extraFields"] = from_union([lambda x: from_list(lambda x: to_class(ExtraField, x), x), from_none], self.extra_fields)
        if (self.created_at):
            result["createdAt"] = from_union([from_int, from_none], self.created_at)
        if (self.updated_at):
            result["updatedAt"] = from_union([from_int, from_none], self.updated_at)
        if (self.uuid):
            result["uuid"] = from_union([from_str, from_none], self.uuid)
        if (self.bc_group_id):
            result["bcGroupId"] = from_union([from_int, from_none], self.bc_group_id)
        return result

@dataclass
class Companies:
    code: Optional[int] = None # response code
    companies: Optional[List[Company]] = None
    pagination: Optional[Pagination] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Companies':
        assert isinstance(obj, dict)
        meta = obj.get('meta')
        assert isinstance(meta,dict)
        code = from_union([from_int, from_none], obj.get("code"))
        companies = from_union([lambda x: from_list(Company.from_dict, x), from_none], obj.get("data"))
        pagination = from_union([Pagination.from_dict, from_none], meta.get("pagination"))
        return Companies(code=code, companies=companies, pagination=pagination)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["companies"] = from_union([lambda x: from_list(lambda x: to_class(Company, x), x), from_none], self.companies)
        result["pagination"] = from_union([lambda x: to_class(Pagination, x), from_none], self.pagination)
        return result

@retry(exceptions=HTTPError,tries=5,delay=20,logger=logger)
def get_companies(session : Session, **kwargs) -> Companies:
    """ Returns companies
    
    https://bundleb2b.stoplight.io/docs/openapi/bd60ac4e8b381-get-companies

    """
    url = f'{_bundleb2b_api_path}/companies'
    params = {}
    for key, value in kwargs.items():
        k = key.replace("__",":")
        params[k] = value
    
    try:
        s = session.get(url,params=params)
        s.raise_for_status()
        return Companies.from_dict(s.json())
    except HTTPError as e:
        raise(e)
    except Exception as e:
        raise(e)

@retry(exceptions=HTTPError,tries=5,delay=20,logger=logger)
def get_company_by_bizowie_customer_id(session:Session,bizowie_customer_id:str,**kwargs) -> Optional[Company]:
    """ Returns a single company
    if multiple companies match, it returns the first match
    
    https://bundleb2b.stoplight.io/docs/openapi/bd60ac4e8b381-get-companies

    """

    url = f'{_bundleb2b_api_path}/companies?extraFields=Customer%20ID:{bizowie_customer_id}'
    params = {}
    for key, value in kwargs.items():
        k = key.replace("__",":")
        params[k] = value

    try:
        result = session.get(url)
        result.raise_for_status()
        companies = Companies.from_dict(result.json())
        if(len(companies.companies)>0):
            return companies.companies[0]
        else:
            return None
    except HTTPError as e:
        raise(e)
    except Exception as e:
        raise(e)

def create_company(session:Session,company:Company,adminUser:User,send_welcome_email=True) -> Response:
    url = f'{_bundleb2b_api_path}/companies'

    if(company.company_name is None or company.company_phone_number is None):
        raise Exception('Required company field missing. Name or Phone')
    if(adminUser.first_name is None or adminUser.last_name is None or adminUser.email is None):
        raise Exception('Required user field missing. First Name, Last Name, or Email')
    
    # Default values
    if(company.country is None):
        company.country = 'US'
    if(company.company_email is None):
        company.company_email = adminUser.email
    
    if(company.catalog_id is None):
        logger.warn('Missing catalog_id on company. Pricing Tier will need to be updated manually')

    temp_body = {
        'companyName':company.company_name,
        'companyPhone':company.company_phone_number,
        'companyEmail':company.company_email,
        'addressLine1':company.address_line1,
        'addressLine2':company.address_line2,
        'city':company.city,
        'state':company.state,
        'country':company.country,
        'zipCode':company.zip_code,
        'adminFirstName':adminUser.first_name,
        'adminLastName':adminUser.last_name,
        'adminEmail':adminUser.email,
        'adminPhoneNumber':adminUser.phone_number,
        'catalogId':company.catalog_id,
        'acceptCreationEmail':send_welcome_email,
        'channelIds':None,
        'originChannelId':None,
        'extraFields':company.extra_fields,
        'userExtraFields':None
    }

    body = {}
    for key,value in temp_body.items():
        if(value):
            body[key] = value


    try:
        s = session.post(url,json=body)
        s.raise_for_status()
        return s
    except HTTPError as e:
        raise(e)
    except Exception as e:
        raise(e)
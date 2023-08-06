from requests import Session, HTTPError, ConnectionError, RequestException,ConnectTimeout,ReadTimeout,Timeout, Response
from dataclasses import dataclass
from bundleb2b_api_management.bundleb2b_api_management.dataclass_functions import Pagination, from_int, from_bool, from_datetime, from_dict, from_float, from_list, from_none, from_str, from_union, to_class, to_enum, to_float, is_type
from typing import List, Any, Optional
from enum import Enum
from bundleb2b_api_management.bundleb2b_api_management.settings import _bundleb2b_api_path
from retry import retry
import logging

logger = logging.getLogger()



@dataclass
class User:
    id: Optional[int] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    role: Optional[int] = 0
    customer_id: Optional[int] = None
    company_id: Optional[int] = None
    uuid: Optional[str] = None

    # handle default values
    def __post_init__(self):
        if(self.role is None):
            self.role = 0

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        created_at = from_union([from_int, from_none], obj.get("createdAt"))
        updated_at = from_union([from_int, from_none], obj.get("updatedAt"))
        first_name = from_union([from_str, from_none], obj.get("firstName"))
        last_name = from_union([from_str, from_none], obj.get("lastName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone_number = from_union([from_none, lambda x: from_str(x)], obj.get("phoneNumber"))
        role = from_union([from_int, from_none], obj.get("role"))
        customer_id = from_union([from_int, from_none], obj.get("customerId"))
        company_id = from_union([from_int, from_none], obj.get("companyId"))
        uuid = from_union([from_str, from_none], obj.get("uuid"))
        return User(id=id, role=role, created_at=created_at, updated_at=updated_at
                    , phone_number=phone_number, first_name=first_name, last_name=last_name
                    , email=email, customer_id=customer_id, company_id=company_id, uuid=uuid)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id:
            result["id"] = from_union([from_int, from_none],self.id)
        if self.created_at:
            result["createdAt"] = from_union([from_int, from_none],self.created_at)
        if self.updated_at:
            result["updatedAt"] = from_union([from_int, from_none],self.updated_at)
        if self.first_name:
            result["firstName"] = from_union([from_str, from_none], self.first_name)
        if self.last_name:
            result["lastName"] = from_union([from_str, from_none], self.last_name)
        if self.email:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone_number:
            result["phoneNumber"] = from_union([from_str, from_none],self.phone_number)
        if self.role is not None:
            result["role"] = from_union([from_int, from_none],self.role)
        if self.customer_id:
            result["customerId"] = from_union([from_int, from_none],self.customer_id)
        if self.company_id:
            result["companyId"] = from_union([from_int, from_none],self.company_id)
        if self.uuid:
            result["uuid"] = from_union([from_int, from_none],self.uuid)
        return result
    

@dataclass
class Users:
    code: Optional[int] = None # response code
    user: Optional[List[User]] = None
    pagination: Optional[Pagination] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Users':
        assert isinstance(obj, dict)
        meta = obj.get('meta')
        assert isinstance(meta,dict)
        user= None
        code = from_union([from_int, from_none], obj.get("code"))
        user = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("data"))
        pagination = from_union([Pagination.from_dict, from_none], meta.get("pagination"))
        return Users(code=code, user=user, pagination=pagination)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user is not None:
            result["Users"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none], self.user)
        if self.pagination is not None:
            result["pagination"] = from_union([lambda x: to_class(Pagination, x), from_none], self.pagination)
        return result

@retry(exceptions=HTTPError,tries=5,delay=20,logger=logger)
def get_user_list(session : Session, **kwargs) -> Users:
    """ Returns users
    
    https://bundleb2b.stoplight.io/docs/openapi/8f5b5d1babbcd-get-users

    """
    url = f"{_bundleb2b_api_path}users"
    params = {}
    for key, value in kwargs.items():
        k = key.replace("__",":")
        params[k] = value

    try:
        s = session.get(url,params=params)
        s.raise_for_status()
        data = s.json()
        return Users.from_dict(data)
    except HTTPError as e:
        raise(e)
    except Exception as e:
        raise(e)
    
@retry(exceptions=HTTPError,tries=5,delay=20,logger=logger)
def create_user(session : Session, user : User, send_welcome_email : bool = True) -> Response:
    """
    """
    try:
        url = f"{_bundleb2b_api_path}users"
        body = user.to_dict()
        if(send_welcome_email):
            body['acceptWelcomeEmail'] = True
        s = session.post(url,json=body)
        s.raise_for_status()
        return s
    except HTTPError as e:
        raise(e)
    except Exception as e:
        raise(e)
    
    

    # resp = session.post(url, json=user.to_dict())
from pydantic import BaseModel, field_validator, EmailStr
from .validation import (
    username_validation,
    password_validation,
    email_validation,
    mobile_no_validation,
    name_validation,
    age_validation,
    user_type_validation
    
)
import re , datetime

class User_signup(BaseModel):
    username : str
    password : str 
    email : str
    mobile_no : str
    name : str
    age : str
    user_type :str

    @field_validator("username")
    @classmethod
    def username_validate_signup(cls,value):
        return username_validation(value)
    
    @field_validator("password")
    @classmethod
    def password_validate_signup(cls,value):
        return password_validation(value)
    
    @field_validator("email")
    @classmethod
    def email_validate_signup(cls,value):
        return email_validation(value)
    
    @field_validator("mobile_no")
    @classmethod
    def mobile_no_validate_signup(cls,value):
        return mobile_no_validation(value)
    
    @field_validator("name")
    @classmethod
    def name_validate_signup(cls,value):
        return name_validation(value)
    
    @field_validator("age")
    @classmethod
    def age_validate_signup(cls,value):
        return age_validation(value)
    
    @field_validator("user_type")
    @classmethod
    def user_type_validate_signup(cls,value):
        return user_type_validation(value)

class user_login(BaseModel):
    email : str
    password : str

class update_user(BaseModel):
    username : str | None = None
    name : str | None = None 
    email : str | None = None
    mobile_no : str | None = None 
    age : str | None = None 

    @field_validator("username")
    @classmethod
    def username_validate_update(cls,value):
        if value is None:
            return value
        return username_validation(value)

    @field_validator("name")
    @classmethod
    def name_validate_update(cls,value):
        if value is None :
            return value
        return name_validation(value) 
    
    @field_validator("email")
    @classmethod
    def email_validate_update(cls,value):
        if value is None :
            return value
        return email_validation(value)
    
    @field_validator("mobile_no")
    @classmethod
    def mobile_no_validate_update(cls,value):
        if value is None :
            return value
        return mobile_no_validation(value)
    
    @field_validator("age")
    @classmethod
    def age_validate_update(cls,value):
        if value is None :
            return value
        return age_validation(value)
    

class show_user_details_for_admin(BaseModel):
    id : int
    name : str
    username : str
    email : str
    mobile_no :str
    age : str
    created_at : datetime
    updated_at : datetime
    active_status : str 

    class config:
        orm_mode = True

class show_user_details_to_user(BaseModel):
    id : int 
    name : str 
    age : str
    username : str
    email : str 
    mobile_no : str
    created_at : datetime

class showtoken (BaseModel):
    access_token : str
    token_type : str
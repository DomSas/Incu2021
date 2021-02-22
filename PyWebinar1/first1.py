import pytest

def u_will_get_vaccine(birthyear: int):
    if(birthyear < 1941):
        return True
    else:
        return False
    
def tests_u_will_get_vaccine():
    x = u_will_get_vaccine(1920)
    assert x == True

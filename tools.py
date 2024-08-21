def parseBoolean(boolean):
    if isinstance(boolean, str):
        boolean = boolean.lower()
    
    my_boolean = {
        "true": True,
        "1": True,
        "false": False,
        "0": False
    }
    
    return my_boolean.get(boolean, False)

COMMON = 'common'

def isEmpty(obj, type=COMMON):
    empty_values = {
        "common": ['', None, "0001-01-01", "0001-01-01T00:00:00Z"],
        "zero": ['', None, 0, "0"],
        "null": ['', None, "null"],
        "undefined": ['', None, "null", "undefined"],
    }

    empty = empty_values.get(type, empty_values[COMMON])

    if obj in empty:
        return True

    if isinstance(obj, dict):
        return len(obj) == 0

    return False
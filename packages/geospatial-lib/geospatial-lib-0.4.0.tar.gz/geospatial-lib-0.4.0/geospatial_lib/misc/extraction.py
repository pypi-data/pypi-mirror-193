import re
from typing import Dict, List


def str_to_dict_from_regex(str_value: str, regex: str) -> List[Dict]:
    r = re.compile(regex)
    return [m.groupdict() for m in r.finditer(str_value)]
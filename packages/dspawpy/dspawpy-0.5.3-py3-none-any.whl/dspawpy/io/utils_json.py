# -*- coding: utf-8 -*-
import re
from typing import List

def get_lines_without_comment(filename:str,comment:str="#")->List[str]:
    lines = []
    with open(filename) as file:
        while True:
            line = file.readline()
            if line:
                line = re.sub(comment + r'.*$', "", line) # remove comment
                line = line.strip()
                if line:
                    lines.append(line)
            else:
                break

    return lines


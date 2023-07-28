import re
import random

def completeName(expression):
    return expression["text"]["selfname"] + " " + expression["firstname"] + " " + expression["surname"]

def find_replace(expression):
    newExpression = expression["text"]["introduction"]
    regex = r"\{([^}]+)\}"
    ocurrences = re.findall(regex, newExpression)

    for founds in ocurrences:
        newExpression = str(newExpression).replace(
            f"{founds}", 
            str(founds).split("|")[random.randint(0, len(str(founds).split("|")) - 1)]
        ).replace("{","").replace("}","")

    return completeName(expression) + " " + newExpression + " " + expression["text"]["working_since"]
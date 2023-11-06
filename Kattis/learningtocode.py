import re
import shelve

variables = shelve.open("variables")

def parse_template(s: str):
    s = re.sub(r"^`(.*)`$", r"\1", s).replace("${`", "").replace("`}", "").replace("${\"", "").replace("\"}", "")
    pattern = r"\$\{(.+?)\}"
    s = re.sub(pattern, lambda m: variables[m.group(1)], s)
    # for match in re.findall(pattern, s):
    #     s = s.replace("${match}", variables[match])
    return s

def parse_value(value: str):
    if value.startswith("`"):
        value = parse_template(value)
    elif value.startswith("\""):
        value = re.sub(r"^\"(.*)\"$", r"\1", value)
    else:
        value = variables[value]
    return value

while True:
    s = input()
    if s == "end.":
        break
    if s.startswith("var"):
        name,value = s.replace("var ", "", 1).replace(";", "").split(" = ", 1)
        value = parse_value(value)
        variables[name] = value
        # print(f'--- Set {name} to "{value}"')
    elif s.startswith("print"):
        value = s.replace("print ", "", 1).replace(";", "")
        print(parse_value(value))

variables.close()

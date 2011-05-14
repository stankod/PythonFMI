import re

def reg_ex_or(first, *args):
    rslt = first
    for reg_ex in args:
        rslt += '|' + reg_ex
    return rslt

reg_ex = dict()
reg_ex['string']     = r'".*?"'
reg_ex['special']    = r'[!\$%&\*\+\-\./:<=>\?@\^_~]'
reg_ex['number']     = r'\d+\.\d+|\d+\.|\.\d+|\d+'
reg_ex['name']       = r'\b[a-zA-Z][\w' + reg_ex['special'][1:-1] + r']*'
reg_ex['braces']     = r'[()]'
reg_ex['bools']      = r'#[tf]'
reg_ex['quote']      = r'\''
reg_ex['identifier'] = reg_ex['name'] + '|' + reg_ex['special']
reg_ex['token']      = reg_ex_or(*reg_ex.values())


def is_identifier(str):    
    return re.match(reg_ex['identifier']+'$', str) != None

def is_name(str):
    return re.match(reg_ex['name'] + '$', str) != None

def tokenize(line):
    return re.findall(reg_ex['token'], line)


def identifiers_list(tokens):
    return list(filter(is_identifier, tokens))


def identifiers(tokens):
    return set([x.lower() for x in identifiers_list(tokens)])

def case_sensitive(code, identifiers_set=set()):
    tokens = tokenize(code)
    names = list(filter(is_name, tokens))
    rsltCode = code[:]

    id_replacements = {x:x.lower() for x in names}

    for name in names:
        for template in identifiers_set:
            print('{0}, {1}'.format(name, template))
            if name.lower() == template.lower():
                id_replacements[name] = template

    for name,repl in id_replacements.items():
        rsltCode = rsltCode.replace(name,repl)
        
    return rsltCode

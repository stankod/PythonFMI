import re

_number = r'(?:[-\+]?(?:\b\d+\.\d*|\.\d+\b|\b\d+\b))'
_string = r'"(?:\\"|.)*?"'
_tokens = r"[\(\)']|#t|#f"
_special_symbol = re.escape(r'!$%&*+-./:<=>?@^_~')
_identifier = r'\b[a-zA-Z][a-zA-Z0-9{0}]*|(?=\W|^)[{0}](?=\W|$)?|\b_'.format(_special_symbol)

def tokenize(code):
    tokens = r'|'.join([_tokens, _string, _number, _identifier])
    return re.findall(tokens, code, re.S)

def identifiers(tokens):
    idents = set()
    for token in tokens:
        iden = re.match(_identifier, token)
        if iden:
            iden = iden.group()
            if iden.lower() not in [found.lower() for found in idents]:
                idents.add(iden)
    return idents

def case_sensitive(code, identifs):
    def replace_identifier(expr):
        ident = expr.group()
        if replacements.get(ident.lower()):
            return replacements[ident.lower()]
        else:
            return ident

    replacements = {iden.lower() : iden for iden in identifs}
    code = re.sub(r'({0})|{1}'.format(_identifier, _string), replace_identifier, code)
    return code

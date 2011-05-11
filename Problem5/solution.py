import re

_number = r'(?:[-\+]?(?:\b\d+\.\d*|\.\d+\b|\b\d+\b))'
_string = r'".*?"'
_tokens = r"[\(\)']|#t|#f"
_special_symbol = re.escape(r'!$%&*+-./:<=>?@^_~')
_identifier = r'\b[a-zA-Z][a-zA-Z0-9{0}]*|(?=\W|^)[{0}](?=\W|$)?|\b_'.format(_special_symbol)

def tokenize(code):
    tokens = r'|'.join([_tokens, _string, _number, _identifier])
    return re.findall(tokens, code, re.S)

def identifiers(tokens, caseinsensitive=True):
    idents = set()
    for token in tokens:
        iden = re.match(_identifier, token)
        if iden:
            iden = iden.group()
            if not caseinsensitive or\
                    iden.lower() not in [found.lower() for found in idents]:
                idents.add(iden)
    return idents

def case_sensitive(code, identifs):
    idents_in_code = identifiers(tokenize(code), False)
    replacements = {iden.lower() : iden for iden in identifs}
    for ident in idents_in_code:
        if replacements.get(ident.lower()):
            code = re.sub(ident, replacements[ident.lower()], code)
    return code

import re

number = r'\d+\.?\d*|\d*\.?\d+'
string = r'\".*\"'
tokens_rest = r"[\(\)']|#t|#f"
special_symbol = r'\!\$\%\&\*\+\-\.\/\:\<\=\>\?\@\^\_\~'
special_symbol = r'!%&-/:<=>@_~\$\*\+\.\?\^'
special_symbol = re.escape(r'!$%&*+-./:<=>?@^_~')
identifier = r'\A[a-zA-Z][{1}a-zA-Z{0}]*|\B[{0}]\B'.format(special_symbol, number)
identifier = r'\b[a-zA-Z][a-zA-Z0-9{0}]*|(?=\W|^)[{0}](?=\W|$)?|\b_'.format(special_symbol)

def tokenize(code):
    tokens = re.findall(r'|'.join([tokens_rest, string, number, identifier]), code)
    return tokens

def identifiers(tokens):
    idents = set()
    for token in tokens:
        iden = re.match(identifier, token)
        if iden and all([iden.group().lower() != found.lower()\
                for found in idents]):
            idents.add(iden.group())
    return idents

def case_sensitive(code, identifs):
    idents_in_code = identifiers(tokenize(code))
    replacements = {iden.lower() : iden for iden in identifs}
    for ident in idents_in_code:
        if replacements.get(ident.lower()):
            code = re.sub(ident, replacements[ident.lower()], code)
    return code

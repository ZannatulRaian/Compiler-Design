import keyword, re

def tokenize(code):
    pat = re.compile(r'''(["'](?:\\.|[^"'\\])*["']|\d+\.?\d*|[A-Za-z_]\w*|#.*|[+\-*/%<>!=&|^~]=?|//=?|\*\*=?|\*\*?|==|<=|>=|!=|[(){}\[\],:;.@#]|\s+|.)''')
    for m in pat.finditer(code):
        t = m.group()
        if t.isspace(): continue
        yield t, ('KEYWORD' if keyword.iskeyword(t) else
                 'STRING' if re.match(r'^["\'].*["\']$', t) else
                 'NUMBER' if re.match(r'^\d+\.?\d*$', t) else
                 'OPERATOR' if re.match(r'^[+\-*/%<>!=&|^~]=?$|^//=?$|^\*\*=?$|^\*\*?$|^==$|^<=$|^>=$|^!=$', t) else
                 'SYMBOL' if re.match(r'^[(){}\[\],:;.@#]$', t) else
                 'COMMENT' if t.startswith('#') else
                 'IDENTIFIER' if re.match(r'^[A-Za-z_]\w*$', t) else 'UNKNOWN')

# Usage
code = 'def hello(): return "world"'
for token, typ in tokenize(code):
    print(f"{typ:12} {token}")
import marshal
with open("MS", "rb") as f:
    code = marshal.loads(f.read())
exec(code)

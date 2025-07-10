import marshal
with open("/sdcard/MS", "rb") as f:
    code = marshal.loads(f.read())
exec(code)

"""Convert one-line flow lists that contain URLs into block lists (PyYAML chokes on '?' in flow URLs)."""
import re, sys
for p in sys.argv[1:]:
    out=[]
    for line in open(p, encoding="utf-8"):
        m=re.match(r"^(\s*)(- )?([a-z_]+): \[(.*http.*)\]\s*$", line)
        if m:
            ind, dash, key, body = m.groups()
            base = ind + ("  " if dash else "")
            out.append(f"{ind}{dash or ''}{key}:\n")
            for item in [x.strip().strip("\"") for x in body.split(", ")]:
                out.append(f"{base}- \"{item}\"\n")
        else:
            out.append(line)
    open(p,"w",encoding="utf-8").writelines(out)

# Second pass: quote plain scalar values that contain ': ' or ' #' (YAML indicators).
for p in sys.argv[1:]:
    out=[]
    for line in open(p, encoding="utf-8"):
        m=re.match(r"^(\s*(?:- )?[a-z_]+: )(.+?)\s*$", line)
        if m and not re.match(r"^[\"'\[{|>]", m.group(2)) and (": " in m.group(2) or " #" in m.group(2)):
            v=m.group(2).replace("\\","\\\\").replace('"','\\"')
            line=f'{m.group(1)}"{v}"\n'
        else:
            m2=re.match(r"^(\s*- )(?![a-z_]+: )(.+?)\s*$", line)
            if m2 and not re.match(r"^[\"'\[{|>]", m2.group(2)) and (": " in m2.group(2) or " #" in m2.group(2)):
                v=m2.group(2).replace("\\","\\\\").replace('"','\\"')
                line=f'{m2.group(1)}"{v}"\n'
        out.append(line)
    open(p,"w",encoding="utf-8").writelines(out)

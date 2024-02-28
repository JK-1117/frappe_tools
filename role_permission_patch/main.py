import pandas as pd
import json

df = pd.read_excel(
    "./sample_excel.xlsx",
    sheet_name="Sheet1",
    header=[0, 1],
    index_col=[0, 1],
)

# print(df.loc[:, [x for x in df.columns if "Accounts Manager" in x]])
# print(df.columns)
# print(df.index)
# print(df["Accounts User", "Read"]["Sales Invoice", "accounts"])

count = 0
perms = []
for [dt, module] in df.index:
    doc = {
        "dn": dt,
        "module": module,
        "perms": {
            0: {},
        },
    }
    for [role, perm] in df.columns:
        count += 1
        val = df[role, perm][dt, module]
        if val in [0, 1, 2] and role not in doc["perms"][0]:
            can_read = 1 if df[role, "Read"][dt, module] > 0 else 0
            doc["perms"][0][role] = {
                "print": can_read,
                "email": can_read,
                "report": can_read,
                "share": can_read,
            }

        if val == 2:
            doc["perms"][0][role][perm.lower()] = 1

            if 1 not in doc["perms"]:
                doc["perms"][1] = {}
            if role not in doc["perms"][1]:
                doc["perms"][1][role] = {}
            doc["perms"][1][role][perm.lower()] = 1
        elif val in [0, 1]:
            doc["perms"][0][role][perm.lower()] = int(val)

    perms.append(doc)

perms_json = json.dumps(perms, indent=2)
f = open("base_permissions.json", "w")
f.write(perms_json)
f.close()

print(count)

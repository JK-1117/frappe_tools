import frappe
import json
from os.path import join

app = "appname"


def check_fixtures():
    cffile = open(join("..", "apps", app, app, "fixtures", "custom_field.json"))
    psfile = open(join("..", "apps", app, app, "fixtures", "property_setter.json"))

    cfjson = json.load(cffile)
    psjson = json.load(psfile)

    cffixtures = []
    psfixtures = []
    fixtures = frappe.get_hooks("fixtures", [], app_name=app)
    for f in fixtures:
        if type(f) == dict:
            if f["doctype"] == "Custom Field":
                cffixtures = f["filters"]["name"][1]
            elif f["doctype"] == "Property Setter":
                psfixtures = f["filters"]["name"][1]

    cfjson = [x["name"] for x in cfjson]
    psjson = [x["name"] for x in psjson]

    print("Checking Custom Fields")
    print("========================")
    clear = True
    for cf in cffixtures:
        if cf not in cfjson:
            print("\033[91m {} is not exported \033[00m".format(cf))
            clear = False
    if clear:
        print("\033[92m All Custom Fields are exported!! \033[00m")

    print("Checking Property Setters")
    print("========================")
    clear = True
    for ps in psfixtures:
        if ps not in psjson:
            print("\033[91m {} is not exported \033[00m".format(ps))
            clear = False
    if clear:
        print("\033[92m All Property Setters are exported!! \033[00m")

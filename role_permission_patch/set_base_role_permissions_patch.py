import frappe
from frappe.permissions import add_permission, update_permission_property
import json
import os

app = "appname"


def execute():
    f = open(
        os.path.join(
            "..",
            "apps",
            app,
            app,
            "patches",
            "v0_1",
            "base_permissions.json",
        )
    )
    perms = json.load(f)

    for dt in perms:
        frappe.reload_doc(dt["module"], "doctype", dt["dn"])
        for lvl in dt["perms"]:
            for role in dt["perms"][lvl]:
                add_permission(dt["dn"], role, lvl)
                for perm in dt["perms"][lvl][role]:
                    update_permission_property(
                        dt["dn"], role, lvl, perm, dt["perms"][lvl][role][perm]
                    )

    # Accounts Manager
    # cti = "Company Taxation Information"
    # am = "Accounts Manager"
    # add_permission(cti, am, 0)
    # update_permission_property(cti, am, 0, "create", 1)
    # update_permission_property(cti, am, 0, "read", 1)
    # update_permission_property(cti, am, 0, "write", 1)
    # update_permission_property(cti, am, 0, "delete", 1)

    # add_permission("Department", "Sales User", 0)
    # update_permission_property("Department", "Sales User", 0, "read", 1)
    # update_permission_property("Department", "Sales User", 0, "select", 1)

    # add_permission("Payment Terms Template", "Sales User", 0)
    # update_permission_property("Payment Terms Template", "Sales User", 0, "read", 1)
    # update_permission_property("Payment Terms Template", "Sales User", 0, "select", 1)

# -*- coding: utf-8 -*-
# Copyright (c) 2015, Convergenix and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class MaterialRequisition(Document):
    def set_onload(self, key, value):
        pass


@frappe.whitelist()
def make_delivery_note(source_name, target_doc=None):
    return _make_delivery_note(source_name, target_doc)


def _make_delivery_note(source_name, target_doc=None, ignore_permissions=False):
    def set_missing_values(source, target):
        target.ignore_pricing_rule = 1
        target.flags.ignore_permissions = ignore_permissions
        target.parent= source_name

    # target.run_method("set_missing_values")
    # target.run_method("calculate_taxes_and_totals")

    doclist = get_mapped_doc("Material Requisition", source_name, {
        "Material Requisition": {
            "doctype": "Material Delivery Note",
            "validation": {
                "docstatus": ["=", 1]
            }
        },
        "Material Requisition Item": {
            "doctype": "Material Delivery Note Item",
            "field_map": {
                "parent": "prevdoc_docname",
            }
        },
    }, target_doc, set_missing_values, ignore_permissions=ignore_permissions)

    # postprocess: fetch shipping address, set missing values

    return doclist


@frappe.whitelist()
def get_details(customer):
    address = ""
    val = {
        'customer_address': _get_address(customer),
        'contact_person': _get_contact_person(customer)
    }
    frappe.errprint(val)
    return val


def _get_address(customer):
    address = ""
    if customer:
        addr_list = frappe.get_all("Address", ["*"], {"customer": customer})
        if addr_list:
            addr_item = addr_list[0]
            address += addr_item.get('address_title') or ""
            address += "\n"
            address += addr_item.get('address_line1') or ""
            address += "\n"
            address += addr_item.get('address_line2') or ""
            address += "\n"
            address += addr_item.get('phone') or ""
            address += "\n"
    return address


def _get_contact_person(customer):
    contact = ""
    if customer:
        contact_list = frappe.get_all("Contact", ["name"], {"customer": customer})
        if contact_list:
            frappe.errprint(contact_list)
            contact_item = contact_list[0]
            contact += contact_item.get('name') or ""
    return contact

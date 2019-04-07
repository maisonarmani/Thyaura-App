# Copyright (c) 2013, Convergenix and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns, data = [
                        "Customer:Link/Customer:150",
                        "Requisition:Link/Material Requisition:100",
                        "Material Delivery Note:Link/Material Delivery Note:100",
                        "Stock Entry:Link/Stock Entry:100",
                        "Requested By:Data:150",
                        "Quantity Delivered:Float:100",
                        "Amount:Float:100",
                        "Date:Date:100",
                    ], []

    cond = ""
    if filters.get("date_from"):
        cond += " AND p.date BETWEEN DATE('{date_from}') AND DATE('{date_to}')"

    d = frappe.db.sql("SELECT p.customer, p.material_requisition,p.name,p.stock_entry , p.requested_by, SUM(c2.qty) ,SUM(c2.amount) , "
                      "p.date FROM `tabStock Entry` c1 INNER  JOIN `tabStock Entry Detail` c2 on(c1.name=c2.parent) INNER JOIN"
                      "`tabMaterial Delivery Note` p on(p.stock_entry=c1.name) WHERE p.docstatus = 1  %s GROUP BY p.name" %(cond.format(**filters)) )
    data = d
    return columns, data

# -*- coding: utf-8 -*-
# Copyright (c) 2015, Convergenix and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils import flt, cint
from datetime import datetime, time
from frappe.model.document import Document

import frappe


class UpdateException(Exception):
    pass

class MaterialDeliveryNote(Document):
    mt_req_del_setup = {}
    def on_submit(self):
        if self.mt_req_del_setup is not None:
            self.update_stock_value()
        else :
            raise Exception("Material Requisition has not been setup properly, please contact your administrator")
        return True



    def validate(self):
        # update stock actual value
        self.mt_req_del_setup = frappe.get_single("Material Requisition and Delivery Setup")
        self.update_items_de_stock()
        self.validate_items()
        return True

    def update_mdn(self, se):
        frappe.db.sql(
            "UPDATE `tabMaterial Delivery Note` SET stock_entry='%s' WHERE name = '%s'" % (se.name, self.name))

    def validate_items(self):
        for item in self.get('items'):
            if(item.qty == 0):
                raise frappe.exceptions.ValidationError("Delivered Quality must be greater than 0")


    def update_items_de_stock(self):
        if self.get("_action") and self._action != "update_after_submit":
            for item in self.get('items'):
                item.actual_qty = frappe.db.get_value("Bin", {"item_code": item.get('item_code'),
                                                           "warehouse" : item.get('warehouse')}, "actual_qty")

    def update_stock_value(self):
        _items = []
        for item in self.get('items'):
            _items.append({
                "s_warehouse": self.mt_req_del_setup.source_warehouse,
                "expense_amount": self.mt_req_del_setup.expense_account,
                "cost_center": self.mt_req_del_setup.cost_center,
                "item_code": item.get('item_code'),
                "item_name": item.get('item_name'),
                "qty": item.get('qty'),
                "actual_qty": item.get('actual_qty'),
                "uom": item.get('uom'),
                "basic_rate": 0,
                "conversion_factor": 0,
                "basic_amount": 0,
                "stock_uom": item.get('uom'),
                "transfer_qty": 1,
                "valuation_rate": 0,
            })

        # create new    stock entry
        # remove item qty that has been delivered to stock
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "purpose": 'Material Issue',
            "posting_date": datetime.now(),
            "posting_time": datetime.now().strftime('%H:%M:%S'),
            "from_warehouse": self.mt_req_del_setup.get('source_warehouse'),
            "total_outgoing_value": 0,
            "total_incoming_value": 0,
            "value_difference": 0,
            "items": _items
        })

        stock_entry.insert()
        try:
            self.update_mdn(stock_entry)
            stock_entry.submit()
        except UpdateException:
            pass

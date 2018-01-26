# -*- coding: utf-8 -*-
# Copyright (c) 2015, Convergenix and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
from datetime import  datetime

# test_records = frappe.get_test_records('Material Delivery Note')

class TestMaterialDeliveryNote(unittest.TestCase):
    def ind_gt(self):
        mt_req_del_setup = frappe.get_single("Material Requisition and Delivery Setup")
        print(mt_req_del_setup.__dict__)

    def test_item_stock(self):

        # get setup information
        mt_req_del_setup = frappe.get_single("Material Requisition and Delivery Setup")

        # create new stock entry
        # remove item qty that has been delivered to stock
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "purpose":'Material Issue',
            "posting_date":datetime.now(),
            "posting_time":datetime.now().strftime('%H:%M:%S'),
            "from_warehouse":mt_req_del_setup.source_warehouse,
            "total_outgoing_value":0,
            "total_incoming_value":0,
            "value_difference":0,
            "items":[
                {
                    "s_warehouse":mt_req_del_setup.source_warehouse,
                    "item_code": 'GCL0012',
                    "item_name": "",
                    "qty":1,
                    "actual_qty":200,
                    "uom":"Carton",
                    "basic_rate":0,
                    "conversion_factor":0,
                    "basic_amount":0,
                    "stock_uom":"Carton",
                    "transfer_qty":1,
                    "valuation_rate":0,
                    "expense_amount":mt_req_del_setup.expense_account,
                    "cost_center": mt_req_del_setup.cost_center
                },
                {
                    "s_warehouse":mt_req_del_setup.source_warehouse,
                    "item_code": 'GCL0013',
                    "item_name": "",
                    "qty":1,
                    "actual_qty":200,
                    "uom":"Carton",
                    "basic_rate":0,
                    "conversion_factor":0,
                    "basic_amount":0,
                    "stock_uom":"Carton",
                    "transfer_qty":1,
                    "valuation_rate":0,
                    "expense_amount":mt_req_del_setup.expense_account,
                    "cost_center": mt_req_del_setup.cost_center
                }
            ]
        })
        stock_entry.flags.ignore_permission = 1
        stock_entry.insert()
        stock_entry.submit()
        print(stock_entry.__dict__)


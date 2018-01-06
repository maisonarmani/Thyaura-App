# -*- coding: utf-8 -*-
# Copyright (c) 2015, Convergenix and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Material Requisition')

class TestMaterialRequisition(unittest.TestCase):
	def _________________(self):
		address = ""
		addr_list = frappe.get_all("Address", ["*"],{"customer":"Damsat"})
		addr_item = addr_list[0]
		address += addr_item.get('address_title')
		address += "\n"
		address += addr_item.get('address_line1')
		address += "\n"
		address += addr_item.get('address_line2')
		address += "\n"
		address += addr_item.get('phone')
		address += "\n"
		print address

	def test_contact_person(customer):
		customer = "Damsat"
		contact = ""
		if customer:
			contact_list = frappe.get_all("Contact", ["name"], {"customer": customer})
			if contact_list:
				frappe.errprint(contact_list)
				contact_item = contact_list[0]
				contact += contact_item.get('name') or ""
		print contact
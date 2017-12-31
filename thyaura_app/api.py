# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import unittest
import frappe
from frappe.desk.form.load import getdoctype


@frappe.whitelist()
def test_doctype():
    print getdoctype(doctype="Daily Route Activity", with_parent = 1)
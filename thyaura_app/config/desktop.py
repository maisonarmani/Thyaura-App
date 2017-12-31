# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Thyaura",
			"color": "#934bec",
			"doctype": "File",
			"icon": "octicon octicon-file-directory",
			"label": _("Thyaura"),
			"link": "modules/Thyaura",
			"type": "module",
			"hidden": 0
		},
	]

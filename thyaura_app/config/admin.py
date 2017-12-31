from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Forms"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Payment Voucher Form",
					"description": _("Payment Voucher Form"),
				},
				{
					"type": "doctype",
					"name": "Petty Cash Log",
					"description": _("Petty Cash Log"),
				},
				{
					"type": "doctype",
					"name": "Daily Generator Activity Log",
					"description": _("Daily Generator Activity Log"),
				},
				{
					"type": "doctype",
					"name": "Generator Fuel Consumption Log",
					"description": _("Generator Fuel Consumption Log"),
				},
				{
					"type": "doctype",
					"name": "Fixed Asset Inspection Checklist",
					"description": _("Fixed Asset Inspection Checklist"),
				},
			]
		},
		{
			"label": _("Logistics"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Daily Route Activity",
					"description": _("Daily Route Activity"),
				},
			]
		},
		{
			"label": _("Material"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Material Requisition",
					"description": _("Material Requisition"),
				},
				{
					"type": "doctype",
					"name": "Material Delivery Note",
					"description": _("Material Delivery Note"),
				},
			]
		},
		{
			"label": _("Reports"),
			"icon": "icon-star",
			"items": [
				{
					"type": "report",
					"name": "Payment Voucher Form Report",
					"doctype": "Payment Voucher Form",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Petty Cash Log Report",
					"doctype": "Petty Cash Log",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Fixed Asset Register Report",
					"doctype": "Asset",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Fixed Asset Inspection Checklist Report",
					"doctype": "Fixed Asset Inspection Checklist",
					"is_query_report": True,
				},
			]
		}
	]

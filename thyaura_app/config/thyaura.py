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
			]
		}
	]

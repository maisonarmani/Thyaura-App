// Copyright (c) 2016, Convergenix and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Delivered Reconciliation"] = {
	"filters": [
		{
			"fieldname":"date_from",
			"label": __("Date from"),
			"fieldtype": "Date",
			"default":frappe.datetime.year_start(),
			'reqd':1
		},
		{
			"fieldname":"date_to",
			"label": __("Date to"),
			"fieldtype": "Date",
			"default":frappe.datetime.year_end(),
			'reqd':1
		}
	]
}

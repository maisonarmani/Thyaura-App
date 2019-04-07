// Copyright (c) 2016, Convergenix and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Report Summary"] = {
	"filters": [
	{
			"fieldname":"month",
			"label": __("Month"),
			"fieldtype": "Select",
			"options": "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAuga\nSep\nOct\nNov\nDec",
			"default": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
				"Dec"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
		},{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ["Left","Active"],
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		}
	]
}
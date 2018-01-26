// Copyright (c) 2016, Convergenix and contributors
// For license information, please see license.txt

frappe.ui.form.on('Material Delivery Note', {
	refresh: function(frm) {
        if (!frm.doc.__islocal && frm.doc.docstatus == 1)
			cur_frm.cscript.make_sales_invoice()
	}
});


// Delivery note button
cur_frm.cscript.make_sales_invoice=  function () {
    cur_frm.add_custom_button(__('Make Sales Invoice'),
       function(){
            var si = frappe.model.make_new_doc_and_get_name('Sales Invoice');
            si = locals['Sales Invoice'][si];
            si.material_delivery_note = cur_frm.doc.name;
            frappe.set_route("Form", "Sales Invoice", si.name);
        }
	);
};

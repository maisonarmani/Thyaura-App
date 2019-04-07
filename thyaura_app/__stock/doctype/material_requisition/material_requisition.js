// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Material Requisition', {
    refresh: function (frm) {
        var doc = frm && frm.doc;
        if (doc.__islocal && doc.docstatus == 0)
            cur_frm.set_value("requested_by", user);
        if (!doc.__islocal && doc.docstatus == 1)
            frm.cscript.material_delivery_note();
    },
    customer:function(frm){
        frappe.call({
            method: "thyaura_app._stock.doctype.material_requisition.material_requisition.get_details",
            args:{customer:frm.doc.customer},
            callback:function(rt){
                cur_frm.set_value('customer_address',rt.message.customer_address);
                cur_frm.set_value('contact_person',rt.message.contact_person);
            }
        });
    }
});


frappe.ui.form.on("Material Requisition Item", {
        "qty": function (frm, doctype, name) {
            var d = locals[doctype][name];
            if (flt(d.qty) < flt(d.min_order_qty)) {
                alert(__("Warning: Material Requested Qty is less than Minimum Order Qty"));
            }
        }
    }
);

// Delivery note button
cur_frm.cscript.material_delivery_note = function () {
    cur_frm.add_custom_button(__('Material Delivery Note'),
        function () {
            frappe.model.open_mapped_doc({
                method: "thyaura_app._stock.doctype.material_requisition.material_requisition.make_delivery_note",
                frm: cur_frm
            });
        }
    );
};


// Delivery note button
cur_frm.cscript.sales_order_btn = function () {
    cur_frm.add_custom_button(__('Material Delivery Note'),
        function () {
            erpnext.utils.map_current_doc({
                method: "thyaura.stock.doctype.make_delivery_note",
                source_doctype: "Material Delivery Note",
                get_query_filters: {
                    docstatus: 1,
                    status: ["!=", "Closed"],
                    per_billed: ["<", 99.99],
                    customer: cur_frm.doc.customer || undefined,
                    company: cur_frm.doc.company,
                    atl: 0
                }
            })
        }, __("Get items from")
    );
};
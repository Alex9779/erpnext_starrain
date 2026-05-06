// Copyright (c) 2026, Beveren Software and contributors
// For license information, please see license.txt

frappe.ui.form.on("Reitanlage", {
	refresh(frm) {
		if (frm.doc.__islocal) {
			const last_doc = frappe.contacts.get_last_doc(frm);
			if (
				frappe.dynamic_link &&
				frappe.dynamic_link.doc &&
				frappe.dynamic_link.doc.name == last_doc.docname
			) {
				frm.set_value("links", "");
				frm.add_child("links", {
					link_doctype: frappe.dynamic_link.doctype,
					link_name: frappe.dynamic_link.doc[frappe.dynamic_link.fieldname],
				});
				frm.refresh_field("links");
			}
		}
	},
});

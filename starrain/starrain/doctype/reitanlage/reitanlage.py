# Copyright (c) 2026, Beveren Software and contributors
# For license information, please see license.txt

import re

import frappe
from frappe.contacts.address_and_contact import set_link_title
from frappe.model.document import Document

_BAUJAHR_PATTERN = re.compile(r"^(?:(?:0?[1-9]|1[0-2])/)?\d{4}$")


def _validate_baujahr(value: str | None, label: str) -> None:
	if not value:
		return
	stripped = str(value).strip()
	if not stripped or stripped == "0":
		return
	if not _BAUJAHR_PATTERN.match(stripped):
		frappe.throw(
			frappe._(
				"{0}: Ungültiges Format. Erlaubt sind ein Jahr (z. B. 2020) "
				"oder Monat/Jahr (z. B. 05/2020)."
			).format(frappe.bold(label))
		)


class Reitanlage(Document):
	def validate(self):
		_validate_baujahr(self.baujahr, frappe._("Baujahr"))
		_validate_baujahr(self.beregnung_baujahr, frappe._("Baujahr (Beregnung)"))
		set_link_title(self)

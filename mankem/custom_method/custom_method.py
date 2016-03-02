
from __future__ import unicode_literals
import frappe
import json
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and, cint
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname


@frappe.whitelist()
def create_customer_code(doc, method):
	if not doc.customer_code:	
		doc.customer_code = make_autoname('CST-'+'.#####')
	else:
		doc.customer_code = doc.customer_code

@frappe.whitelist()
def create_supplier_code(doc, method):
	if not doc.supplier_code:	
		doc.supplier_code = make_autoname('SUP-'+'.#####')
	else:
		doc.supplier_code = doc.supplier_code
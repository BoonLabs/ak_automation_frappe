"""API endpoints for AK Automation — visual/configuration only.

These endpoints provide metadata for the UI (field lists, operators, options).
No automation dispatching or execution occurs.
"""

import frappe


@frappe.whitelist()
def get_doctype_fields(doctype):
	"""Return fields of a DocType for UI dropdowns (field pickers)."""
	meta = frappe.get_meta(doctype)
	fields = []
	for df in meta.fields:
		if df.fieldtype not in (
			"Section Break", "Column Break", "Tab Break", "HTML",
			"Table", "Table MultiSelect", "Fold",
		):
			fields.append({
				"fieldname": df.fieldname,
				"label": df.label or df.fieldname,
				"fieldtype": df.fieldtype,
				"options": df.options,
				"reqd": df.reqd,
			})
	return fields


@frappe.whitelist()
def get_field_options(doctype, fieldname):
	"""Return valid options for a Select field on a DocType."""
	meta = frappe.get_meta(doctype)
	df = meta.get_field(fieldname)
	if df and df.fieldtype == "Select" and df.options:
		return [opt for opt in df.options.split("\n") if opt]
	return []


@frappe.whitelist()
def get_operators_for_field(doctype, fieldname):
	"""Return valid operators based on field type."""
	meta = frappe.get_meta(doctype)
	df = meta.get_field(fieldname)

	if not df:
		return _text_operators()

	fieldtype = df.fieldtype

	if fieldtype in ("Int", "Float", "Currency", "Percent"):
		return _numeric_operators()
	elif fieldtype in ("Date", "Datetime"):
		return _date_operators()
	elif fieldtype == "Select":
		return _select_operators()
	elif fieldtype in ("Link", "Dynamic Link"):
		return _link_operators()
	elif fieldtype == "Check":
		return _check_operators()
	else:
		return _text_operators()


def _text_operators():
	return [
		"is", "is not", "contains", "does not contain",
		"starts with", "ends with", "is empty", "is not empty",
		"has changed", "has changed to", "has changed from",
	]


def _numeric_operators():
	return [
		"=", "!=", ">", "<", ">=", "<=", "between",
		"is empty", "is not empty", "has changed",
	]


def _date_operators():
	return [
		"is", "is not", "before", "after", "between",
		"is today", "is tomorrow", "is yesterday",
		"less than days ago", "more than days ago",
		"less than days later", "more than days later",
		"is empty", "is not empty",
	]


def _select_operators():
	return [
		"is", "is not", "has changed", "has changed to", "has changed from",
	]


def _link_operators():
	return [
		"is", "is not", "is empty", "is not empty", "has changed",
	]


def _check_operators():
	return ["is", "is not"]


@frappe.whitelist()
def get_button_automations(doctype):
	"""Return all active button/macro automations for a DocType (visual listing only)."""
	return frappe.get_list("AK Automation",
		filters={
			"reference_doctype": doctype,
			"trigger_type": "Macro (Button)",
			"enabled": 1,
		},
		fields=["name", "title", "button_label"],
	)

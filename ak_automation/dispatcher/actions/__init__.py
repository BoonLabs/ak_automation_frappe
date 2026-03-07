import frappe
from importlib import import_module


ACTION_MODULE_MAP = {
	"Send Email": "ak_automation.dispatcher.actions.send_email",
	"Send WhatsApp": "ak_automation.dispatcher.actions.send_whatsapp",
	"Update Fields": "ak_automation.dispatcher.actions.update_fields",
	"Create Record": "ak_automation.dispatcher.actions.create_record",
	"Create Todo": "ak_automation.dispatcher.actions.create_todo",
	"Create Event": "ak_automation.dispatcher.actions.create_event",
	"HTTP Request": "ak_automation.dispatcher.actions.http_request",
	"Run Script": "ak_automation.dispatcher.actions.run_script",
}


def execute_action(action_row, doc, automation):
	"""Dispatch an action row to the correct handler module."""
	action_type = action_row.action_type
	module_path = ACTION_MODULE_MAP.get(action_type)

	if not module_path:
		frappe.throw(f"Unknown action type: {action_type}")

	module = import_module(module_path)
	return module.execute(action_row, doc, automation)

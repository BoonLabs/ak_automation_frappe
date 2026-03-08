import frappe
from frappe.model.document import Document


class AKAutomation(Document):
	def validate(self):
		if not self.actions:
			frappe.throw("At least one action is required.")

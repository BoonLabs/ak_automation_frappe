import frappe
from frappe.tests import UnitTestCase


class TestAKAutomationController(UnitTestCase):
	"""Tests for AK Automation DocType controller methods."""

	def test_validate_throws_without_actions(self):
		"""Automation without actions should fail validation."""
		auto = frappe.get_doc({
			"doctype": "AK Automation",
			"title": "No Actions Auto",
			"reference_doctype": "ToDo",
			"trigger_type": "On Create",
			"enabled": 1,
			"actions": [],
		})
		with self.assertRaises(Exception):
			auto.insert(ignore_permissions=True)

	def test_validate_passes_with_action(self):
		"""Automation with at least one action should pass validation."""
		auto = frappe.get_doc({
			"doctype": "AK Automation",
			"title": "Valid Auto",
			"reference_doctype": "ToDo",
			"trigger_type": "On Create",
			"enabled": 1,
			"actions": [{
				"action_type": "Run Script",
				"action_label": "Test",
				"enabled": 1,
				"script_code": "1",
			}],
		})
		auto.insert(ignore_permissions=True)
		self.assertTrue(auto.name)
		frappe.delete_doc("AK Automation", auto.name, ignore_permissions=True, force=True)

	def test_creation_with_all_fields(self):
		"""Automation with all field types should be created successfully."""
		auto = frappe.get_doc({
			"doctype": "AK Automation",
			"title": "Full Fields Auto",
			"reference_doctype": "ToDo",
			"trigger_type": "On Update (includes Create)",
			"trigger_field": "status",
			"enabled": 1,
			"recurrence": "Only First Time Conditions Are Met",
			"description": "Test automation with all fields",
			"all_conditions": [{
				"field": "status",
				"operator": "is",
				"value": "Open",
			}],
			"any_conditions": [{
				"field": "priority",
				"operator": "is",
				"value": "High",
			}],
			"actions": [{
				"action_type": "Update Fields",
				"action_label": "Update status",
				"enabled": 1,
			}],
		}).insert(ignore_permissions=True)

		self.assertTrue(auto.name)
		self.assertEqual(auto.trigger_type, "On Update (includes Create)")
		self.assertEqual(auto.trigger_field, "status")
		self.assertEqual(auto.recurrence, "Only First Time Conditions Are Met")
		self.assertEqual(len(auto.all_conditions), 1)
		self.assertEqual(len(auto.any_conditions), 1)
		self.assertEqual(len(auto.actions), 1)

		frappe.delete_doc("AK Automation", auto.name, ignore_permissions=True, force=True)

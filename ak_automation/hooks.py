app_name = "ak_automation"
app_title = "AK Automation"
app_publisher = "AK"
app_description = "Visual automation configuration app for Frappe"
app_email = "advait.k@swajal.in"
app_license = "MIT"
required_apps = ["frappe"]

# Include custom CSS for AK Automation form styling
app_include_css = "/assets/ak_automation/css/automation_ak.css"

# NOTE: This app is visual/configuration-only.
# No doc_events or scheduler_events — automations are not dispatched.

app_name = "ak_automation"
app_title = "AK Automation"
app_publisher = "AK"
app_description = "Automation engine for Frappe — trigger actions on document events, cron, and macros"
app_email = "advait.k@swajal.in"
app_license = "MIT"
required_apps = ["frappe"]

# Document Events
doc_events = {
    "*": {
        "after_insert": "ak_automation.dispatcher.engine.handle_event",
        "on_update": "ak_automation.dispatcher.engine.handle_event",
        "on_submit": "ak_automation.dispatcher.engine.handle_event",
    }
}

# Scheduled Tasks
scheduler_events = {
    "all": [
        "ak_automation.dispatcher.engine.run_cron_automations",
    ],
    "daily": [
        "ak_automation.dispatcher.engine.cleanup_old_logs",
    ],
}

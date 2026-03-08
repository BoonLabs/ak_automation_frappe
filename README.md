# AK Automation

Visual automation configuration app for Frappe — define triggers, conditions, and actions on document events, cron schedules, and macros. This app is **configuration-only**; it does not dispatch or execute automations at runtime.

## Installation

```bash
bench get-app https://github.com/<your-org>/ak_automation_frappe.git
bench --site <site-name> install-app ak_automation
bench --site <site-name> migrate
```

## DocTypes

| DocType | Type | Purpose |
|---------|------|---------|
| **AK Automation** | Parent | Core automation record — trigger, conditions, actions, linked Server Script |
| **AK Automation Condition** | Child table | Condition row (field + operator + value) used in All/Any condition groups |
| **AK Automation Action** | Child table | Action row (action type + config) attached to an automation |
| **AK Field Update** | Child table | Field update detail row (target field + value type + expression) |
| **AK Automation Settings** | Single | App-wide settings |

## API Endpoints

All endpoints live in `ak_automation.api.automation`:

| Method | Description |
|--------|-------------|
| `get_doctype_fields(doctype)` | Returns non-layout fields for UI field pickers |
| `get_field_options(doctype, fieldname)` | Returns Select field options |
| `get_operators_for_field(doctype, fieldname)` | Returns valid operators based on field type |
| `get_button_automations(doctype)` | Lists active Macro (Button) automations for a DocType |

## Project Structure

```
ak_automation_frappe/
├── pyproject.toml                          # Package metadata & dependencies
├── README.md
├── CLAUDE.md                               # AI developer reference
├── .gitignore
│
└── ak_automation/                          # Frappe app root
    ├── __init__.py                         # App version
    ├── hooks.py                            # Frappe hooks (visual-only, no doc_events)
    ├── modules.txt                         # Registered modules
    ├── patches.txt                         # Migration patches
    │
    ├── api/
    │   ├── __init__.py
    │   └── automation.py                   # Whitelisted API endpoints
    │
    ├── automation_ak/                      # "Automation AK" module
    │   ├── __init__.py
    │   ├── doctype/
    │   │   ├── ak_automation/              # Main automation DocType
    │   │   │   ├── ak_automation.json      # Schema (fields, permissions)
    │   │   │   ├── ak_automation.py        # Controller (validate)
    │   │   │   ├── ak_automation.js        # Client script (field pickers, dialogs)
    │   │   │   └── test_ak_automation.py   # Unit tests
    │   │   │
    │   │   ├── ak_automation_action/       # Child table — action rows
    │   │   │   ├── ak_automation_action.json
    │   │   │   └── ak_automation_action.py
    │   │   │
    │   │   ├── ak_automation_condition/    # Child table — condition rows
    │   │   │   ├── ak_automation_condition.json
    │   │   │   └── ak_automation_condition.py
    │   │   │
    │   │   ├── ak_automation_settings/     # Single settings DocType
    │   │   │   ├── ak_automation_settings.json
    │   │   │   ├── ak_automation_settings.py
    │   │   │   └── ak_automation_settings.js
    │   │   │
    │   │   └── ak_field_update/            # Child table — field update detail
    │   │       ├── ak_field_update.json
    │   │       └── ak_field_update.py
    │   │
    │   └── workspace/
    │       └── automation_ak/
    │           └── automation_ak.json      # Desk workspace definition
    │
    ├── public/
    │   └── css/
    │       └── automation_ak.css           # Custom styles
    │
    └── tests/
        ├── __init__.py
        └── test_automation_api.py          # API endpoint tests
```

## License

MIT

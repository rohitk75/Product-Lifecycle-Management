from frappe import _


def get_data():
    return {
        "fieldname": "article",
        "non_standard_fieldnames": {
            "Project": "custom_article",
            "Task": "project",            
        },
        "transactions": [
            {
                "label": _("New Product Launch"),
                "items": ["Project", "Task"],
            },
 
        ],
    }

from frappe import _


def get_data():
    return {
        "fieldname": "article",
        "non_standard_fieldnames": {
            "Project": "custom_article",
        },
        "transactions": [
            {
                "label": _("Payment"),
                "items": [
                    "Project",

                ],
            },
 
        ],
    }

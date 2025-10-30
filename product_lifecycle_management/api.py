@frappe.whitelist()
def get_measure_attributes(measure_category):
    measurement_attributes = frappe.db.sql(f""" SELECT measurement_attribute FROM `tabMeasurement Attributes` WHERE measure_category='{measure_category}' """, as_dict=True)
    return measurement_attributes

@frappe.whitelist(allow_guest=True)
def public_api_endpoint():
    return {"message": "This is a public endpoint!"}
    
# http://127.0.0.1:8000/api/method/product_lifecycle_management.product_lifecycle_management.api.public_api_endpoint

# http://127.0.0.1:8000/app/product_lifecycle_management/product_lifecycle_management/api/get_measure_attributes
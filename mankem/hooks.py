# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "mankem"
app_title = "mankem"
app_publisher = "SBK"
app_description = "app to manage customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kolate.sambhaji@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

fixtures = ["Custom Field", "Property Setter"]

doc_events = {
	"Customer":{
		"before_insert": "mankem.custom_method.custom_method.create_customer_code"
	},
	"Supplier":{
		"before_insert": "mankem.custom_method.custom_method.create_supplier_code"
	}
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mankem/css/mankem.css"
# app_include_js = "/assets/mankem/js/mankem.js"

# include js, css files in header of web template
# web_include_css = "/assets/mankem/css/mankem.css"
# web_include_js = "/assets/mankem/js/mankem.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mankem.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mankem.install.before_install"
# after_install = "mankem.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mankem.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mankem.tasks.all"
# 	],
# 	"daily": [
# 		"mankem.tasks.daily"
# 	],
# 	"hourly": [
# 		"mankem.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mankem.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mankem.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mankem.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mankem.event.get_events"
# }


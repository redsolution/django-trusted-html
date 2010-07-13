# django-trusted-html
INSTALLED_APPS += ['trustedhtml']

TRUSTEDHTML_ENABLE_LOG = {% if trustedhtml_settings.enabled_log %}True{% else %}False{% endif %}
TRUSTEDHTML_VERIFY_SITES = {% if trustedhtml_settings.verify_sites %}True{% else %}False{% endif %}
TRUSTEDHTML_CUT_SITES = CONFIG_SITES + CONFIG_REDIRECTS + [{% for cut_site in trustedhtml_settings.cut_sites.all %}
    '{{ cut_site.site }}',{% endfor %}
]
TRUSTEDHTML_OBJECT_SITES = [{% for object_site in trustedhtml_settings.object_sites.all %}
    '{{ object_site.site }}',{% endfor %}
]
TRUSTEDHTML_MODELS = [{% for model in trustedhtml_settings.models.all %}
    {
    	'model': '{{ model.model }}',
    	'fields': [{% for field in model.fields.all %}'{{ field.field }}',{% endfor %}]
	},{% endfor %}
]

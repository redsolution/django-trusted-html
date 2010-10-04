# ---- django-trusted-html ----

INSTALLED_APPS += ['trustedhtml']

# Should validation results be logged in database
TRUSTEDHTML_ENABLE_LOG = {% if trustedhtml_settings.enabled_log %}True{% else %}False{% endif %}

# Links from these sites are allowed. Other are not. 
TRUSTEDHTML_VERIFY_SITES = {% if trustedhtml_settings.verify_sites %}True{% else %}False{% endif %}
TRUSTEDHTML_CUT_SITES = {% if server_config_was_installed %}CONFIG_SITES + CONFIG_REDIRECTS + {% endif %}[{% for cut_site in trustedhtml_settings.cut_sites.all %}
    '{{ cut_site.cut_site }}',{% endfor %}
]

# Object tags (swf players an so on) from these sites are allowed
TRUSTEDHTML_OBJECT_SITES = [{% for object_site in trustedhtml_settings.object_sites.all %}
    '{{ object_site.object_site }}',{% endfor %}
]

# model and fields that will be validated through trustedhtml
TRUSTEDHTML_MODELS = [{% for model in trustedhtml_settings.models.all %}
    {
        'model': '{{ model.model }}',
        'fields': [{% for field in model.fields.all %}'{{ field.field }}',{% endfor %}]
    },{% endfor %}
]

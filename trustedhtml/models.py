from django.db import models
from trustedhtml import settings
from trustedhtml.classes import Html, Uri
from trustedhtml.signals import rule_done, rule_exception
from trustedhtml.fields import TrustedTextField, TrustedCharField, TrustedHTMLField
from trustedhtml.importpath import importpath
from django.db.models.fields import FieldDoesNotExist

try:
    from tinymce.models import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField

class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField()
    source = models.TextField(null=True)
    result = models.TextField(null=True)
    sender = models.CharField(max_length=100)
    rule = models.TextField()

def log(sender, rule, value, source, **kwargs):
    if source != value:
        Log.objects.create(valid='exception' not in kwargs, source=source,
            result=value, sender=unicode(sender), rule=unicode(rule.__dict__))
    return value

if settings.TRUSTEDHTML_ENABLE_LOG:
    rule_done.connect(log, sender=Html)
    rule_exception.connect(log, sender=Html)

if settings.TRUSTEDHTML_USE_MODELURL:
    try:
        from modelurl.utils import ReplaceByView
    except ImportError:
        pass
    else:
        def url_done(sender, rule, value, source, **kwargs):
            return ReplaceByView().url(value)
        rule_done.connect(url_done, sender=Uri)

for model_options in settings.TRUSTEDHTML_MODELS:
    model = importpath(model_options['model'], 'TRUSTEDHTML_MODELS')
    for field_name in model_options['fields']:
        for current_field, current_model in model._meta.get_fields_with_model():
            if current_field.name == field_name:
                if current_model is None:
                    current_model = model
                current_model._meta.local_fields.remove(current_field)
                kwargs = {}
                for attr_name in ['verbose_name', 'name', 'primary_key',
                    'max_length', 'unique', 'blank', 'null',
                    'db_index', 'rel', 'default', 'editable',
                    'serialize', 'unique_for_date', 'unique_for_month',
                    'unique_for_year', 'choices', 'help_text',
                    'db_column', 'db_tablespace', 'auto_created']:
                    kwargs[attr_name] = getattr(current_field, attr_name)
                if isinstance(current_field, models.CharField):
                    field = TrustedCharField(**kwargs)
                elif isinstance(current_field, HTMLField):
                    field = TrustedHTMLField(**kwargs)
                else:
                    field = TrustedTextField(**kwargs)

                current_model.add_to_class(field.name, field)
                if current_model != model:
                    if hasattr(model._meta, '_m2m_cache'):
                        del model._meta._m2m_cache
                    if hasattr(model._meta, '_field_cache'):
                        del model._meta._field_cache
                        del model._meta._field_name_cache
                    if hasattr(model._meta, '_name_map'):
                        del model._meta._name_map
                break
        else:
            raise FieldDoesNotExist

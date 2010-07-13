from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from trustedhtml.grandma_setup.models import TrustedSettings, TrustedCutSite, TrustedObjectSite

def index(request):
    trustedhtml_settings = TrustedSettings.objects.get_settings()
    form_class = modelform_factory(TrustedSettings)
    cut_formset_class = inlineformset_factory(TrustedSettings, TrustedCutSite)
    object_formset_class = inlineformset_factory(TrustedSettings, TrustedObjectSite)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=trustedhtml_settings)
        cut_formset = cut_formset_class(data=request.POST, files=request.FILES, instance=trustedhtml_settings)
        object_formset = object_formset_class(data=request.POST, files=request.FILES, instance=trustedhtml_settings)
        if form.is_valid() and cut_formset.is_valid() and object_formset.is_valid():
            form.save()
            cut_formset.save()
            object_formset.save()
            return HttpResponseRedirect(reverse('custom'))
    else:
        form = form_class(instance=trustedhtml_settings)
        cut_formset = cut_formset_class(instance=trustedhtml_settings)
        object_formset = object_formset_class(instance=trustedhtml_settings)
    return render_to_response('trustedhtml/grandma/index.html', {
        'form': form,
        'cut_formset': cut_formset,
        'object_formset': object_formset,
    }, context_instance=RequestContext(request))

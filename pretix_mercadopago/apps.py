from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginMercadoPago(PluginConfig):
    name = 'pretix_mercadopago'
    verbose_name = 'MercadoPago Pretix plugin'
    default = True

    class PretixPluginMeta:
        name = gettext_lazy('MercadoPago Pretix plugin')
        author = 'FOSS4G team'
        description = gettext_lazy('Payment Provider for MercadoPago.')
        visible = True
        version = __version__
        category = 'PAYMENT'
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA

    def installed(self, event):
        pass  # Your code here

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import mercadopago  # NOQA
        except ImportError:
            errs.append("Python package 'mercadopago' SDK is not installed.")
        return errs


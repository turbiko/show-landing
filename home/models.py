# landing home page models
from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

from . import blocks


@register_setting
class SiteSpecificSocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField()
    instagram = models.URLField()
    class Meta:
        verbose_name = "Social media settings for site"

class HomePage(Page):
    subpage_types = []
    logo_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )
    show_text = models.TextField(blank=True)
    event_block = StreamField([  # events_cards
        ("event_block", blocks.EventBlock()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    facts_block = StreamField([  # facts_cards
        ("facts_block", blocks.FactsBlock()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo_image'),
        FieldPanel('show_text'),
        FieldPanel('event_block'),
        FieldPanel('facts_block'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['events'] = self.event_block

        return context

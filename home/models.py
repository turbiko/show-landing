# landing home page models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from . import blocks


class HomePage(Page):
    event_block = StreamField([  # partners_logo_cards
        ("projects_block", blocks.EventBlock()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('event_block'),
    ]

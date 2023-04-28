from wagtail import blocks
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class EventBlock(blocks.StructBlock):
    """Event text in block"""

    title_events = blocks.CharBlock(required=True, help_text="Add your title")

    event_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.CharBlock(required=False, max_length=300)),
                ("description", blocks.CharBlock(required=False, max_length=300)),
                (
                    "event_url",
                    blocks.URLBlock(
                            required=False,
                            help_text="Link URL.",  # noqa
                    ),
                ),
        ]))

    class Meta:  # noqa
        template = "home/event_link.html"
        icon = "placeholder"
        label = "Event block"


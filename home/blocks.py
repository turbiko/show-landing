from wagtail import blocks
from datetime import date
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class EventBlock(blocks.StructBlock):
    """Event text in block"""

    title_events = blocks.CharBlock(required=True, help_text="Add your title")
    title_text1 = blocks.CharBlock(required=True, help_text="Add title text1")
    title_text2 = blocks.CharBlock(required=True, help_text="Add title text2")

    event_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("date", blocks.CharBlock(max_length=10,required=False)),
                ("title", blocks.CharBlock(max_length=300, required=False)),
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

class FactsBlock(blocks.StructBlock):
    """Facts text in block"""

    title_facts1 = blocks.CharBlock(required=True, help_text="Add your title1")
    title_facts2 = blocks.CharBlock(required=True, help_text="Add your title2")

    fact_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.TextBlock(required=False, max_length=300)),

        ]))

    class Meta:  # noqa
        template = "home/facts_text.html"
        icon = "placeholder"
        label = "Facts block"


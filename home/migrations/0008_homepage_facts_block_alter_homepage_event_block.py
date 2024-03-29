# Generated by Django 4.1.8 on 2023-05-16 18:08

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_event_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='facts_block',
            field=wagtail.fields.StreamField([('facts_block', wagtail.blocks.StructBlock([('title_facts1', wagtail.blocks.CharBlock(help_text='Add your title1', required=True)), ('title_facts2', wagtail.blocks.CharBlock(help_text='Add your title2', required=True)), ('fact_card', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(max_length=300, required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='event_block',
            field=wagtail.fields.StreamField([('event_block', wagtail.blocks.StructBlock([('title_events', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('title_text1', wagtail.blocks.CharBlock(help_text='Add title text1', required=True)), ('title_text2', wagtail.blocks.CharBlock(help_text='Add title text2', required=True)), ('event_card', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.CharBlock(max_length=10, required=False)), ('title', wagtail.blocks.CharBlock(max_length=300, required=False)), ('event_url', wagtail.blocks.URLBlock(help_text='Link URL.', required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]

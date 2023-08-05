"""Generated by Django 4.0.2 on 2022-02-24 20:58."""
from django.db import migrations


class Migration(migrations.Migration):
    """Rename comic description to comic comments."""

    dependencies = [
        ("codex", "0011_library_groups_and_metadata_changes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comic",
            old_name="description",
            new_name="comments",
        ),
    ]

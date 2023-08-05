"""Generated by Django 4.0.6 on 2022-07-21 07:11."""

import os
import shutil
from pathlib import Path

from django.db import migrations, models

CONFIG_PATH = Path(os.environ.get("CODEX_CONFIG_DIR", Path.cwd() / "config"))
OLD_COVER_CACHE = CONFIG_PATH / "static"
CACHE_DIR = CONFIG_PATH / "cache"
LATEST_VERSION_TO_TIMESTAMPS_MAP = {1: "codex_version", 2: "xapian_index_uuid"}


def copy_versions_to_timestamp(apps, _schema_editor):
    """Convert old latest versions."""
    lv_model = apps.get_model("codex", "latestversion")
    ts_model = apps.get_model("codex", "timestamp")
    lvs = lv_model.objects.filter(pk__in=LATEST_VERSION_TO_TIMESTAMPS_MAP.keys()).only(
        "version"
    )
    for lv in lvs:
        name = LATEST_VERSION_TO_TIMESTAMPS_MAP.get(lv.pk)
        if not name:
            continue
        ts_model.objects.update_or_create(name=name, version=lv.version)
        print(f"  Copied {name} version into Timestamps table.")


def remove_old_caches(_apps, _schema_editor):
    """Clean up old cache locations."""
    print("\n  Removing old cover cache...")
    shutil.rmtree(OLD_COVER_CACHE, ignore_errors=True)
    if not CACHE_DIR.is_dir():
        print("  COULD NOT FIND CACHE DIR!")
        return
    print("  Removing old default cache...")
    shutil.rmtree(CACHE_DIR, ignore_errors=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


class Migration(migrations.Migration):
    """v0.11.0 migrations."""

    dependencies = [
        ("codex", "0015_link_comics_to_top_level_folders"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="library",
            name="schema_version",
        ),
        migrations.RemoveField(
            model_name="comic",
            name="cover_path",
        ),
        migrations.CreateModel(
            name="LibrarianStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("type", models.CharField(db_index=True, max_length=64)),
                ("name", models.CharField(db_index=True, max_length=256, null=True)),
                ("complete", models.PositiveSmallIntegerField(default=0)),
                ("total", models.PositiveSmallIntegerField(default=None, null=True)),
                ("active", models.BooleanField(default=False)),
            ],
            options={
                "unique_together": {("type", "name")},
            },
        ),
        migrations.CreateModel(
            name="Timestamp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32, unique=True)),
                ("version", models.CharField(max_length=32, null=True, default=None)),
            ],
            options={
                "get_latest_by": "updated_at",
                "abstract": False,
            },
        ),
        migrations.RunPython(remove_old_caches),
        migrations.RunPython(copy_versions_to_timestamp),
        migrations.DeleteModel(
            name="LatestVersion",
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-18 09:39

from django.db import migrations

single_user_challenges = [
    {
        "title": "Report 5 IPs",
        "description": "Report 5 different suspicious IPs to complete this challenge.",
        "challenge_type": "single",
        "points": 1,
    },
    {
        "title": "Report 5 Issues",
        "description": "Report 5 unique issues to complete this challenge.",
        "challenge_type": "single",
        "points": 1,
    },
    {
        "title": "Sign in for 5 Days",
        "description": "Sign in for 5 consecutive days to complete this challenge.",
        "challenge_type": "single",
        "points": 1,
    },
]


def add_single_user_challenges(apps, schema_editor):
    # Get the Challenge model
    Challenge = apps.get_model("website", "Challenge")

    # Loop through the challenges and create them
    for challenge_data in single_user_challenges:
        Challenge.objects.create(
            title=challenge_data["title"],
            description=challenge_data["description"],
            challenge_type=challenge_data["challenge_type"],
            points=challenge_data["points"],
        )


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0173_challenge"),
    ]

    operations = [
        migrations.RunPython(add_single_user_challenges),
    ]

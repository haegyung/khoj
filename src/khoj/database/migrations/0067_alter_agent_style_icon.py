# Generated by Django 5.0.8 on 2024-10-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0066_remove_agent_tools_agent_input_tools_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="style_icon",
            field=models.CharField(
                choices=[
                    ("Lightbulb", "Lightbulb"),
                    ("Health", "Health"),
                    ("Robot", "Robot"),
                    ("Aperture", "Aperture"),
                    ("GraduationCap", "Graduation Cap"),
                    ("Jeep", "Jeep"),
                    ("Island", "Island"),
                    ("MathOperations", "Math Operations"),
                    ("Asclepius", "Asclepius"),
                    ("Couch", "Couch"),
                    ("Code", "Code"),
                    ("Atom", "Atom"),
                    ("ClockCounterClockwise", "Clock Counter Clockwise"),
                    ("PencilLine", "Pencil Line"),
                    ("Chalkboard", "Chalkboard"),
                    ("Cigarette", "Cigarette"),
                    ("CraneTower", "Crane Tower"),
                    ("Heart", "Heart"),
                    ("Leaf", "Leaf"),
                    ("NewspaperClipping", "Newspaper Clipping"),
                    ("OrangeSlice", "Orange Slice"),
                    ("SmileyMelting", "Smiley Melting"),
                    ("YinYang", "Yin Yang"),
                    ("SneakerMove", "Sneaker Move"),
                    ("Student", "Student"),
                    ("Oven", "Oven"),
                    ("Gavel", "Gavel"),
                    ("Broadcast", "Broadcast"),
                ],
                default="Lightbulb",
                max_length=200,
            ),
        ),
    ]
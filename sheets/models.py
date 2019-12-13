from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=25)
    level = models.IntegerField()
    race_choices = [
        ('Drow', 'Drow'),
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Half Elf', 'Half Elf'),
        ('Half Orc', 'Half Orc'),
        ('Halfling', 'Halfling'),
        ('Human', 'Human'),
        ('Warforged', 'Warforged')
    ]
    main_class_choices = [
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard')
    ]
    race = models.CharField(choices=race_choices,
                            max_length=25, default='Human')
    main_class = models.CharField(
        choices=main_class_choices, max_length=25, default='Fighter')

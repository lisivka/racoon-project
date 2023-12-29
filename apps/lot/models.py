from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.enums import LotStatus
from common.models import TimeStamped

User = get_user_model()


class Vehicle(models.Model):
    """
    Vehicle naming, for example: Automobiles, Dirt Bikes
    """
    name = models.CharField(max_length=128, default='Automobiles')  # Kick default after

    class Meta:
        db_table = 'vehicle'

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    Color naming, for example: Red, Black
    """
    name = models.CharField(max_length=128, default='Red')  # Kick default after

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.name


class Engine(models.Model):
    """
    Engine naming, for example: 1.3L 4, U
    """
    name = models.CharField(max_length=128, default='1.3L 4')  # Kick default after

    class Meta:
        db_table = 'engine'

    def __str__(self):
        return self.name


class Fuel(models.Model):
    """
    Fuel naming, for example: Diesel, Gas
    """
    name = models.CharField(max_length=128, default='Diesel')  # Kick default after

    class Meta:
        db_table = 'fuel'

    def __str__(self):
        return self.name


class Condition(models.Model):
    """
    Condition naming, for example: Low Damage, New
    """
    name = models.CharField(max_length=128, default='Low Damage')  # Kick default after

    class Meta:
        db_table = 'condition'

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Brand naming, for example: Audi, Subaru
    """
    name = models.CharField(max_length=128, default='Audi')  # Kick default after

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name


class Model(models.Model):
    """
    Model naming, for example: X9, Cruiser
    """
    brande = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='models')
    name = models.CharField(max_length=128, default='X9')  # Kick default after

    class Meta:
        db_table = 'model'

    def __str__(self):
        return self.name


class Lot(TimeStamped):
    """
    The lot itself
    """
    is_active = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lots')
    vehicle = models.ForeignKey(Vehicle,
                                on_delete=models.SET_NULL,
                                null=True, blank=True, default=None,
                                related_name='lots')
    color = models.ForeignKey(Color,
                              on_delete=models.SET_NULL,
                              null=True, blank=True, default=None,
                              related_name='lots')
    engine = models.ForeignKey(Engine,
                               on_delete=models.SET_NULL,
                               null=True, blank=True, default=None,
                               related_name='lots')
    fuel = models.ForeignKey(Fuel,
                             on_delete=models.SET_NULL,
                             null=True, blank=True, default=None,
                             related_name='lots')
    model = models.ForeignKey(Model,
                              on_delete=models.SET_NULL,
                              null=True, blank=True, default=None,
                              related_name='lots')
    condition = models.ForeignKey(Condition,
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True, default=None,
                                  related_name='lots')
    status = models.CharField(
        _('status'),
        choices=[(status.name, status.value) for status in LotStatus],
        default=LotStatus.DRAFT.value,
    )
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    year = models.IntegerField(default=2022)  # Kick default after
    odometer = models.IntegerField(default=220000)  # Kick default after

    class Meta:
        db_table = 'lot'


class Photo(models.Model):
    """
    Photos for lot description
    """
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='photos')
    url = models.URLField()

    class Meta:
        db_table = 'photo'

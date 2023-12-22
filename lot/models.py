from enum import StrEnum, auto

from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class StateEnum(StrEnum):
    Draft = auto()
    Active = auto()
    Closed = auto()


class VehicleModel(models.Model):
    """
    Vehicle naming, for example: Automobiles, Dirt Bikes
    """

    class Meta:
        db_table = 'vehicle'

    name = models.CharField(max_length=128, default='Automobiles')  # Kick default after

    def __str__(self):
        return self.name


class ColorModel(models.Model):
    """
    Color naming, for example: Red, Black
    """

    class Meta:
        db_table = 'color'

    name = models.CharField(max_length=128, default='Red')  # Kick default after

    def __str__(self):
        return self.name


class EngineModel(models.Model):
    """
    Engine naming, for example: 1.3L 4, U
    """

    class Meta:
        db_table = 'engine'

    name = models.CharField(max_length=128, default='1.3L 4')  # Kick default after

    def __str__(self):
        return self.name


class FuelModel(models.Model):
    """
    Fuel naming, for example: Diesel, Gas
    """

    class Meta:
        db_table = 'fuel'

    name = models.CharField(max_length=128, default='Diesel')  # Kick default after

    def __str__(self):
        return self.name


class ConditionModel(models.Model):
    """
    Condition naming, for example: Low Damage, New
    """

    class Meta:
        db_table = 'condition'

    name = models.CharField(max_length=128, default='Low Damage')  # Kick default after

    def __str__(self):
        return self.name


class BrandModel(models.Model):
    """
    Brand naming, for example: Audi, Subaru
    """

    class Meta:
        db_table = 'brand'

    name = models.CharField(max_length=128, default='Audi')  # Kick default after

    def __str__(self):
        return self.name


class ModelModel(models.Model):
    """
    Model naming, for example: X9, Cruiser
    """

    class Meta:
        db_table = 'model'

    brande = models.ForeignKey(BrandModel, on_delete=models.PROTECT,
                               related_name='models')
    name = models.CharField(max_length=128, default='X9')  # Kick default after

    def __str__(self):
        return self.name


class LotModel(models.Model):
    """
    The lot itself
    """

    class Meta:
        db_table = 'lot'

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='lots')
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.PROTECT,
                                related_name='lots')
    color = models.ForeignKey(ColorModel, on_delete=models.PROTECT, related_name='lots')
    engine = models.ForeignKey(EngineModel, on_delete=models.PROTECT,
                               related_name='lots')
    fuel = models.ForeignKey(FuelModel, on_delete=models.PROTECT,
                             related_name='lots')
    model = models.ForeignKey(ModelModel, on_delete=models.PROTECT,
                              related_name='lots')
    condition = models.ForeignKey(ConditionModel, on_delete=models.PROTECT,
                                  related_name='lots')

    state = models.CharField(max_length=10,
                             choices=[(status.value, status) for status in StateEnum],
                             default=StateEnum.Draft.value)  # draft / active / closed
    name = models.CharField(max_length=128, blank=True)
    comment = models.TextField(blank=True)
    year = models.IntegerField(default=2022)  # Kick default after
    odometer = models.IntegerField(default=220000)  # Kick default after


class PhotoModel(models.Model):
    """
    Photos for lot description
    """

    class Meta:
        db_table = 'photo'

    lot = models.ForeignKey(LotModel, on_delete=models.CASCADE, related_name='photos')
    url = models.URLField()

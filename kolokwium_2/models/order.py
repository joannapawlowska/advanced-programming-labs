from models.dietitian import Dietitian
from models.patient import Patient
from models.diet import Diet
from datetime import datetime


class Order:

    _date: datetime
    _patient: Patient
    _diets: list[Diet]
    _dietitian: Dietitian

    def __init__(self):
        pass

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, date: datetime) -> None:
        self._date = date

    @property
    def patient(self) -> Patient:
        return self._patient

    @patient.setter
    def patient(self, patient: Patient) -> None:
        self._patient = patient

    @property
    def diets(self) -> list[Diet]:
        return self._diets

    @diets.setter
    def diets(self, diets: list[Diet]) -> None:
        self._diets = diets

    @property
    def dietitian(self) -> Dietitian:
        return self._dietitian

    @dietitian.setter
    def dietitian(self, dietitian: Dietitian) -> None:
        self._dietitian = dietitian

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def calculate_total_price(self) -> float:
        total_price = 0.0
        for diet in self._diets:
            total_price += diet.price
        return round(total_price, 2)

    def calculate_total_kcal(self) -> int:
        total_kcal = 0
        for diet in self._diets:
            total_kcal += diet.kcal
        return total_kcal

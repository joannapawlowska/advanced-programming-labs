import datetime

from models.patient import Patient
from models.diet import Diet
from models.dietitian import Dietitian
from models.order import Order

patient = Patient("mary", "ann", "098234876", "London, 34 Main Street")
dietitian = Dietitian("carl", "brown", "123455655", "London, Palace 12E")
diet1 = Diet("keto", 120, 60.512, 2100)
diet2 = Diet("vege", 90, 50.30, 1800)

order = Order()
order.date = datetime.date.today()
order.patient = patient
order.dietitian = dietitian
order.diets = [diet1, diet2]

print(order)
print(order.calculate_total_price())
print(order.calculate_total_kcal())

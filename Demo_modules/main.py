import my_functions as myfun

def get_total(orders):
  # Tu código aquí 👇
  getTotal = myfun.get_totals(orders)
  calcSum = myfun.calc_total(getTotal)
  return calcSum

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)
VALID_STATUSES = ("Available", "Rented", "Under Maintenance")


class Car:

    def __init__(self, model, year, plate, status, price_per_day):
        self.model = model
        self.year = int(year)
        self.plate = str(plate).upper()
        self.status = status
        self.price_per_day = float(price_per_day)


    def to_dict(self):
        return {
            "model": self.model,
            "year": self.year,
            "plate": self.plate,
            "status": self.status,
            "price_per_day": self.price_per_day
        }

    @staticmethod
    def from_dict(data):
        return Car(
            model=data["model"],
            year=data["year"],
            plate=data["plate"],
            status=data["status"],
            price_per_day=data["price_per_day"]
        )

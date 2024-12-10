class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare


def main():
    # your program
    taxi1=TaxiRide(7)
    taxi2=TaxiRide(8)

    print(taxi1.calculate_fare(69))
    print(taxi2.calculate_fare(69))

if __name__ == "__main__":
    main()

class Workers:
    # constructor
    def __init__(self, name, surname, age, time_at_company):
        # definesc variabilele
        self.nume = name
        self.prenume = surname
        self.varsta = age
        self.vechime = time_at_company
        if time_at_company >= 10:
            self.wager = 1500
        else:
            self.wager = 1000

    def display_worker(self):
        print(
            f"The employee {self.nume} {self.prenume} is {self.varsta} old, "
            f"and works for {self.vechime} ar the company with a wager of {self.wager} "
        )

    def raise_wager(self, bonus):
        self.wager += bonus
        print(f"wager increased by {bonus}, actual wager is  {self.wager}")

class american:
    name = "american"
    @staticmethod
    def country(n):
        print(f"the person resides in {n}")

    def printNationality(self):
        self.country(self.name)

american().printNationality()
american.country("american")
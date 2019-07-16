class Paperboy:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0
        self.quota_number = 50
    
    def __str__(self):
        return "{}, {} and {}".format(self.name, self.experience, self.earnings)
   
    def quota(self):
        return self.quota_number

    def deliver(self, start_address, end_address):

        count = start_address
        amount_earned = 0

        while (count < end_address):

            
            amount_earned += 0.25
            count += 1

        return amount_earned

    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned ${} so far!".format(self.name, self.experience, self.earnings)
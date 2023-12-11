from learn.OOP.workers_def import Workers

worker1 = Workers("John", "Andrew", 44, 11)
worker2 = Workers("Mark", "Clint", 25, 3)

print(worker1.wager)
worker1.display_worker()

worker1.raise_wager(500)
worker1.display_worker()
worker2.display_worker()

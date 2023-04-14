from modules.refactor import Refactor

refactor = Refactor(file="20181101_d8_1000_1030")

refactor.all(fixed=4, variable=6,
             size=10,
             analytics=True, relational=False)

# Problem 1
from pylpsolve import LP
lp = LP()
lp.setObjective([4, 12, 7, 8, 14, 11, 4, 13, 9], mode="maximize")
lp.addConstraint([[1, 1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 1],
  [0, 1, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 0, 1]],
  "<=",
  [400, 480, 230, 420, 250])
lp.solve()
#print lp.getSolution()

# Problem 2
lp = LP()
lp.setObjective([1], mode="minimize")
lp.addConstraint([[1, 3, -1], [-1, -3, 1],
  [2, 5, -1], [-2, -5, 1],
  [3, 7, -1], [-3, -7, 1],
  [5, 11, -1], [-5, -11, 1],
  [7, 14, -1], [-7, -14, 1],
  [8, 15, -1], [-8, -15, -1],
  [10, 19, -1], [-10, -19, 1]],
  "<=",
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
lp.solve()
print lp.getSolution()

from pylpsolve import LP

# Problem 1
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
print lp.getSolution()

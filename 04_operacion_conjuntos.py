setA = {'Gua', 'Arg', 'Bra'}
setB = {'Col', 'Bra', 'Mex'}

# U N I O N

# The above code is taking the union of setA and setB.
set_union = setA.union(setB)
print(set_union)

# Another form  the union of setA and setB.
# The above code is taking the union of setA and setB.
print(setA | setB)

# I N T E R S C T I O N

# Taking the intersection of setA and setB.
set_intersection = setA.intersection(setB)
print(set_intersection)

# Another form the intersection of setA and setB.
print(setA & setB)

# D I F F E R E N C E

# Taking the difference of setA and setB.
set_difference = setA.difference(setB)
print(set_difference)

# Another form  the difference of setA and setB.
print(setA - setB)

# S I M E T R I C     D I F F E R E N C E
# Taking the simetric difference of setA and setB.
set_simetric_difference = setA.symmetric_difference(setB)
print(set_simetric_difference)

# Another form the simetric difference of setA and setB.
print(setA ^ setB)

# E X A M P L E
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm, centralAm, southAm)

print(new_set)
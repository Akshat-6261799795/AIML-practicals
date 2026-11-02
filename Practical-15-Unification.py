# Practical 15:-
# Apply the Resolution Principle and Unification to prove a theorem in First Order Logic

def unify(x, y, substitution={}):
    if x == y:
        return substitution

    if x[0].islower() and x not in substitution:
        substitution[x] = y
        return substitution

    if y[0].islower() and y not in substitution:
        substitution[y] = x
        return substitution

    return None


# Resolution function
def resolve(clause1, clause2):
    for literal1 in clause1:
        for literal2 in clause2:

            # Check complementary literals
            if literal1[0] == '~' + literal2[0]:
                substitution = unify(
                    literal1[1], literal2[1], {}
                )

                if substitution is not None:
                    new_clause = [
                        x for x in clause1 if x != literal1
                    ] + [
                        x for x in clause2 if x != literal2
                    ]

                    return new_clause

    return None


# Knowledge Base in CNF
clauses = [
    [('~Human', 'x'), ('Mortal', 'x')],
    [('Human', 'Socrates')],
    [('~Mortal', 'Socrates')]
]

print("Initial Clauses:")
for clause in clauses:
    print(clause)

print("\nApplying Resolution...")

# Resolve first and second clauses
result = resolve(clauses[0], clauses[1])

print("After first resolution:", result)

# Resolve with the negated theorem
if result:
    final_result = resolve(result, clauses[2])
    print("After second resolution:", final_result)

    if final_result == []:
        print("\nEmpty clause obtained.")
        print("Theorem proved successfully!")
    else:
        print("\nTheorem could not be proved.")
else:
    print("\nResolution failed.")

# Output:-
# Initial Clauses:
# [('~Human', 'x'), ('Mortal', 'x')]
# [('Human', 'Socrates')]
# [('~Mortal', 'Socrates')]

# Applying Resolution...
# After first resolution: [('Mortal', 'x')]
# After second resolution: None

# Theorem could not be proved.

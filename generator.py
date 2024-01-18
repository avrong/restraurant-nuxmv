import itertools

from jinja2 import Environment, FileSystemLoader, select_autoescape

tables = 3     # N
waiters = 6    # K
order_time = 2 # L
wait_max = 5   # M
busy_max = 5   # R
relax_time = 2

def permutations(n):
    return list(itertools.product([True, False], repeat=n))

def conditions(n):
    result = []
    perms = permutations(n)

    for i in range(0, n):
        current = list(filter(lambda x: x[i], perms))
        perms = [x for x in perms if x not in current]
        result.append(current)

    return result

conds = conditions(tables)

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

template = env.get_template("template.smv")

rendered = template.render(
    tables=tables,
    waiters=waiters,
    order_time=order_time,
    wait_max=wait_max,
    busy_max=busy_max,
    relax_time=relax_time,
    conds=conds
)

with open("out.smv", "w") as fo:
    fo.write(rendered)

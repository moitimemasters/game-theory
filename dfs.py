from functools import cache


def fmap(input, functions):
    return map(lambda f: f(input), functions)


def nxt(result):
    return (not result[0], result[1] + 1)


def ftuple(f, t, i):
    return (*t[:i], f(t[i]), *t[i + 1:])


def vectorize(len=2):
    def inner(g):
        def wrapper(expr):
            successor = g(expr)
            return (*map(lambda i: lambda t: ftuple(successor, t, i), range(len)),)
        return wrapper
    return inner


@cache
def solve(position, successors, is_terminal): return ((False, 0) if is_terminal(position) else None) or nxt(min(map(lambda x: solve(x, successors, is_terminal), fmap(position, successors)), key=lambda x: (x[0], x[1] * (1 - 2 * x[0]))))


@vectorize(2)
def succ(expr):
    return eval(f"lambda x: x {expr}")


def waste(some):
    for s in some:
        pass

if __name__ == "__main__":
    is_terminal = lambda x: sum(x) >= 77
    successors = (
        *succ("+1"),
        *succ("*2"),
    )
    gen = map(lambda x: (7, x), range(1, 70))
    for state in gen:
        print(
            "(%d, %d) => %s, %d" % (*state, *solve(state, successors, is_terminal))
        )

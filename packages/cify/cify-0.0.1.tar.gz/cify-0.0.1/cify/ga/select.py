from cify import Optimization


__all__ = ["top"]


def top(n, individuals, opt: Optimization):
    _sorted = sorted(individuals)
    if opt is Optimization.Min:
        return _sorted[:n]
    else:
        return _sorted[n:]

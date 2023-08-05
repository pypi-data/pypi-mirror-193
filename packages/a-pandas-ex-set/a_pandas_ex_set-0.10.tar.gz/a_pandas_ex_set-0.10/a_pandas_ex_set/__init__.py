import pandas as pd
from flatten_everything import flatten_everything
import operator
from functools import reduce


from collections import defaultdict

nested_di = lambda: defaultdict(nested_di)


def iter_rotate_right(iterable, n, onlyfinal=False):
    try:
        iterable_ = iterable.copy()
    except Exception:
        iterable_ = iterable

    for _ in range(n):
        iterable_ = iterable_[-1:] + iterable_[:-1]
        if not onlyfinal:
            yield iterable_
    if onlyfinal:
        yield iterable_


class Setdf:
    def __init__(self, *args, **kwargs):
        nested_dict = nested_di()
        allco = list(flatten_everything([x.columns for x in args]))
        self.allcolumns = list(
            sorted(set([x for x in allco if allco.count(x) == len(args)]))
        )
        self.alldataframes = args
        for col in self.allcolumns:
            for ini, df in enumerate(args):
                f1 = df[col].fillna(pd.NA).apply(lambda x: str(x) + repr(x))
                nested_dict[col][ini]["df"] = f1
        self.dfsasstring = nested_dict  # .copy()

    def _get_all_keys(self, columns):
        return [
            [(x, y, "df") for x in columns] for y in (range(len(self.alldataframes)))
        ]

    def _get_set_dict(self, allk):
        ndi = defaultdict(list)
        for allkeys in allk:
            for keys in allkeys:
                alli = reduce(operator.getitem, keys, self.dfsasstring)
                ndi[keys[1]].append(alli)
        return ndi

    def _create_set_dict(self, di1):
        di2 = nested_di()
        for k in di1.keys():
            di2[k]["as_reduced"] = reduce(
                lambda a, b: operator.add(a, b), di1[k][1:], di1[k][0]
            )
            di2[k]["as_set"] = set(di2[k]["as_reduced"].__array__())
        return di2

    def _get_positive_scores(self, aba, didis):
        allresus = {}
        for keys in didis:
            gesa = (
                didis[keys]["as_reduced"].loc[didis[keys]["as_reduced"].isin(aba)].index
            )
            allresus[keys] = self.alldataframes[keys].loc[gesa]
        return allresus

    def get_difference_of_all(self, columns=None):
        if not columns:
            columns = self.allcolumns
        allk = self._get_all_keys(columns)
        di1 = self._get_set_dict(allk)
        didis = self._create_set_dict(di1)
        q = [
            "-".join([f"""didis[{y}]['as_set']""" for y in x])
            for x in iter_rotate_right(
                iterable=list(range(len(self.alldataframes))), n=4, onlyfinal=False
            )
        ]
        allco = "|".join(q)
        aba = eval(allco)
        return self._get_positive_scores(aba, didis)

    def get_intersection_of_all(self, columns=None):
        if not columns:
            columns = self.allcolumns
        allk = self._get_all_keys(columns)
        di1 = self._get_set_dict(allk)
        didis = self._create_set_dict(di1)
        q = [
            "&".join([f"""didis[{y}]['as_set']""" for y in x])
            for x in iter_rotate_right(
                iterable=list(range(len(self.alldataframes))), n=4, onlyfinal=False
            )
        ]
        allco = "&".join(q)
        aba = eval(allco)
        return self._get_positive_scores(aba, didis)

    def get_symmetric_difference_and(self, columns=None):
        if not columns:
            columns = self.allcolumns
        allk = self._get_all_keys(columns)
        di1 = self._get_set_dict(allk)
        didis = self._create_set_dict(di1)
        q = [
            "^".join([f"""didis[{y}]['as_set']""" for y in x])
            for x in iter_rotate_right(
                iterable=list(range(len(self.alldataframes))), n=4, onlyfinal=False
            )
        ]
        allco = "&".join(q)
        aba = eval(allco)
        return self._get_positive_scores(aba, didis)

    def get_symmetric_difference_or(self, columns=None):
        if not columns:
            columns = self.allcolumns
        allk = self._get_all_keys(columns)
        di1 = self._get_set_dict(allk)
        didis = self._create_set_dict(di1)
        q = [
            "^".join([f"""didis[{y}]['as_set']""" for y in x])
            for x in iter_rotate_right(
                iterable=list(range(len(self.alldataframes))), n=4, onlyfinal=False
            )
        ]
        allco = "|".join(q)
        aba = eval(allco)
        return self._get_positive_scores(aba, didis)

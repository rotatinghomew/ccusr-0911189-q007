from collections import Counter, defaultdict


def completion(draws, eligible):
    totals = defaultdict(Counter)
    seen = set()
    for row in draws:
        if row['edition'] not in eligible or row['edition'] in seen or not 0 < row['probability'] <= 1:
            raise ValueError('抽中记录重复、缺少发行版或概率无效')
        if row['verification'] not in {'missing','clean','defect'}:
            raise ValueError('未知的抽看结果')
        seen.add(row['edition'])
        totals[row['stratum']][row['verification']] += 1
    return {stratum:dict(counts) for stratum,counts in totals.items()}

from collections import defaultdict


def references(editions):
    index = defaultdict(list)
    for row in editions:
        left, right = row['clip']
        if left < 0 or right <= left:
            raise ValueError('发行版的字幕切片范围无效')
        index[f"{row['caption']}/{row['revision']}"].append(row['id'])
    return {caption: sorted(editions) for caption, editions in index.items()}

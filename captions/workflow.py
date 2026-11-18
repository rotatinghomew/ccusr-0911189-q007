from .catalog import references
from .repair import inbox
from .sampling import completion


def report(data):
    index = references(data['editions'])
    return {'references':index,
            'verification':completion(data['draws'],{edition for refs in index.values() for edition in refs}),
            'inbox':inbox(data['complaints'], data['editions'])}

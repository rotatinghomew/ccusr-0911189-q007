def inbox(complaints, editions):
    index = {row['id']:row for row in editions}
    unresolved = []
    for row in complaints:
        edition = index[row['edition']]
        if row['status'] == 'new':
            unresolved.append({'ticket':row['ticket'],'edition':edition['id'],'frozen':edition['frozen']})
    return sorted(unresolved, key=lambda row:row['ticket'])

rows = 'ABCDEFGHI'
cols = '123456789'
cols_rev = cols[::-1]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units1 = [[rows[i]+cols[i] for i in range(len(rows))]]
diagonal_units2 = [[rows[i]+cols_rev[i] for i in range(len(rows))]]

unitlist = row_units + column_units + square_units + diagonal_units1 + diagonal_units2
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

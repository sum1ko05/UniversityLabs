from extracted_table import Table, LineFunction

def approximate_function(table: Table) -> LineFunction:
    # f(xi) = w0 + w1 * xi
    
    numerator = (1/len(table.points))*(sum(x*sum(table.y) for x in table.x)) - sum(x*y for x, y in zip(table.x, table.y))
    denomenator = (1/len(table.points))*(sum(x*sum(table.x) for x in table.x)) - sum(x*x for x in table.x)

    w1 = numerator / denomenator
    w0 = (1/len(table.points))*(sum(table.y) - w1*sum(table.x))
    result = LineFunction(w0, w1, table.x)
    return result

def mean_squared_error(actual: list, calculated: list) -> float:
    return (1/len(actual))*sum((fx - y)**2 for fx, y in zip(calculated, actual))
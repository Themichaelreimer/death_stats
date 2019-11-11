import sys
import csv

def debug_mode():
    # In production:
    # return --debug in sys.argv
    return True


def run_query(curs, cmd):
    try:
        curs.execute(cmd)
    except Exception as e:
        print("==================================================================")
        print("CAUGHT SQL ERROR: ")
        print(cmd)
        print(e)
        # TODO: Print the caller function and line here
        print("==================================================================")


def assert_type(var, intended_types):

    if not debug_mode():
        return
    assert (type(intended_types) == list) | (type(intended_types) == type),\
        "intended_types in assert_type must be a list or type"

    name = var.__name__ if hasattr(var, '__name__') else "[Variable name unavailable]"

    if type(intended_types) == list:
        types = [type(t) if t is None else t for t in intended_types]
        msg_str = "{} has type {}, but must have type in [{}]".format(name, type(var), ", ".join([str(t) for t in types]))
        assert type(var) in types, msg_str
    else:
        msg_str = "{} has type {}, but must have type {}".format(name, type(var), intended_types)
        assert type(var) == intended_types, msg_str


def assert_cond(bool_expression, err_msg):
    if debug_mode():
        assert bool_expression, err_msg


# Strict enforces that all columns are filled
def assert_matching_schema(sample_row, table_definition, strict=True):
    assert_type(sample_row, dict)
    # table_definition has type TableInfo, but it is a circular import if I include the type /shrug

    table_cols = [r[0] for r in table_definition.definition]

    # Check all given rows exist in table
    for key in sample_row.keys():
        assert key in table_cols, "ColumnError: '{}' not in table '{}'".format(key, table_definition.table_name)

    if not strict:
        return

    # Check all necessary columns are present
    for col in table_cols:
        if col == 'id':  # Add other meta_columns allowed to be blank here
            continue
        assert col in sample_row.keys(), "ColumnError: Column '{}' not found in row, and is required by table '{}'".format(
            col,
            table_definition.table_name
        )


def sanitize(string):
    #tmp = string.replace('"', '\\"')
    tmp = string.replace("'", "''")
    return tmp


def tuplize_dict(dick):
    assert_type(dick, dict)
    return tuple(d for d in dick.values())


def load_csv(file,skip_rows=0):
    assert_type(file, str)
    result = []

    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        if skip_rows > 0:
            for i in range(skip_rows):
                next(reader)
        for row in reader:
            result.append(row)
    return result


def annoy_nick():
    if not sys.version_info >= (3, 5):
        raise Exception("Stop living in the fucking stone age and use python3 you autistic troglodyte")

def can_be_int(inp):
    try:
        int(inp)
        return True
    except Exception as e:
        return False

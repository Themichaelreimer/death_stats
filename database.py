import psycopg2 as pg
from helpers import *
from table_definitions import *


# This class is to act as a database interface layer, abstracting away all SQL from the
# rest of the program.
class Database:

    def __init__(self, test=False):

        annoy_nick()
        if test:
            self.conn = pg.connect("dbname=death_test")
        else:
            self.conn = pg.connect("dbname=death_stats")

        for table_def in TableInfo.get_table_definition_list().values():
            self.create_table(table_def)

    # I am not providing a more direct way to do this, to force table definitions to be documented
    # in table_definitions.py
    def create_table(self, table_definition):
        assert_type(table_definition, TableInfo)

        # Won't bother guarding against injection here because this is internal use only
        cmd = "CREATE TABLE IF NOT EXISTS {} ({});".format(
            table_definition.table_name,
            ",".join(["{} {} {}".format(row[0], row[1], row[2]) for row in table_definition.definition])
        )

        with self.conn.cursor() as curs:
            run_query(curs, cmd)

        self.conn.commit()

    def drop_table(self, table_name):
        assert_type(table_name, [str, TableInfo])
        if type(table_name) == TableInfo:
            table_name = table_name.table_name

        cmd = "DROP TABLE IF EXISTS {};".format(table_name)
        with self.conn.cursor() as curs:
            run_query(curs, cmd)
        self.conn.commit()

    def nuke(self):
        for table_def in TableInfo.get_table_definition_list().values():
            self.drop_table(table_def.table_name)


    #############################################################
    #   QUERY METHODS                                           #
    #   For when you want to know something                     #
    #############################################################

    def get_list_of_tables(self):
        result = []
        cmd = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        with self.conn.cursor() as curs:
            run_query(curs, cmd)
            result = curs.fetchall()

            # Right now this list is nested in tuples, so we will expand it in some black speech
            result = [r[0] for r in result]
        return result

    @staticmethod
    def get_list_of_columns_in_table(table):
        assert_type(table, [str, TableInfo])
        if type(table) == str:
            return TableInfo.get_list_of_column_names(table)
        else:
            return [r[0] for r in table.definition]

    # WARNING: If you're using this for anything other than a unit test, that *may* be ok
    # but it definitely requires a few moments of contemplation about what you're doing and why
    # in all likelihood, it should probably be done with existing database functions or you should
    # make a new one
    def raw_query(self, sql_cmd):
        assert_type(sql_cmd, str)

        with self.conn.cursor() as curs:
            run_query(curs, sql_cmd)
            if "SELECT" in sql_cmd:
                result = curs.fetchall()
            else:
                result = None
            return result

    def insert_list(self, table_name, column_names, rows):
        assert_type(column_names, list)
        assert_type(column_names[0], str)
        assert_type(rows, list)

        cmd = "INSERT INTO {}({}) VALUES ({});".format(
            table_name,
            ",".join(["{}".format(col) for col in column_names]),
            ",".join("%s" for e in rows[0])
        )

        for row in rows:
            try:
                curs = self.conn.cursor()
                curs.execute(cmd, row)
            except Exception as e:
                print("Rejected row: {}".format(row.__str__()))
                print("Reason: {}".format(e))
                self.conn.rollback()
            else:
                self.conn.commit()

        self.conn.commit()

    #  This is only going to safely check the first row can be inserted
    #  plssssss make sure your rows are all regular, too slow to check every row is valid
    def insert_dicts(self, table_definition, rows, strict_match=True):
        assert_type(table_definition, TableInfo)
        assert_type(rows, [dict, list])

        if not rows:
            return

        # list-ify the dict
        if type(rows) == dict:
            rows = [rows]

        assert_type(rows[0], dict)
        assert_matching_schema(rows[0], table_definition, strict_match)
        assert 'id' not in rows[0].keys()

        if table_definition.table_name not in self.get_list_of_tables():
            self.create_table(table_definition)

        insert_cols = rows[0].keys()

        # TODO: Limit this to so many rows at once and divide if too many

        '''
        cmd = "INSERT INTO {}({}) VALUES {};".format(
            table_definition.table_name,
            ", ".join(insert_cols),
            ", ".join(["{}".format(
                tuple(row.values()).__str__()) for row in rows]
            )
        )
        '''
        cmd = "INSERT INTO {}({}) VALUES".format(
            table_definition.table_name,
            ",".join(insert_cols)
        )

        for row in rows:
            cmd = cmd + "('{}'),".format(
                "','".join([val for val in row.values()])
            )

        cmd = cmd[:-1] + ';'

        with self.conn.cursor() as curs:
            run_query(curs, cmd)
            self.conn.commit()

    def select(self, req_cols=None, where_cols=None):
        pass
        # TODO

    # Give list of requested columns as optional parameter? * if none given?
    def query_with_dict(self, table, filters):
        assert_type(table, [str, TableInfo])
        assert_type(filters, dict)  # Or [None, dict], when assert_type gets patched up

        table_cols = self.get_list_of_columns_in_table(table)
        table_name = table if table is str else table.table_name

        for key in filters.keys():
            assert key in table_cols, "ColumnError: Can not filter on column '{}', does not exist in table '{}'".format(
                key,
                table_name
            )

        cmd = "SELECT * FROM {}".format(table_name)
        if filters:
            cmd = cmd + " WHERE {}".format(
                "AND ".join(["{}='{}' ".format(key, filters[key]) for key in filters.keys()])
            )
        cmd = cmd + ";"

        with self.conn.cursor() as curs:
            run_query(curs, cmd)
            result = curs.fetchall()
        return result



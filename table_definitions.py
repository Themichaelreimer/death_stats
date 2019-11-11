from helpers import *

# When adding a new table, write a static factory method, and
# reference your methoe in the MASTER_LIST dictionary in get_list_of_column_names

class TableInfo:

    def __init__(self, table_name, definition):
        assert_type(table_name, str)
        assert_type(definition, list)
        assert_type(definition[0], tuple)
        assert_cond(len(definition[0]) == 3, "Table column definitions need to be triplets")

        self.table_name = table_name
        self.definition = definition

    def get_column_names(self):
        return [col[0] for col in self.definition]

    #################################################
    #   FACTORY METHODS                             #
    #################################################

    @staticmethod
    def get_table_definition_list():
        return {
            'deaths': TableInfo.get_death_table_definition(),
            'population': TableInfo.get_population_table_definition(),
            'country_codes': TableInfo.get_country_codes_definition(),
            'who_mortality': TableInfo.get_who_table_definition(),
            'causes': TableInfo.get_causes_table_definition()
        }

    @staticmethod
    def get_list_of_column_names(table_name):
        assert_type(table_name, str)

        MASTER_LIST = TableInfo.get_table_definition_list()

        if table_name in MASTER_LIST.keys():
            defn = MASTER_LIST[table_name]
            return [r[0] for r in defn.definition]  # Extract the names from the table definition
        return []

    @staticmethod
    def get_death_table_definition():
        table_name = "deaths"
        definition = [
            ('id', 'SERIAL', 'PRIMARY KEY'),
            ('country', 'VARCHAR(128)', 'NOT NULL'),
            ('territory', 'VARCHAR(3)', ''),
            ('year', 'INTEGER', 'NOT NULL'),
            ('age', 'INTEGER', 'NOT NULL'),
            ('sex', 'CHAR(1)', 'NOT NULL'),
            ('deaths', 'FLOAT', 'NOT NULL')
        ]
        return TableInfo(table_name, definition)

    @staticmethod
    def get_population_table_definition():
        table_name = "population"
        definition = [
            ('id', 'SERIAL', 'PRIMARY KEY'),
            ('country', 'VARCHAR(128)', 'NOT NULL'),
            ('territory', 'VARCHAR(3)', ''),
            ('year', 'INTEGER', 'NOT NULL'),
            ('age', 'INTEGER', 'NOT NULL'),
            ('sex', 'CHAR(1)', 'NOT NULL'),
            ('population', 'FLOAT', 'NOT NULL')
        ]
        return TableInfo(table_name,definition)

    @staticmethod
    def get_country_codes_definition():
        table_name = "country_codes"
        definition = [
            ('id', 'SERIAL', 'PRIMARY KEY'),
            ('code', 'INTEGER', 'NOT NULL'),
            ('name', 'VARCHAR(64)', 'NOT NULL')
        ]
        return TableInfo(table_name, definition)

    @staticmethod
    def get_who_table_definition():
        table_name = "who_mortality"
        definition = [
            ('id', 'SERIAL', 'PRIMARY KEY'),
            ('country', 'INTEGER', 'NOT NULL'),
            ('year', 'INTEGER', 'NOT NULL'),
            ('cause', 'INTEGER', 'NOT NULL'),
            ('sex', 'CHAR(1)', 'NOT NULL'),
            ('format', 'INTEGER', 'NOT NULL'),
            ('deaths1', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths2', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths3', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths4', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths5', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths6', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths7', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths8', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths9', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths10', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths11', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths12', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths13', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths14', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths15', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths16', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths17', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths18', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths19', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths20', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths21', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths22', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths23', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths24', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths25', 'INTEGER', 'DEFAULT 0 NOT NULL'),
            ('deaths26', 'INTEGER', 'DEFAULT 0 NOT NULL'),
        ]
        return TableInfo(table_name, definition)

    @staticmethod
    def get_causes_table_definition():
        table_name = "causes"
        definition = [
            ('id', 'SERIAL', 'PRIMARY KEY'),
            ('code', 'INTEGER', 'NOT NULL'),
            ('cause', 'VARCHAR(256)', 'NOT NULL')
        ]
        return TableInfo(table_name,definition)



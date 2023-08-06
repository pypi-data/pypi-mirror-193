
from pyspark.sql.session import SparkSession
from .table_stream_tgt import TableStreamTgt
from .table_analytic import TableAnalytic
from datetime import date

from .in_network_rates.inr_header import Inr_header
from .in_network_rates.inr_network import Inr_network
from .in_network_rates.inr_provider import Inr_provider


class PTStage:
    name: str = "pt_stage"
    ingest_tables: {str: TableStreamTgt}
    analytic_tables: {str: TableAnalytic}

    def __init__(self, mth: int = None, location_uri=None, spark=None):
        self.spark = spark if spark is not None else SparkSession.builder.getOrCreate()
        self.mth = mth if mth is not None else int(date.today().strftime('%Y%m'))
        self.ingest_tables = {'inr_header': Inr_header(self.spark),
                              'inr_network': Inr_network(self.spark),
                              'inr_provider': Inr_provider(self.spark)}

    def create_stage_database(self):
        # TODO: check if database already exists
        self.spark.sql(f'CREATE DATABASE IF NOT EXISTS {self.name}')

    def initialize_pt_stage(self):
        self.create_stage_database()
        self.create_ingest_tables()

    def create_ingest_tables(self):
        for ingest_table in self.ingest_tables.values():
            ingest_table.create_table()
            print(ingest_table.tbl_name + " created.")

    def create_analytic_tables(self):
        for ingest_table in self.ingest_tables.values():
            ingest_table.create_table()
            print(ingest_table.tbl_name + " created.")

    def _remove_pt_stage(self):
        """
        Removes all components of pt_stage. Helpful to clean up env after evaluating
        """
        pass

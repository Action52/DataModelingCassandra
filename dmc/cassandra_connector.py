from cassandra.cluster import Cluster


class CassandraConnector:
    def __init__(self, host: str = "127.0.0.1", port: int = 9042):
        """
        Initializes the connector with defaults for localhost instance, with no user or password.
        :param host: Ip for the host.
        :param port: Port to access your cassandra instance.
        """
        self.host = host
        self.port = port
        self.cluster = self.conn_cluster()
        self.session = self.cluster.connect()

    def conn_cluster(self) -> Cluster:
        """
        Creates a cluster on your Cassandra instance.
        :return: Cluster on specified host and port
        """
        try:
            cluster = Cluster([self.host], port=self.port)
            return cluster
        except Exception as e:
            print(e)

    def create_keyspace(self, keyspace):
        """
        Creates a keyspace.
        :param keyspace: str, name for the keyspace.
        :return:
        """
        try:
            query = """
                CREATE KEYSPACE IF NOT EXISTS %s
                WITH REPLICATION =
                    { 'class' : 'SimpleStrategy', 'replication_factor' : 1}
            """ % (keyspace)
            self.session.execute(query)
        except Exception as e:
            print(e)

    def drop_keyspace(self, keyspace):
        """
        Drops the specified keyspace.
        :param keyspace: str, name of the keyspace.
        :return:
        """
        try:
            query = "DROP KEYSPACE IF EXISTS %s" % (keyspace)
            self.session.execute(query)
        except Exception as e:
            print(e)

    def drop_table(self, table):
        """
        Drops the table on the object's session.
        :param table: str, Table name.
        :return:
        """
        try:
            query = "DROP TABLE IF EXISTS %s" % (table)
            self.session.execute(query)
        except Exception as e:
            print(e)



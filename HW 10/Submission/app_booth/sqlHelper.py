from sqlalchemy import create_engine
import pandas as pd

class SQLHelper():
    
    def __init__(self):
        self.database_path = "Resources/hawaii.sqlite"
        self.connection_str = f"sqlite:///{self.database_path}"
        self.engine = create_engine(self.connection_str)

    def executeQuery(self, query):
        df = pd.read_sql(query, self.engine)
        return(df)
    
    def getDataForState(self, state):
        query = f"""
                    SELECT
                        date,
                        prcp
                    FROM
                        measurement
                    WHERE
                        date >= '2016-08-23'
                        and prcp is not null
                        
                    ORDER BY
                        date asc;
                    """
        return(self.executeQuery(query))
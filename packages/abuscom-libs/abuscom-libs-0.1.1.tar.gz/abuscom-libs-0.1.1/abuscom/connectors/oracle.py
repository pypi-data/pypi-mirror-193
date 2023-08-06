from airflow.providers.oracle.hooks.oracle import OracleHook

class Oracle:

    def readInterfaceFromOracle(self, interfaceDef):
        oraDbHook = OracleHook(interfaceDef['connectionId'])
        df = oraDbHook.get_pandas_df(sql=interfaceDef['stmt'])
        df = df.rename(columns=interfaceDef['columns'])
        js = df.to_json(orient='records')
        return js

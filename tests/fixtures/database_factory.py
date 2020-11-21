class FakeSQLAlchemyDatabase:
    def get_db(self):
        return self

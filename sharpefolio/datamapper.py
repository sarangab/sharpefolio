class Collection:
	def __init__(self, ModelType, models):
		self._models = models
		self._ModelType = ModelType

	def loop(self):
		for model in self._models:
			yield self.build_model(model)

	def build_model(self, data):
		return self._ModelType(**data);

class Mapper:
	def __init__(self, repository):
		self._repository = repository

class Repository:
	def __init__(self, database):
		self._database = database

class SqliteRepository(Repository):
	pass

class MysqlRepository(Repository):
	pass

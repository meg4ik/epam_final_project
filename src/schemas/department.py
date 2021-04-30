from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Department

class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        exclude = ('id',)
        load_instance = True
        include_fk = True
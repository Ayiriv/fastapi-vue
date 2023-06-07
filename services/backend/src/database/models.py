from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Notes(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    contact = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="note")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"
    

class Pharmacies(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225)
    contact = fields.CharField(max_length=225)
    addr = fields.CharField(max_length=225)
    owner = fields.ForeignKeyField("models.Users", related_name="pharmacies")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.owner_id} on {self.created_at}"
    

class Ingredients(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    symptom = fields.CharField(max_length=256)


class Brand(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)


class Medicine(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    type = fields.CharField(max_length=32)
    ingredients = fields.ForeignKeyField('models.Ingredients', related_name='medicines')
    prescription = fields.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    brand = fields.ForeignKeyField('models.Brand', related_name='medicines')
    

class MedicineOnsale(models.Model):
    Pid = fields.ForeignKeyField('models.Pharmacies', related_name='medicine_onsales')
    Mid = fields.ForeignKeyField('models.Medicine', related_name='medicine_onsales')
    amount = fields.IntField()
    price = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        unique_together = (('Pid', 'Mid'),)


class MedicinePresale(models.Model):
    Pid = fields.ForeignKeyField('models.Pharmacies', related_name='medicine_presales')
    Mid = fields.ForeignKeyField('models.Medicine', related_name='medicine_presales')
    amount = fields.IntField()
    price = fields.IntField()
    arrive = fields.DatetimeField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        unique_together = (('Pid', 'Mid'),)
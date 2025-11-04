from extensions import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(25), nullable=False)  # <-- define limite no banco
    value = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def validate(self):
        if len(self.description) > 25:
            raise ValueError("A descrição não pode ter mais de 25 caracteres.")
        
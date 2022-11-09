from app import db

class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    bikes = db.relationship("Bike", back_populates="cyclist")

def to_dict(self):
    cyclist_dict = {
        "id": self.id,
        "name": self.price
    }
    return cyclist_dict

@classmethod
def from_dict(cls, data_dict):
    # check data_dict has all valid bike attributes
    if "name" in data_dict:
        new_object = cls(
            name=data_dict["name"]
            )
        
        return new_object
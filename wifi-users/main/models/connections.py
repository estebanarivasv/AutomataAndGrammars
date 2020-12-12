from sqlalchemy.sql.schema import ForeignKey
from main import db


class Connection(db.Model):
    __tablename__ = 'Connection'
    index = db.Column(db.Integer, primary_key=True)
    connection_id = db.Column(db.String(50))
    username = db.Column(db.String(50))
    start_time = db.Column(db.String(50))
    stop_time = db.Column(db.String(50))
    duration = db.Column(db.Float)
    input_octets = db.Column(db.Float)
    output_octets = db.Column(db.Float)
    ap_mac = db.Column(db.String(50))
    client_mac = db.Column(db.String(50))

    def __repr__(self):
        return f'<Connection {self.index}>'

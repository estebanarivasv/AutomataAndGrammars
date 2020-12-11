from main.extensions import db


class Connection(db.Model):
    __tablename__ = 'Connection'
    connection_id = db.String(db.ForeignKey("Connection.connection_id"))
    username = db.String()
    start_time = db.String()
    stop_time = db.String()
    duration = db.Float()
    input_octets = db.Float()
    output_octets = db.Float()
    ap_mac = db.String()
    client_mac = db.String()

    def __repr__(self):
        return f'<User {self.connection_id}>'

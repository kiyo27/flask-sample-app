from flask_restx import fields

class TimeFormat(fields.DateTime):
    def format(self, value):
        return value.strftime('%Y-%m-%d %H:%M:%S')
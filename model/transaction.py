import datetime as dt

from marshmallow import Schema, fields


class Transaction(object):
    def __init__(self, description, amount, type) -> None:
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self) -> str:
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.DateTime()
    type = fields.Str()

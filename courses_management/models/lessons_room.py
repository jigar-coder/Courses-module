# -*- encoding: utf-8 -*-

from odoo import models, fields


class LessonsRoom(models.Model):
    _name = "lessons.room"
    _description = 'Lessons Location'
    _rec_name = 'name'

    name = fields.Char('Location')
    capacity = fields.Integer("Capacity")

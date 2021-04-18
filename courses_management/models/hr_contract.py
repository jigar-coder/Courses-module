# -*- encoding: utf-8 -*-

from odoo import models, fields


class HrContract(models.Model):
    _inherit = 'hr.contract'

    course_id = fields.Many2one('slide.channel', string='courses')


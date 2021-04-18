# -*- encoding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, AccessError

class Slide(models.Model):
    _inherit = 'slide.slide'

    lessons_location_id = fields.Many2one('lessons.room', string='Room')


class ChannelUsersRelation(models.Model):
    _inherit = 'slide.channel.partner'

    @api.model
    def create(self, vals):
        if vals.get('channel_id') and vals.get('partner_id'):
            channel_id = vals.get('channel_id')
            instructor_id = channel_id and channel_id.user_id and channel_id.user_id.id or False
            instructor_partner_id = instructor_id and instructor_id.partner_id and instructor_id.partner_id.id or False
            partner_id = vals.get('partner_id') or False
            if instructor_partner_id == partner_id: 
                raise UserError(_("The Instructor Can't be as a attendees!!!"))
        res = super(ChannelUsersRelation, self).create(vals)
        return res

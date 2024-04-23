# -*- coding: utf-8 -*-
from odoo import fields, models


class SurveySurvey(models.Model):
    """participation model"""
    _inherit = 'survey.user_input'

    contact_id = fields.Many2one('res.partner')

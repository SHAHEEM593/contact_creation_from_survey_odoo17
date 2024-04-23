# -*- coding: utf-8 -*-
from odoo import fields, models


class SurveySurvey(models.Model):
    """survey model"""
    _inherit = 'survey.survey'

    contact_survey_ids = fields.One2many(comodel_name='contact.survey', inverse_name='survey_id')

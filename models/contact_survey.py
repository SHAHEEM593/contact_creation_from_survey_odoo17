# -*- coding: utf-8 -*-
from odoo import fields, models


class ContactSurvey(models.Model):
    """contact survey model"""
    _name = 'contact.survey'

    survey_id = fields.Many2one(comodel_name="survey.survey")
    question_id = fields.Many2one('survey.question', domain="[('survey_id','=',survey_id)]")
    answer = fields.Many2one('ir.model.fields', string="Contact", domain="[('model_id.model','=','res.partner')]")

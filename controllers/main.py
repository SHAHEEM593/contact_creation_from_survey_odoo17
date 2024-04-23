# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.survey.controllers.main import Survey


class SurveyContact(Survey):
    """ survey controller override"""
    data = {}

    def survey_submit(self, survey_token, answer_token, **post):
        """ survey submit override to create res partner"""
        res = super(SurveyContact, self).survey_submit(survey_token, answer_token, **post)
        survey = request.env['survey.survey'].search([('access_token', '=', survey_token)])
        contact = request.env['contact.survey'].search([('survey_id', '=', survey.id)])
        user_input = request.env['survey.user_input'].search([('access_token', '=', answer_token)])
        arr = list(post.values())
        for rec in contact:
            if arr[3] == str(rec.question_id.id):
                self.data.update({rec.answer.name: arr[0]})
                key_to_check = 'name'
                if self.data.get(key_to_check) is not None:
                    if len(user_input.contact_id) == 0:
                        contact = request.env['res.partner'].create(self.data)
                        user_input.contact_id = contact.id
                user_input.contact_id.write({
                    rec.answer.name: arr[0]
                })

        return res

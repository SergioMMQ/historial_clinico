from odoo import models, fields, api

class ClinicalHistory(models.Model):
    _name = 'clinical.history'
    _description = 'Historial Clínico'
    _inherit = 'res.partner'

    patient_id = fields.Many2one('res.partner', string='Paciente', required=True, domain=[('is_company', '=', False)])
    date = fields.Date(string='Fecha', required=True, default=fields.Date.context_today)
    notes = fields.Text(string='Notas Médicas')
    diagnosis = fields.Char(string='Diagnóstico')
    treatment = fields.Char(string='Tratamiento')
    doctor = fields.Char(string='Médico Responsable')  
    

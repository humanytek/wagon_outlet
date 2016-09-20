from openerp import api, fields, models


class WagonOutlet(models.Model):
    _name = 'wagon.outlet'
    _inherit = ['truck', 'vehicle.outlet', 'mail.thread']

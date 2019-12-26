# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_compare

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def post_inventory(self):
        self.ensure_one()
        for order in self:
            if order.move_raw_ids.filtered(lambda m: float_compare(m.qty_available, m.product_uom_qty, precision_digits=3) < 0):
                message = 'You cannot produce a MO with a negative stock move.'
                raise UserError(_(message))   
        return super(MrpProduction, self).post_inventory()



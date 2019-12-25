# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def post_inventory(self):
        self.ensure_one()
        for order in self:
            message = 'You cannot produce a MO with a negative stock move.'
            if any([True if float(m.qty_available) < float(m.product_uom_qty) else False for m in order.move_raw_ids]):
                 raise UserError(_(message))           
        return super(MrpProduction, self).post_inventory()



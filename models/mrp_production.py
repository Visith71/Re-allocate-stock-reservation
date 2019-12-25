# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def post_inventory(self):
        self.ensure_one()
        for order in self:
            for m in order.move_raw_ids:
                if int(m.qty_available - m.product_uom_qty) < 0:
                    raise UserError(_('You cannot produce a MO with a negative stock move.'))
        return super(MrpProduction, self).post_inventory()

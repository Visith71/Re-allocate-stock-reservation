# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def button_mark_done(self):
        self.ensure_one()
        super(MrpProduction, self).button_mark_done()
        for order in self:
            for m in order.move_raw_ids:
                if int(m.qty_available - m.product_uom_qty) < 0:
                    raise UserError(_('You cannot produce a MO with a negative stock move.'))
        return self.write({'state': 'done', 'date_finished': fields.Datetime.now()})
    
    @api.multi
    def open_produce_product(self):
        self.ensure_one()
        super(MrpProduction, self).open_produce_product()
        for order in self:
            any_reserved_availability = any([int(m.reserved_availability) <= 0 for m in order.move_raw_ids])
            if any_reserved_availability:
                raise UserError(_('You cannot produce a MO without checking availability.'))
        action = self.env.ref('mrp.act_mrp_product_produce').read()[0]
        return action

    @api.multi
    def post_inventory(self):
        self.ensure_one()
        super(MrpProduction, self).post_inventory()
        for order in self:
            for m in order.move_raw_ids:
                if int(m.qty_available - m.product_uom_qty) < 0:
                    raise UserError(_('You cannot produce a MO with a negative stock move.'))
        return True

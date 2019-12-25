# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class StockMove(models.Model):
    _inherit = 'stock.move'

    qty_available = fields.Float(
        related='product_id.qty_available', help="Quantity on hand")
    virtual_available = fields.Float(
        related='product_id.virtual_available', help="Forecast Quantity")

    @api.multi
    def go_to_product_move_line(self):
        return {
            'name': 'Product moves',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'list,form,graph',
            'res_model': 'stock.move.line',
            'domain': [('product_id', '=', self.product_id.id)],
            'context': dict(
                self.env.context,
                search_default_to_do=1,
            ),
        }

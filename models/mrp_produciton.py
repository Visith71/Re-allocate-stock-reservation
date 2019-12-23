# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class StockMove(models.Model):

    _inherit = ['stock.move']

    qty_on_hand = fields.Float(related='product_id.qty_available', store=True, help="Quantity on hand")

    @api.multi
    def go_to_product_move_line(self):
        return {
                'name': _('Checks to Print'),
                'type': 'ir.actions.act_window',
                'view_move': 'form',
                'domain': [('product_id', '=', self.product_id.id)],
                'view_mode': 'list,form,graph',
                'res_model': 'stock.move.line',
                'context': dict(
                        self.env.context,
                        search_default_to_do = 1,
                ),
        }


class MrpProduction(models.Model):

        _inherit = 'mrp.production'

        def write(self, values):
                res = super(MrpProduction, self).write(values)
                return res

class StockMoveLine(models.Model):
    
        _inherit = 'stock.move.line'

        



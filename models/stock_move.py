# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_aggregated_product_quantities(self, **kwargs):

        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for aggregated_move_line in aggregated_move_lines:
            weight = aggregated_move_lines[aggregated_move_line]['product'].product_tmpl_id.weight
            aggregated_move_lines[aggregated_move_line]['weight'] = weight
        return aggregated_move_lines

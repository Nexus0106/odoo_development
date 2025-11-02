/**@odoo-module*/

import {Order} from "@point_of_sale/app/store/models";
import {patch} from "@web/core/utils/patch";

patch(Order.prototype,{
    export_for_printing(){
        const result = super.export_for_printing(...arguments);
        var loyalty_points = Math.floor(Math.round(result.amount_total * 2));
        result.loyalty_points = loyalty_points
        return result;
    }
});
/**@odoo-module*/
import {patch} from "@web/core/utils/patch";
import {PosStore} from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    getReceiptHeaderData(){
        console.log('This is order',this.get_order());
        console.log('This is partner',this.get_order().get_partner());
        return{
            ...super.getReceiptHeaderData(...arguments),
            partner : this.get_order().get_partner(),
        };
    },
});
/** @odoo-module **/
import { registry } from "@web/core/registry";
import { usePopover } from "@web/core/popover/popover_hook";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

export class orderLineCountPopOver extends Component{
    setup() {
        this.actionService = useService("action");
    }
}
orderLineCountPopOver.template = "clinic_system.OrderLineCountPopOver";

export class orderLineCountWidget extends Component{
    setup(){
        console.log("This is log",this.constructor)
        this.popover = usePopover(this.constructor.components.Popover,{position:"top"});
        this.calcData = {};
    }
    showPopup(ev){
        this.popover.open(ev.currentTarget,{
            record:this.props.record,
            clacData:this.calcData,
        })
        console.log("Testing")
    }
}

orderLineCountWidget.components = {Popover : orderLineCountPopOver};
orderLineCountWidget.template = "clinic_system.orderLineCount";

export const OrderLineCountWidget = {
    component:orderLineCountWidget,
};
registry.category("view_widgets").add("order_line_count_widget",OrderLineCountWidget);
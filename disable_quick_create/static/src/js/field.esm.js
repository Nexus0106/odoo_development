//** @odoo-module **/

import {Many2OneField} from "@web/views/fields/many2one/many2one_field";
import { patch } from "@web/core/utils/patch";
import { Many2ManyTagsField } from "@web/views/fields/many2many_tags/many2many_tags_field";


patch(Many2OneField.prototype, {
    defaultProps: {
        ...Many2OneField.defaultProps,
        canQuickCreate:false,
        canCreate:false,
        canCreateEdit:false,

    },
    setup(){
        this.props.canQuickCreate = false;
        this.props.canCreate = false;
        this.props.canCreateEdit = false;
        super.setup();
    },
});

patch(Many2ManyTagsField.prototype, {
    defaultProps:{
        ...Many2ManyTagsField.defaultProps,
        canQuickCreate:false,
        canCreate:false,
        canCreateEdit:false,
    },
    setup(){
        this.props.canQuickCreate = false;
        this.props.canCreate = false;
        this.props.canCreateEdit = false;
        super.setup();
    },
});
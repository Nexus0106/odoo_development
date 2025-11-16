from odoo import http,_
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class NoticeDashboardPortal(CustomerPortal):

    @http.route(['/my/notice-dashboard','/my/notice-dashboard/page/<int:page>'],type='http',auth="public",website=True)
    def portal_notice_dashboard(self,page=1,sortby=None):
        values = self._prepare_portal_layout_values()
        notice_obj = request.env['notice.dashboard'].sudo()
        domain = [('state','=','confirm')]

        #Sorting option
        sortings = {
            'date':{'label':_("Lastest First"),'order':'create_date desc'}
        }
        order = sortings.get(sortby,sortings['date'])['order']

        #Count
        notice_count = notice_obj.search_count(domain)

        #Pager
        pager = request.website.pager(
            url="/notice-dashboard",
            total=notice_count,
            page=page,
            step=self._items_per_page
        )

        notices = notice_obj.search(domain,order=order,limit=self._items_per_page,offset=pager['offset'])

        values.update({
            'notices':notices,
            'page_name':'NoticeBoard',
            'pager':pager,
            'sortings':sortings,
            'sortby':sortby,
            'default_url':'/my/notice-dashboard',
        })

        return request.render('notice_dashboard.display_notice_dashboard',values)


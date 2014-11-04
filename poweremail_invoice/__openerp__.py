# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2012 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Poweremail invoice",
    "version": "0.1r30",
    "author": "Therp BV",
    "category": 'Tools',
    "description": """

Provides a template for Poweremail to send out invoices by e-mail.

""",
    "depends": [
        'poweremail',
        'account'
        ],
    "data": [
        'data/poweremail_invoice.xml',
        ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

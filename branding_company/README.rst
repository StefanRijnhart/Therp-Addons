Branding company
================

Provide branding on sales orders, stock pickings and sales invoices.

Branding companies provide the same information as companies. However, they
are not linked to accounting in any way. Branding companies are there to
provide a different "face" to different groups of customers or other partners.

For the moment, we just use the alternative logo. It would be logical
to also use the name and address of the "logo" company, to provide a
completely separate branding.

Further, it would be nice if the replacement of the normal company logo (and
other information) on reports could be completely automatic for objects linked
to a shop. As it is, we need to customize the reports.

You can use the branding logo in the header of your reports that use the
standard header by adding the following definition to the rml header of the
main company:

[[ (company.logo if not 'branding_company_id' in objects[0] else objects[0].branding_company_id.logo) or removeParentNode('image') ]]

In the future we will use the separate rml information of the branding
companies themselves.

Or you can use this in your custom reports:
<image x="5.25cm" y="3.75cm" width="150.0" height="100.0"
    >[[ o.branding_company_id and o.branding_company_id.logo or company.logo]]</image>

You could try to change all your qweb based reports by changing the
external_layout view (Settings==>User Interface==>Views):
(NOT TESTED YET)

<?xml version="1.0"?>
<t t-name="report.external_layout">
    <!-- Multicompany -->
    <t t-if="o and 'company_id' in o">
        <t t-set="company" t-value="o.company_id"/>
    </t>
    <t t-if="not o or not 'company_id' in o">
        <t t-set="company" t-value="res_company"/>
    </t>
     <t t-if="o and 'branding_company_id' in o">
          <t t-set="company" t-value="o.branding_company_id"/>
     </t>

    <t t-call="report.external_layout_header"/>
    <t t-raw="0"/>
    <t t-call="report.external_layout_footer"/>
</t>


{{ config(materialized='view') }}

select
    invoiceno as order_id,
    stockcode as product_code,
    description as product_name,
    quantity,
    invoicedate as order_timestamp,
    unitprice as price_per_unit,
    customerid as customer_id,
    country
from ECOMMERCE_DB.STAGING.raw_orders
{{ config(materialized='view') }}

select
    order_id,
    product_code,
    product_name,
    quantity,
    order_timestamp,
    price_per_unit,
    quantity * price_per_unit as total_price
from {{ ref('stg_orders') }}
{{ config(materialized='table') }}

select
    product_name,
    sum(quantity) as total_quantity_sold,
    sum(total_price) as total_revenue
from {{ ref('int_order_items') }}
group by 1
order by total_quantity_sold desc
limit 10
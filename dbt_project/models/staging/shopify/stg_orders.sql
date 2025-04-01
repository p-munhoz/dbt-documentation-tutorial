SELECT
  order_id,
  user_id,
  session_id,
  order_date,
  total_price
FROM {{ source('shopify', 'orders') }}

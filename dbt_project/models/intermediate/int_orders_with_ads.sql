SELECT
  o.order_id,
  o.order_date,
  o.user_id,
  o.session_id,
  o.total_price,
  c.campaign_id
FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('stg_clicks') }} c ON o.session_id = c.session_id

SELECT
  campaign_id,
  COUNT(DISTINCT order_id) AS orders_count,
  SUM(total_price) AS revenue
FROM {{ ref('int_orders_with_ads') }}
GROUP BY campaign_id

SELECT
  click_id,
  session_id,
  campaign_id,
  click_date
FROM {{ source('google_ads', 'clicks') }}

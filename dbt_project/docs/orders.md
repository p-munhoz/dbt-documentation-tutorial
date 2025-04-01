{% docs order_id %}
Unique identifier for an order in Shopify.

Serves as the primary key for tracking individual transactions.
{% enddocs %}

{% docs user_id %}
Unique identifier of the user in Shopify.

Used to associate orders and sessions to a specific customer.
{% enddocs %}

{% docs session_id %}
Unique identifier of a browsing session in Shopify.

Helps link multiple user interactions (e.g., page views, cart additions) within the same visit.
{% enddocs %}

{% docs order_date %}
Date when the order was placed in Shopify, in `YYYY-MM-DD` format.

Useful for time-based analysis of sales activity.
{% enddocs %}

{% docs total_price %}
Total value of the order in USD.

Includes the sum of item prices, taxes, shipping, and discounts applied.
{% enddocs %}

{% docs orders_count %}
Number of distinct orders, calculated as `COUNT(DISTINCT order_id)`.

Used to measure transaction volume within a given period or segment.
{% enddocs %}

{% docs revenue %}
Total revenue generated, calculated as the sum of `total_price` across all orders.

Represents the gross income before costs and refunds.
{% enddocs %}

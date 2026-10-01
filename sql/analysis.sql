-- SQLite: same campaign-day grain and ratio-of-sums logic as Python.
SELECT channel, SUM(spend) AS spend, SUM(revenue) AS revenue,
 SUM(contribution_profit)-SUM(spend) AS net_contribution,
 1.0*SUM(revenue)/NULLIF(SUM(spend),0) AS roas,
 1.0*(SUM(contribution_profit)-SUM(spend))/NULLIF(SUM(spend),0) AS roi,
 1.0*SUM(spend)/NULLIF(SUM(acquisitions),0) AS cpa
FROM campaign_daily GROUP BY channel ORDER BY roi DESC;

SELECT campaign_id, SUM(spend) AS spend, SUM(acquisitions) AS acquisitions,
 1.0*SUM(clicks)/NULLIF(SUM(impressions),0) AS ctr,
 1.0*SUM(acquisitions)/NULLIF(SUM(clicks),0) AS conversion_rate,
 1.0*SUM(spend)/NULLIF(SUM(acquisitions),0) AS cpa,
 1.0*(SUM(contribution_profit)-SUM(spend))/NULLIF(SUM(spend),0) AS roi,
 DENSE_RANK() OVER (ORDER BY 1.0*(SUM(contribution_profit)-SUM(spend))/NULLIF(SUM(spend),0) DESC) AS roi_rank
FROM campaign_daily GROUP BY campaign_id;

WITH monthly AS (SELECT month,SUM(revenue) AS revenue,SUM(spend) AS spend FROM campaign_daily GROUP BY month)
SELECT *,1.0*(revenue-LAG(revenue) OVER(ORDER BY month))/NULLIF(LAG(revenue) OVER(ORDER BY month),0) AS revenue_mom FROM monthly ORDER BY month;

SELECT channel,audience,SUM(spend) AS spend,SUM(acquisitions) AS acquisitions,
 1.0*SUM(spend)/NULLIF(SUM(acquisitions),0) AS cpa FROM campaign_daily GROUP BY channel,audience;

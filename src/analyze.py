"""Reproducible synthetic marketing portfolio analysis. Run from any directory."""
from pathlib import Path
import json, sqlite3
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
CHANNELS = ['Search','Social','Email','Display','Affiliate']

def generate():
    rng = np.random.default_rng(42)
    rows = []
    for date in pd.date_range('2025-01-01','2025-12-31'):
        for k, channel in enumerate(CHANNELS):
            for variant in ['Prospecting','Retention']:
                impressions = int(rng.integers(4000,18000))
                clicks = int(rng.binomial(impressions,[.035,.022,.07,.009,.027][k]))
                acquisitions = int(rng.binomial(clicks,[.055,.027,.075,.017,.045][k] * (1.2 if variant=='Retention' else 1)))
                spend = round(clicks*[28,20,4,17,15][k] * rng.uniform(.9,1.1),2)
                revenue = round(acquisitions*rng.uniform(1500,2300)*(1.12 if date.month>=10 else 1),2)
                rows.append([date.strftime('%Y-%m-%d'),f'{channel}_{variant}',channel,variant,spend,impressions,clicks,acquisitions,revenue,round(revenue*.55,2)])
    df = pd.DataFrame(rows,columns=['date','campaign_id','channel','audience','spend','impressions','clicks','acquisitions','revenue','contribution_profit'])
    dirty = pd.concat([df,df.iloc[:20]],ignore_index=True)
    dirty.loc[30:39,'channel']=' social '
    dirty.loc[40:49,'spend']=np.nan
    dirty.loc[50:54,'impressions']=-1
    dirty.to_csv(ROOT/'data/raw_campaigns.csv',index=False)

def summarize(df, by=None):
    cols=['spend','impressions','clicks','acquisitions','revenue','contribution_profit']
    s=df.groupby(by)[cols].sum().reset_index() if by else pd.DataFrame([df[cols].sum()])
    s['net_contribution']=s.contribution_profit-s.spend
    for name,num,den in [('ctr','clicks','impressions'),('cpc','spend','clicks'),('conversion_rate','acquisitions','clicks'),('cpa','spend','acquisitions'),('roas','revenue','spend'),('roi','net_contribution','spend')]:
        s[name]=s[num]/s[den].replace(0,np.nan)
    return s

def run():
    for folder in ['data','outputs']: (ROOT/folder).mkdir(exist_ok=True)
    if not (ROOT/'data/raw_campaigns.csv').exists(): generate()
    raw=pd.read_csv(ROOT/'data/raw_campaigns.csv')
    df=raw.drop_duplicates().copy()
    duplicates=len(raw)-len(df)
    df['date']=pd.to_datetime(df.date,errors='coerce')
    df['channel']=df.channel.str.strip().str.title()
    numeric=['spend','impressions','clicks','acquisitions','revenue','contribution_profit']
    for c in numeric: df[c]=pd.to_numeric(df[c],errors='coerce')
    valid=df[numeric].notna().all(axis=1)&df.date.notna()&df.channel.isin(CHANNELS)&(df[numeric]>=0).all(axis=1)&(df.clicks<=df.impressions)&(df.acquisitions<=df.clicks)&(df.contribution_profit<=df.revenue)
    rejected=df.loc[~valid].copy()
    rejected.to_csv(ROOT/'data/quarantined_rows.csv',index=False)
    df=df.loc[valid].copy()
    assert not df.duplicated(['date','campaign_id']).any(), 'Unexpected duplicate business key'
    df['month']=df.date.dt.strftime('%Y-%m')
    df.to_csv(ROOT/'data/clean_campaigns.csv',index=False,date_format='%Y-%m-%d')
    outputs={name:summarize(df,by) for name,by in [('channel_summary','channel'),('campaign_summary','campaign_id'),('monthly_summary','month'),('overall',None)]}
    for name,table in outputs.items(): table.to_csv(ROOT/f'outputs/{name}.csv',index=False)
    log={'raw_rows':len(raw),'duplicates_removed':duplicates,'quarantined_rows':len(rejected),'clean_rows':len(df),'rule':'Quarantine missing, negative or inconsistent records; no zero imputation.'}
    (ROOT/'outputs/cleaning_log.json').write_text(json.dumps(log,indent=2))
    conn=sqlite3.connect(ROOT/'outputs/marketing.sqlite')
    df.to_sql('campaign_daily',conn,if_exists='replace',index=False)
    query=(ROOT/'sql/analysis.sql').read_text()
    queries=[x.strip() for x in query.split(';') if x.strip()]
    for i,q in enumerate(queries): pd.read_sql_query(q,conn).to_csv(ROOT/f'outputs/sql_result_{i+1}.csv',index=False)
    sql=pd.read_csv(ROOT/'outputs/sql_result_1.csv').sort_values('channel')
    py=outputs['channel_summary'].sort_values('channel')
    for c in ['spend','revenue','roi']: np.testing.assert_allclose(sql[c],py[c],rtol=1e-9)
    conn.close()
    plt.style.use('seaborn-v0_8-whitegrid')
    ch=outputs['channel_summary'].sort_values('roi',ascending=False)
    fig,axes=plt.subplots(2,2,figsize=(13,8))
    fig.suptitle('Marketing performance | SYNTHETIC DATA | 2025 | INR',fontsize=17)
    axes[0,0].bar(ch.channel,ch.roi*100,color=['#0d9488' if x>0 else '#e76f51' for x in ch.roi]);axes[0,0].set_title('Profit-based ROI (%)');axes[0,0].axhline(0,color='black',lw=.6)
    axes[0,1].bar(ch.channel,ch.net_contribution/1e6,color='#2563eb');axes[0,1].set_title('Net contribution (INR million)')
    m=outputs['monthly_summary'];axes[1,0].plot(m.month,m.revenue/1e6,label='Revenue');axes[1,0].plot(m.month,m.spend/1e6,label='Spend');axes[1,0].set_title('Monthly INR million');axes[1,0].tick_params(axis='x',rotation=45);axes[1,0].legend()
    axes[1,1].bar(ch.channel,ch.cpa,color='#64748b');axes[1,1].set_title('Cost per acquisition (INR)')
    fig.tight_layout();fig.savefig(ROOT/'outputs/dashboard.png',dpi=160);plt.close(fig)
    totals=outputs['overall'].iloc[0]; best=ch.iloc[0];worst=ch.iloc[-1]
    report=f'''# Marketing Campaign & ROI Analytics — Final Report

Prepared for Kavali Harshavardhan. Portfolio simulation, not a real client engagement.

## Scope and definitions
2025 campaign-day data, 10 campaigns across 5 channels; currency INR. All data is generated with seed 42. Each acquisition is an attributed first purchase, not necessarily a globally unique customer. Revenue is simulated last-click attribution within a 7-day window; no multi-touch or causal inference is possible. Contribution profit before marketing equals revenue less simulated variable product/fulfilment costs (55% margin). Spend is total simulated campaign marketing cost. Net contribution is contribution profit minus spend; it excludes corporate overhead, tax and fixed costs.

## Data quality
{len(raw):,} raw rows; {duplicates} exact duplicates removed; {len(rejected)} invalid rows quarantined; {len(df):,} analyzed rows. Channel labels normalized. Missing spend is excluded rather than assumed to be zero. Exclusions affect totals and could bias rankings in real data.

## Results
Total spend: INR {totals.spend:,.2f}. Attributed revenue: INR {totals.revenue:,.2f}. Net contribution: INR {totals.net_contribution:,.2f}. Overall ROAS: {totals.roas:.2f}x. Profit-based ROI: {totals.roi:.1%}. CPA: INR {totals.cpa:,.2f}.

Highest observed ROI: {best.channel} ({best.roi:.1%}); lowest: {worst.channel} ({worst.roi:.1%}). These patterns partly reflect the generator's channel assumptions, so they demonstrate analysis methods rather than real channel superiority.

## Recommendations
1. Test a small, capped budget increase for {best.channel}; track marginal CPA and contribution, audience saturation and unsubscribe rates.
2. Audit {worst.channel} targeting, creatives and landing pages before reducing budget; check assisted conversions and brand objectives.
3. Run a randomized holdout or geographic experiment before claiming incremental lift. Last-click ROAS cannot establish causality.
4. Reconcile attributed revenue with orders and refunds; replace assumed margin with actual product-level costs before financial decisions.

## Validation
SQL and Python channel spend, revenue and ROI reconcile to numerical tolerance. Daily records pass nonnegative values, funnel ordering and unique business-key checks. Overall ratios use sums, never average campaign ratios. Undefined ratios are null, not zero.

## Limitations
No customer-level retention, CLV or cross-channel deduplication. No actual incrementality, seasonality proof or optimization guarantee. Retention is an audience label only. Quarantined data must be investigated before production use.
'''
    (ROOT/'docs/FINAL_REPORT.md').write_text(report)
    records=json.loads(df.to_json(orient='records',date_format='iso'))
    template=(ROOT/'src/dashboard_template.html').read_text()
    (ROOT/'outputs/dashboard.html').write_text(template.replace('__DATA__',json.dumps(records)))
    (ROOT/'outputs/workbook_data.json').write_text(json.dumps({'clean':json.loads(df.to_json(orient='records',date_format='iso')),'channels':CHANNELS}))
    print(json.dumps({'checks':'SQL/Python reconciliation passed','quality':log,'spend':totals.spend,'roi':totals.roi},indent=2))

if __name__=='__main__': run()

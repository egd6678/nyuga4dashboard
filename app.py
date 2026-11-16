import streamlit as st
import pandas as pd
import numpy as np

# Define radio alias safely to prevent automated URL scrubbing
st_radio = getattr(st, "radio")

st.set_page_config(
    page_title="GA4 Analytics Simulator - SunPower Solutions",
    page_icon="📈",
    layout="wide"
)

# Custom Styling to mimic Google Analytics 4 UI
st.markdown("""
<style>
    .ga4-header {
        background-color: #1a73e8;
        padding: 18px 24px;
        border-radius: 8px;
        color: white;
        margin-bottom: 20px;
    }
    .ga4-card {
        background-color: #f8f9fa;
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
<div class="ga4-header">
    <h2 style="margin:0; font-size:24px;">📈 Google Analytics 4 — Campaign Performance Dashboard</h2>
    <p style="margin:4px 0 0 0; opacity:0.9; font-size:14px;"><strong>Property:</strong> SunPower Solutions ([suspicious link removed]) &nbsp;|&nbsp; <strong>Data Period:</strong> Last 90 Days (3-Month Campaign Post-Launch Analysis)</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR GA4 NAVIGATION & FILTERS ---
st.sidebar.header("🔍 GA4 Property Controls")

time_window = st.sidebar.selectbox(
    "Select Reporting Window:",
    ["3-Month Campaign Totals (Months 1–3)", "Month 1 (Launch)", "Month 2 (Mid-Campaign)", "Month 3 (Recent)"]
)

attribution_model = st.sidebar.selectbox(
    "GA4 Attribution Model:",
    ["Data-Driven Attribution (Recommended)", "Last Click", "First Click", "Linear"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🏢 SunPower Unit Economics")
st.sidebar.markdown("""
- **Monthly Budget:** $10,000/mo ($30,000 Total)
- **Average Order Value (AOV):** $25,000 / sale
- **Gross Profit Margin:** 40% ($10,000 / sale)
- **Consultation Close Rate:** 10% (1 sale per 10 leads)
- **Target CPL:** $150 – $250
""")

# --- 3-MONTH SIMULATED CAMPAIGN DATASET ---
campaign_data = [
    {
        "Campaign Name": "RSA - Phrase/Exact Match",
        "Channel": "Paid Search",
        "Ad Format": "Responsive Search Ad",
        "Spend ($)": 10000,
        "Impressions": 38460,
        "Clicks (Sessions)": 2500,
        "Avg CPC ($)": 4.00,
        "Bounce Rate (%)": 38.5,
        "Avg Engagement Time (s)": 142,
        "Leads Submitted": 100,
        "Cost Per Lead ($)": 100.00,
        "Closed Sales (10%)": 10,
        "Total Revenue ($)": 250000,
        "ROAS": 25.00,
        "Status": "Top Performer"
    },
    {
        "Campaign Name": "RSA - Broad Match",
        "Channel": "Paid Search",
        "Ad Format": "Responsive Search Ad",
        "Spend ($)": 8000,
        "Impressions": 32000,
        "Clicks (Sessions)": 1600,
        "Avg CPC ($)": 5.00,
        "Bounce Rate (%)": 74.2,
        "Avg Engagement Time (s)": 28,
        "Leads Submitted": 8,
        "Cost Per Lead ($)": 1000.00,
        "Closed Sales (10%)": 1,
        "Total Revenue ($)": 25000,
        "ROAS": 3.13,
        "Status": "High Cost / Broad Leak"
    },
    {
        "Campaign Name": "Display",
        "Channel": "Display Network",
        "Ad Format": "Image / Banner Ad",
        "Spend ($)": 5000,
        "Impressions": 250000,
        "Clicks (Sessions)": 10000,
        "Avg CPC ($)": 0.50,
        "Bounce Rate (%)": 98.2,
        "Avg Engagement Time (s)": 6,
        "Leads Submitted": 10,
        "Cost Per Lead ($)": 500.00,
        "Closed Sales (10%)": 0,
        "Total Revenue ($)": 0,
        "ROAS": 0.00,
        "Status": "Disastrous Clickbait Waste"
    },
    {
        "Campaign Name": "YouTube - Cinematic Video Ad",
        "Channel": "Video (YouTube)",
        "Ad Format": "Skippable In-Stream Video",
        "Spend ($)": 4000,
        "Impressions": 80000,
        "Clicks (Sessions)": 200,
        "Avg CPC ($)": 20.00,
        "Bounce Rate (%)": 92.0,
        "Avg Engagement Time (s)": 12,
        "Leads Submitted": 2,
        "Cost Per Lead ($)": 2000.00,
        "Closed Sales (10%)": 0,
        "Total Revenue ($)": 0,
        "ROAS": 0.00,
        "Status": "98%+ Skip Rate / Weak Hook"
    },
    {
        "Campaign Name": "Performance Max (PMax)",
        "Channel": "Cross-Channel PMax",
        "Ad Format": "Automated Multi-Asset",
        "Spend ($)": 3000,
        "Impressions": 28000,
        "Clicks (Sessions)": 1000,
        "Avg CPC ($)": 3.00,
        "Bounce Rate (%)": 58.0,
        "Avg Engagement Time (s)": 64,
        "Leads Submitted": 15,
        "Cost Per Lead ($)": 200.00,
        "Closed Sales (10%)": 1,
        "Total Revenue ($)": 25000,
        "ROAS": 8.33,
        "Status": "Moderate (Geo Leak Outside Target States)"
    }
]

df_campaigns = pd.DataFrame(campaign_data)

# Calculate Overall Aggregates
total_spend = df_campaigns["Spend ($)"].sum()
total_clicks = df_campaigns["Clicks (Sessions)"].sum()
total_leads = df_campaigns["Leads Submitted"].sum()
total_sales = df_campaigns["Closed Sales (10%)"].sum()
total_revenue = df_campaigns["Total Revenue ($)"].sum()
blended_cpl = total_spend / total_leads if total_leads > 0 else 0
blended_roas = total_revenue / total_spend if total_spend > 0 else 0

# --- TAB NAVIGATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive Summary", 
    "🎯 Campaign & Channel Acquisition", 
    "📍 Location & Geo-Targeting Audit", 
    "🔍 Search Terms & Quality Audit", 
    "🛠️ Student Diagnostic & Optimization Challenge"
])

# --- TAB 1: EXECUTIVE SUMMARY ---
with tab1:
    st.header("1. 3-Month Performance Overview")
    st.write("Review the high-level GA4 metrics for SunPower Solutions over the past 90 days. Pay attention to how macro numbers can hide severe underlying inefficiencies.")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Ad Spend", f"${total_spend:,.2f}")
    col2.metric("GA4 Sessions (Clicks)", f"{total_clicks:,}")
    col3.metric("Consultation Leads", f"{total_leads}", help="Form submissions requesting a solar quote")
    col4.metric("Blended Cost Per Lead (CPL)", f"${blended_cpl:.2f}", delta="Target: $150-$250", delta_color="normal")
    col5.metric("Blended ROAS", f"{blended_roas:.2f}x", delta="Revenue: $300,000")

    st.markdown("---")
    st.subheader("💡 Financial Impact Breakdown")
    
    f1, f2, f3 = st.columns(3)
    f1.metric("Closed Installations (10% Close Rate)", f"{total_sales} Systems Sold")
    f2.metric("Gross Revenue ($25k AOV)", f"${total_revenue:,.2f}")
    f3.metric("Gross Profit (40% Margin - Ad Spend)", f"${(total_revenue * 0.40) - total_spend:,.2f}")

    st.subheader("📈 90-Day GA4 Traffic & Conversion Trend")
    days = np.arange(1, 91)
    np.random.seed(42)
    daily_traffic = np.random.normal(total_clicks / 90, 8, 90).astype(int)
    daily_leads = np.random.normal(total_leads / 90, 0.5, 90).clip(0, 5).astype(int)
    trend_df = pd.DataFrame({"Day": days, "GA4 Sessions": daily_traffic, "Lead Conversions": daily_leads})
    st.line_chart(trend_df.set_index("Day"))

# --- TAB 2: CAMPAIGN & CHANNEL ACQUISITION ---
with tab2:
    st.header("2. Campaign & Channel Breakdown")
    st.write("Dissect individual campaign performance to see which ad formats generated profitable revenue and which wasted budget.")
    
    st.dataframe(
        df_campaigns[[
            "Campaign Name", "Channel", "Spend ($)", "Clicks (Sessions)", 
            "Avg CPC ($)", "Bounce Rate (%)", "Leads Submitted", 
            "Cost Per Lead ($)", "Total Revenue ($)", "ROAS", "Status"
        ]],
        use_container_width=True,
        hide_index=True
    )
    
    st.subheader("📊 Spend vs. Revenue Contribution by Campaign")
    chart_data = df_campaigns.set_index("Campaign Name")[["Spend ($)", "Total Revenue ($)"]]
    st.bar_chart(chart_data)

# --- TAB 3: LOCATION & GEO-TARGETING AUDIT ---
with tab3:
    st.header("3. Geographic Location Audit")
    st.write("SunPower's approved expansion states are **California (CA), Arizona (AZ), Texas (TX), Florida (FL), and Nevada (NV)**. Check how location settings impacted campaign efficiency.")
    
    geo_data = [
        {"State / Region": "California (CA)", "Approved Market?": "YES", "Spend ($)": 11000, "Sessions": 2800, "Leads": 70, "CPL ($)": 157.14, "Closed Sales": 7},
        {"State / Region": "Arizona (AZ)", "Approved Market?": "YES", "Spend ($)": 5000, "Sessions": 1200, "Leads": 30, "CPL ($)": 166.67, "Closed Sales": 3},
        {"State / Region": "Texas (TX)", "Approved Market?": "YES", "Spend ($)": 4500, "Sessions": 1000, "Leads": 22, "CPL ($)": 204.55, "Closed Sales": 2},
        {"State / Region": "Florida (FL)", "Approved Market?": "YES", "Spend ($)": 3000, "Sessions": 750, "Leads": 10, "CPL ($)": 300.00, "Closed Sales": 0},
        {"State / Region": "Nevada (NV)", "Approved Market?": "YES", "Spend ($)": 2500, "Sessions": 600, "Leads": 3, "CPL ($)": 833.33, "Closed Sales": 0},
        {"State / Region": "Ohio, Pennsylvania, New York (Out of State Leak)", "Approved Market?": "NO", "Spend ($)": 4000, "Sessions": 9050, "Leads": 0, "CPL ($)": 0.00, "Closed Sales": 0}
    ]
    df_geo = pd.DataFrame(geo_data)
    st.table(df_geo)
    
    st.warning("⚠️ **Geo-Targeting Warning:** Notice that $4,000 (13.3% of total budget) leaked into non-target states like OH, PA, and NY because location settings were set to *'Presence or Interest'* instead of *'Presence only'*!")

# --- TAB 4: SEARCH TERMS & QUALITY AUDIT ---
with tab4:
    st.header("4. Search Query & Quality Score Audit")
    st.write("Review the exact search queries typed into Google that triggered SunPower's search ads, along with their Google Quality Score rating based on ad relevance.")
    
    query_data = [
        {"Search Query Typed by User": "solar panel installation cost san diego", "Matched Keyword": "solar panel cost", "Match Type": "Phrase", "Clicks": 850, "Spend ($)": 3400, "Leads": 42, "CPL ($)": 80.95, "Quality Score": "10/10 (High)"},
        {"Search Query Typed by User": "best residential solar warranty california", "Matched Keyword": "solar warranty", "Match Type": "Exact", "Clicks": 620, "Spend ($)": 2480, "Leads": 31, "CPL ($)": 80.00, "Quality Score": "9/10 (High)"},
        {"Search Query Typed by User": "solar panel subsidies government rebate", "Matched Keyword": "solar energy", "Match Type": "Broad", "Clicks": 2100, "Spend ($)": 6300, "Leads": 2, "CPL ($)": 3150.00, "Quality Score": "3/10 (Low)"},
        {"Search Query Typed by User": "solar panel installer career opportunities", "Matched Keyword": "solar energy", "Match Type": "Broad", "Clicks": 950, "Spend ($)": 2850, "Leads": 0, "CPL ($)": 0.00, "Quality Score": "2/10 (Low)"},
        {"Search Query Typed by User": "how to assemble home solar kit", "Matched Keyword": "solar energy", "Match Type": "Broad", "Clicks": 1200, "Spend ($)": 3600, "Leads": 0, "CPL ($)": 0.00, "Quality Score": "2/10 (Low)"}
    ]
    st.table(pd.DataFrame(query_data))

# --- TAB 5: STUDENT DIAGNOSTIC & OPTIMIZATION CHALLENGE ---
with tab5:
    st.header("5. Student Optimization Challenge")
    st.write("Analyze the 3-month GA4 data above, diagnose the major bottlenecks, optimize keywords and negative keyword lists, and reallocate monthly budget for Month 4.")
    
    st.subheader("📋 Step 1: Diagnose Campaign Waste")
    q1 = st.multiselect(
        "Which campaign tactics resulted in major budget waste? (Select all that apply):",
        [
            "Display Ads",
            "RSA - Broad Match",
            "RSA - Exact/Phrase Match",
            "YouTube TV Style Ad",
            'Geo-targeting Set to "Presence or Interest"'
        ],
        default=[]
    )

    st.subheader("🔍 Step 2: Keyword Optimization & Negative Keyword Shield")
    st.caption("Adding negative terms blocks wasteful searches.")
    
    neg_selected = st.multiselect(
        "Select Negative Keywords to Add:",
        [
            "diy", 
            "san diego", 
            "houston", 
            "jobs", 
            "installation", 
            "careers", 
            "home kit", 
            "warranty"
        ],
        default=[]
    )
    
    st.subheader("💰 Step 3: Propose Month 4 Budget Re-Allocation ($10,000/mo)")
    st.caption("Shift funds as needed based on campaign performance.")
    
    c_b1, c_b2, c_b3, c_b4, c_b5 = st.columns(5)
    b_rsa = c_b1.number_input("High-Intent RSA Search ($):", value=0, step=500)
    b_lsa = c_b2.number_input("Local Service Ads (LSA) ($):", value=0, step=500)
    b_pmax = c_b3.number_input("Performance Max (Presence Only) ($):", value=0, step=500)
    b_yt = c_b4.number_input("YouTube (Video 6 Hook) ($):", value=0, step=500)
    b_disp = c_b5.number_input("Display Banner Ads ($):", value=0, step=500)
    
    total_reallocated = b_rsa + b_lsa + b_pmax + b_yt + b_disp
    
    if total_reallocated == 10000:
        st.success(f"✅ Budget Balanced: ${total_reallocated:,.2f} / $10,000.00")
    else:
        st.warning(f"⚠️ Total budget reallocation must equal $10,000 (Currently ${total_reallocated:,.2f})")

    st.subheader("📝 Step 4: Executive Rationale & Strategy Note")
    student_notes = st.text_area(
        "Explain your diagnostic findings, negative keyword additions, and budget shift rationale for SunPower's CMO:",
        placeholder="e.g., We recommend completely eliminating Display ad spend and shifting funds into Local Service Ads (LSAs) and High-Intent RSA search to capture direct phone and consultation leads..."
    )
    
    if st.button("Submit GA4 Campaign Audit & Recommendations"):
        correct_diag = (
            "Display Ads" in q1 and
            "RSA - Broad Match" in q1 and
            "YouTube TV Style Ad" in q1 and
            'Geo-targeting Set to "Presence or Interest"' in q1 and
            "RSA - Exact/Phrase Match" not in q1
        )
        
        target_negatives = {"diy", "jobs", "careers", "home kit"}
        user_negatives = set(neg_selected)
        has_correct_negatives = (target_negatives == user_negatives)
        
        if correct_diag and has_correct_negatives and total_reallocated == 10000 and len(student_notes.strip()) > 30:
            st.balloons()
            st.success("🎉 EXCELLENT GA4 AUDIT! You correctly identified all campaign bottlenecks, established an active Negative Keyword Shield, and optimized budget allocation!")
            
            # Projection calculation incorporating LSA efficiency (~$125 CPL)
            proj_leads = int((b_rsa / 100) + (b_lsa / 125) + (b_pmax / 200) + (b_yt / 250))
            proj_sales = int(proj_leads * 0.10)
            proj_rev = proj_sales * 25000
            proj_roas = proj_rev / 10000
            
            st.markdown(f"""
            ### 🏆 Month 4 Projected Impact of Your Optimization:
            - **Projected Monthly Leads:** **{proj_leads} Qualified Leads** (vs 45/mo previously)
            - **Projected Monthly Sales:** **{proj_sales} Closed Installations** (vs 4/mo previously)
            - **Projected Monthly Revenue:** **${proj_rev:,.2f}**
            - **Projected Monthly ROAS:** **{proj_roas:.2f}x** (Up from 10.0x blended!)
            """)
        else:
            st.error("🚨 Audit Incomplete or Sub-optimal! Ensure you selected the 4 major waste tactics (without selecting RSA - Exact/Phrase Match), chose the exact negative keywords ('diy', 'jobs', 'careers', 'home kit'), balanced your budget to exactly $10,000, and provided detailed executive notes.")

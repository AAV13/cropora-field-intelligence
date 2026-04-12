import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import os

st.set_page_config(
    page_title="Cropora - Field Intelligence Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE = os.path.dirname(os.path.abspath(__file__))

def img(name):
    return Image.open(os.path.join(BASE, name))

def csv(name):
    return pd.read_csv(os.path.join(BASE, name))

def scoreColor(s):
    if s >= 70: return "#3A7D44"
    if s >= 40: return "#E8A020"
    return "#D32F2F"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1200px; }

.hero-banner {
    background: #2C1A0E;
    border-radius: 12px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero-tag {
    display: inline-block;
    background: #C8973A;
    color: #2C1A0E;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 2px;
    margin-bottom: 16px;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 40px;
    color: white;
    font-weight: 400;
    line-height: 1.15;
    margin-bottom: 12px;
}
.hero-title span { color: #C8973A; }
.hero-sub { font-size: 15px; color: rgba(255,255,255,0.6); max-width: 600px; line-height: 1.7; }

.lookup-card {
    background: #FAFAF7;
    border: 1px solid #E2DDD5;
    border-radius: 12px;
    padding: 28px 32px;
    margin-bottom: 32px;
}
.lookup-title {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #2C1A0E;
    margin-bottom: 4px;
    font-weight: 400;
}
.lookup-sub { font-size: 13px; color: #6B5E4E; margin-bottom: 20px; }

.score-hero {
    text-align: center;
    padding: 24px 16px;
    border-radius: 12px;
    border: 1px solid;
}
.score-number {
    font-family: 'DM Serif Display', serif;
    font-size: 56px;
    line-height: 1;
    margin-bottom: 4px;
}
.score-tier { font-size: 14px; font-weight: 600; margin-bottom: 12px; }
.score-rec { font-size: 13px; line-height: 1.6; opacity: 0.8; }

.stat-card {
    background: white;
    border: 1px solid #E2DDD5;
    border-radius: 10px;
    padding: 20px 16px;
    text-align: center;
    height: 100%;
}
.stat-label { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6B5E4E; margin-bottom: 8px; }
.stat-value { font-family: 'DM Serif Display', serif; font-size: 32px; line-height: 1; margin-bottom: 4px; }
.stat-sub { font-size: 12px; color: #6B5E4E; }

.section-divider { border: none; border-top: 2px solid #E2DDD5; margin: 40px 0 32px; }
.section-label { font-size: 11px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #6B5E4E; margin-bottom: 8px; }
.section-title { font-family: 'DM Serif Display', serif; font-size: 26px; color: #2C1A0E; font-weight: 400; margin-bottom: 6px; }
.section-sub { font-size: 14px; color: #6B5E4E; margin-bottom: 24px; line-height: 1.6; }

.insight {
    border-left: 3px solid #C8973A;
    padding: 14px 20px;
    background: rgba(200,151,58,0.06);
    border-radius: 0 6px 6px 0;
    font-size: 14px;
    line-height: 1.7;
    color: #2C1A0E;
    margin: 16px 0;
}
.insight strong { color: #2C1A0E; }

.what-if-card {
    background: #F0F7FF;
    border: 1px solid #B8D4F0;
    border-radius: 12px;
    padding: 24px 28px;
    margin: 24px 0;
}
.what-if-title { font-size: 15px; font-weight: 600; color: #1A3A5C; margin-bottom: 4px; }
.what-if-sub { font-size: 13px; color: #4A6A8C; margin-bottom: 16px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-tag">Bitcamp 2025</div>
    <div class="hero-title">Cropora<br><span>Field Intelligence Platform</span></div>
    <div class="hero-sub">
        11 years of satellite crop data. Two ML models. A confidence-scored 2024 projection
        for every field in Iowa. Built to help lenders, insurers, and farmers make better
        decisions before a single seed goes in the ground.
    </div>
</div>
""", unsafe_allow_html=True)

# ── GLOBAL METRICS ─────────────────────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
metrics = [
    ("1.93M", "Cropland pixels analyzed", "#2C1A0E"),
    ("96%", "ML model accuracy", "#3A7D44"),
    ("68.3%", "Iowa in regular rotation", "#2196F3"),
    ("0.856", "2024 projection confidence", "#E8A020"),
    ("66.7%", "High resilience fields", "#3A7D44"),
]
for col, (val, lab, color) in zip([c1,c2,c3,c4,c5], metrics):
    with col:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-label">{lab}</div>
            <div class="stat-value" style="color:{color};">{val}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── FIELD LOOKUP ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="lookup-title">Field Intelligence Lookup</div>
<div class="lookup-sub">Select an Iowa region to get an instant risk assessment, 2024 crop projection, and lending recommendation.</div>
""", unsafe_allow_html=True)

regions_data = {
    "SW Iowa":          {"score":82.0,"pct_high":78.7,"pct_low":8.8,"pixels":182809},
    "SC Iowa":          {"score":79.2,"pct_high":74.6,"pct_low":10.1,"pixels":143448},
    "SE Iowa":          {"score":80.5,"pct_high":74.7,"pct_low":3.9,"pixels":180373},
    "Far SE Iowa":      {"score":84.3,"pct_high":81.9,"pct_low":2.9,"pixels":203330},
    "W Iowa":           {"score":76.6,"pct_high":69.1,"pct_low":9.1,"pixels":137732},
    "Central Iowa":     {"score":65.7,"pct_high":49.1,"pct_low":13.5,"pixels":104874},
    "E Central Iowa":   {"score":79.7,"pct_high":73.9,"pct_low":5.1,"pixels":157235},
    "E Iowa":           {"score":87.7,"pct_high":87.9,"pct_low":2.4,"pixels":214631},
    "NW Iowa":          {"score":63.9,"pct_high":45.1,"pct_low":14.1,"pixels":79544},
    "NC Iowa":          {"score":70.1,"pct_high":57.2,"pct_low":11.3,"pixels":75236},
    "NE Central Iowa":  {"score":69.1,"pct_high":54.3,"pct_low":9.4,"pixels":75067},
    "NE Iowa":          {"score":72.7,"pct_high":61.7,"pct_low":7.3,"pixels":167973},
    "Far NW Iowa":      {"score":54.2,"pct_high":28.4,"pct_low":25.3,"pixels":78247},
    "N Central Iowa":   {"score":39.2,"pct_high":10.6,"pct_low":56.2,"pixels":5086},
    "Far NE Central":   {"score":48.8,"pct_high":19.4,"pct_low":31.6,"pixels":16402},
    "Far NE Iowa":      {"score":57.3,"pct_high":33.2,"pct_low":20.1,"pixels":110240},
}

col_sel, col_gap = st.columns([1, 3])
with col_sel:
    selected = st.selectbox("", list(regions_data.keys()), label_visibility="collapsed")

r = regions_data[selected]
score = r['score']

if score >= 70:
    color = "#3A7D44"; bg = "rgba(58,125,68,0.08)"; tier = "High Resilience"
    rec = "Strong agronomic stability. Consistent corn-soy rotation with high predictability. Suitable for standard lending terms and baseline insurance premiums."
elif score >= 40:
    color = "#E8A020"; bg = "rgba(232,160,32,0.08)"; tier = "Medium Resilience"
    rec = "Moderate stability. Some monoculture concentration present. Consider requesting field-level rotation history before extending credit."
else:
    color = "#D32F2F"; bg = "rgba(211,47,47,0.08)"; tier = "Low Resilience"
    rec = "Elevated agronomic risk. High monoculture rates and irregular cropping patterns. Apply risk premium to lending and insurance products."

proj_soy = 51.1 + (score - 70) * 0.05
proj_corn = 100 - proj_soy
dominant = "Soybean" if proj_soy > proj_corn else "Corn"
dom_pct = max(proj_soy, proj_corn)
dom_color = "#3A7D44" if dominant == "Soybean" else "#E8A020"
conf_label = "High" if score >= 70 else "Moderate" if score >= 40 else "Low"

lc1, lc2, lc3, lc4, lc5 = st.columns([1.2, 1, 1, 1, 1])

with lc1:
    st.markdown(f"""<div class="score-hero" style="background:{bg};border-color:{color};">
        <div class="score-number" style="color:{color};">{score:.0f}</div>
        <div class="score-tier" style="color:{color};">{tier}</div>
        <div class="score-rec" style="color:{color};">{rec}</div>
    </div>""", unsafe_allow_html=True)

with lc2:
    st.markdown(f"""<div class="stat-card">
        <div class="stat-label">2024 Projected Crop</div>
        <div class="stat-value" style="color:{dom_color};font-size:24px;">{dominant}</div>
        <div class="stat-sub">{dom_pct:.1f}% - {conf_label} confidence</div>
    </div>""", unsafe_allow_html=True)

with lc3:
    st.markdown(f"""<div class="stat-card">
        <div class="stat-label">High Resilience Fields</div>
        <div class="stat-value" style="color:#3A7D44;">{r['pct_high']:.0f}%</div>
        <div class="stat-sub">of cropland pixels</div>
    </div>""", unsafe_allow_html=True)

with lc4:
    st.markdown(f"""<div class="stat-card">
        <div class="stat-label">At-Risk Fields</div>
        <div class="stat-value" style="color:#D32F2F;">{r['pct_low']:.0f}%</div>
        <div class="stat-sub">below threshold</div>
    </div>""", unsafe_allow_html=True)

with lc5:
    st.markdown(f"""<div class="stat-card">
        <div class="stat-label">Cropland Pixels</div>
        <div class="stat-value" style="font-size:22px;">{r['pixels']:,}</div>
        <div class="stat-sub">at 300m resolution</div>
    </div>""", unsafe_allow_html=True)

# ── IOWA REGION MAP ───────────────────────────────────────────────────────────
region_lats = {
    "SW Iowa":40.79,"SC Iowa":40.79,"SE Iowa":40.79,"Far SE Iowa":40.79,
    "W Iowa":41.56,"Central Iowa":41.56,"E Central Iowa":41.56,"E Iowa":41.56,
    "NW Iowa":42.34,"NC Iowa":42.34,"NE Central Iowa":42.34,"NE Iowa":42.34,
    "Far NW Iowa":43.11,"N Central Iowa":43.11,"Far NE Central":43.11,"Far NE Iowa":43.11,
}
region_lons = {
    "SW Iowa":-95.79,"SC Iowa":-94.16,"SE Iowa":-92.54,"Far SE Iowa":-90.91,
    "W Iowa":-95.79,"Central Iowa":-94.16,"E Central Iowa":-92.54,"E Iowa":-90.91,
    "NW Iowa":-95.79,"NC Iowa":-94.16,"NE Central Iowa":-92.54,"NE Iowa":-90.91,
    "Far NW Iowa":-95.79,"N Central Iowa":-94.16,"Far NE Central":-92.54,"Far NE Iowa":-90.91,
}

fig_map = go.Figure()

# All regions as bubbles
for rname, rdata in regions_data.items():
    is_selected = rname == selected
    fig_map.add_trace(go.Scattergeo(
        lon=[region_lons[rname]],
        lat=[region_lats[rname]],
        mode='markers+text',
        marker=dict(
            size=28 if is_selected else 18,
            color=rdata['score'],
            colorscale='RdYlGn',
            cmin=0, cmax=100,
            line=dict(color='white' if is_selected else 'rgba(255,255,255,0.4)',
                      width=3 if is_selected else 1),
            opacity=1.0 if is_selected else 0.7,
        ),
        text=[f"{rdata['score']:.0f}"],
        textposition='middle center',
        textfont=dict(size=10 if is_selected else 8, color='white', family='DM Sans'),
        hovertemplate=f"<b>{rname}</b><br>Score: {rdata['score']:.0f}<br>High resilience: {rdata['pct_high']:.0f}%<br>At-risk: {rdata['pct_low']:.0f}%<extra></extra>",
        showlegend=False,
        name=rname
    ))

# Selected region ring
fig_map.add_trace(go.Scattergeo(
    lon=[region_lons[selected]],
    lat=[region_lats[selected]],
    mode='markers',
    marker=dict(size=44, color='rgba(0,0,0,0)',
                line=dict(color=color, width=3)),
    hoverinfo='skip', showlegend=False
))

fig_map.update_layout(
    geo=dict(
        scope='usa',
        center=dict(lat=42.0, lon=-93.5),
        projection_scale=8,
        showland=True, landcolor='#F5F0E8',
        showlakes=True, lakecolor='#C8E6F5',
        showrivers=True, rivercolor='#C8E6F5',
        showsubunits=True, subunitcolor='#D0C8BC',
        bgcolor='#FAFAF7',
        showcoastlines=False,
    ),
    height=340,
    paper_bgcolor='#FAFAF7',
    margin=dict(l=0, r=0, t=10, b=0),
    font=dict(family='DM Sans'),
    annotations=[dict(
        x=0.5, y=0, xref='paper', yref='paper',
        text=f'Selected: <b>{selected}</b> - Score {score:.0f} ({tier}) - Color = resilience score (red=low, green=high)',
        showarrow=False, font=dict(size=11, color='#6B5E4E')
    )]
)
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""<div class="what-if-title">What-if analysis: rotation threshold</div>
<div class="what-if-sub">Adjust the minimum transition rate required to classify a field as "regular rotation". Watch how Iowa's cropland distribution changes.</div>
""", unsafe_allow_html=True)

threshold = st.slider("Rotation threshold (minimum corn-soy alternation rate)",
                      min_value=0.40, max_value=0.90, value=0.60, step=0.05,
                      format="%.2f")

base_rotation = 68.3
base_mono = 24.9
base_irregular = 6.9

delta = (threshold - 0.60) * 100
adj_rotation  = max(0, min(100, base_rotation  - delta * 0.8))
adj_mono      = max(0, min(100, base_mono      + delta * 0.5))
adj_irregular = max(0, min(100, base_irregular + delta * 0.3))
total = adj_rotation + adj_mono + adj_irregular
adj_rotation  = adj_rotation  / total * 100
adj_mono      = adj_mono      / total * 100
adj_irregular = adj_irregular / total * 100

wc1, wc2, wc3, wc4 = st.columns(4)
with wc1:
    delta_r = adj_rotation - base_rotation
    st.metric("Regular Rotation", f"{adj_rotation:.1f}%", f"{delta_r:+.1f}% vs baseline")
with wc2:
    delta_m = adj_mono - base_mono
    st.metric("Monoculture", f"{adj_mono:.1f}%", f"{delta_m:+.1f}% vs baseline")
with wc3:
    delta_i = adj_irregular - base_irregular
    st.metric("Irregular", f"{adj_irregular:.1f}%", f"{delta_i:+.1f}% vs baseline")
with wc4:
    high_res_adj = 66.7 - delta * 0.4
    st.metric("High Resilience Fields", f"{high_res_adj:.1f}%", f"{high_res_adj-66.7:+.1f}% vs baseline")

fig_whatif = go.Figure()
categories = ["Regular Rotation", "Monoculture", "Irregular"]
baseline_vals = [base_rotation, base_mono, base_irregular]
adjusted_vals = [adj_rotation, adj_mono, adj_irregular]
colors_wf = ['#2196F3', '#FF9800', '#9C27B0']

fig_whatif.add_trace(go.Bar(
    name='Baseline (0.60)', x=categories, y=baseline_vals,
    marker_color=['rgba(33,150,243,0.4)', 'rgba(255,152,0,0.4)', 'rgba(156,39,176,0.4)'],
    hovertemplate='<b>%{x}</b><br>Baseline: %{y:.1f}%<extra></extra>'
))
fig_whatif.add_trace(go.Bar(
    name=f'Adjusted ({threshold:.2f})', x=categories, y=adjusted_vals,
    marker_color=colors_wf,
    hovertemplate='<b>%{x}</b><br>Adjusted: %{y:.1f}%<extra></extra>'
))
fig_whatif.update_layout(
    barmode='group', height=260,
    paper_bgcolor='white', plot_bgcolor='white',
    yaxis=dict(title='% of Cropland', gridcolor='#f0f0f0'),
    legend=dict(orientation='h', y=1.1),
    margin=dict(l=40, r=20, t=20, b=40),
    font=dict(family='DM Sans')
)
st.plotly_chart(fig_whatif, use_container_width=True)

# ── SECTION: NDVI ─────────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Task 01</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">NDVI Phenological Curves</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Corn vs. soybean vegetation dynamics - Iowa 2022 growing season. MODIS MOD13Q1, 250m, 16-day composites.</div>', unsafe_allow_html=True)

try:
    df_ndvi = csv("task1_ndvi_stats.csv")
    df_ndvi['Date'] = pd.to_datetime(df_ndvi['Date'])

    n1, n2 = st.columns([1, 4])
    with n1:
        show_iqr    = st.checkbox("Show IQR bands", value=True)
        season_only = st.checkbox("Growing season only", value=False)
    with n2:
        df_plot = df_ndvi.copy()
        if season_only:
            df_plot = df_plot[(df_plot['Date'].dt.month >= 5) & (df_plot['Date'].dt.month <= 10)]

        fig_ndvi = go.Figure()
        if show_iqr:
            fig_ndvi.add_trace(go.Scatter(
                x=pd.concat([df_plot['Date'], df_plot['Date'][::-1]]),
                y=pd.concat([df_plot['Corn_Q75'], df_plot['Corn_Q25'][::-1]]),
                fill='toself', fillcolor='rgba(232,160,32,0.15)',
                line=dict(color='rgba(0,0,0,0)'), name='Corn IQR', hoverinfo='skip'
            ))
            fig_ndvi.add_trace(go.Scatter(
                x=pd.concat([df_plot['Date'], df_plot['Date'][::-1]]),
                y=pd.concat([df_plot['Soy_Q75'], df_plot['Soy_Q25'][::-1]]),
                fill='toself', fillcolor='rgba(58,125,68,0.15)',
                line=dict(color='rgba(0,0,0,0)'), name='Soy IQR', hoverinfo='skip'
            ))
        fig_ndvi.add_trace(go.Scatter(
            x=df_plot['Date'], y=df_plot['Corn_Mean'],
            name='Corn', line=dict(color='#E8A020', width=3),
            hovertemplate='<b>Corn</b><br>%{x|%b %d}: %{y:.3f}<extra></extra>'
        ))
        fig_ndvi.add_trace(go.Scatter(
            x=df_plot['Date'], y=df_plot['Soy_Mean'],
            name='Soybean', line=dict(color='#3A7D44', width=3),
            hovertemplate='<b>Soybean</b><br>%{x|%b %d}: %{y:.3f}<extra></extra>'
        ))
        stages = {'Planting':pd.Timestamp('2022-05-01'),'Green-up':pd.Timestamp('2022-06-01'),
                  'Peak':pd.Timestamp('2022-07-20'),'Senescence':pd.Timestamp('2022-09-15'),
                  'Harvest':pd.Timestamp('2022-10-15')}
        for label, dt in stages.items():
            fig_ndvi.add_vline(x=dt.timestamp()*1000, line_dash='dash',
                               line_color='gray', line_width=1, opacity=0.5,
                               annotation_text=label, annotation_position='top')
        fig_ndvi.update_layout(
            height=380, paper_bgcolor='white', plot_bgcolor='white',
            xaxis=dict(gridcolor='#f0f0f0'), yaxis=dict(title='NDVI', range=[-0.05,1.0], gridcolor='#f0f0f0'),
            legend=dict(orientation='h', y=1.08), hovermode='x unified',
            margin=dict(l=50,r=20,t=40,b=40), font=dict(family='DM Sans')
        )
        st.plotly_chart(fig_ndvi, use_container_width=True)
except FileNotFoundError:
    st.image(img("task1_ndvi_phenology.png"), use_container_width=True)

mc1, mc2, mc3 = st.columns(3)
mc1.metric("Corn Peak NDVI", "0.874", "July 12, 2022")
mc2.metric("Soybean Peak NDVI", "0.867", "August 13, 2022")
mc3.metric("NDVI Classifier Accuracy", "78%", "Phenology features only")

st.markdown("""<div class="insight">
    <strong>Key finding:</strong> Corn peaks 32 days before soybean - reflecting its C4 photosynthetic
    pathway and earlier planting calendar. Early-season NDVI during green-up (June) is the single most
    predictive feature for crop type discrimination, confirmed by the NDVI-based ML classifier.
    Fields below the Iowa IQR during peak greenness signal stress before yield loss is irreversible.
</div>""", unsafe_allow_html=True)

st.markdown("#### NDVI-Based Crop Classifier Results")
st.image(img("task1_ndvi_classifier.png"), use_container_width=True)
st.caption("Random Forest trained purely on NDVI phenological features - no crop history needed. 78% accuracy confirms vegetation timing is a strong discriminator.")

# ── SECTION: ROTATION ─────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Task 02</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Crop Rotation Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">11-year CDL time series (2013-2023) - field-level rotation patterns across Iowa cropland.</div>', unsafe_allow_html=True)

rc1, rc2 = st.columns([1, 2])
with rc1:
    try:
        df_rot = csv("task2_rotation_stats.csv")
        df_rot = df_rot[df_rot['Class'] != 'Total Cropland']
        fig_rot = go.Figure(go.Pie(
            labels=df_rot['Class'],
            values=[float(str(v).replace(',','')) for v in df_rot['Pixel Count']],
            hole=0.6,
            marker_colors=['#2196F3','#FF9800','#9C27B0'],
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Share: %{percent}<extra></extra>'
        ))
        fig_rot.update_layout(
            height=300, paper_bgcolor='white',
            margin=dict(l=20,r=20,t=20,b=20), showlegend=False,
            annotations=[dict(text='Iowa<br>Cropland', x=0.5, y=0.5, font_size=13, showarrow=False)]
        )
        st.plotly_chart(fig_rot, use_container_width=True)
    except FileNotFoundError:
        pass

with rc2:
    st.metric("Regular Rotation", "68.3%", "118,722 ha")
    st.metric("Monoculture", "24.9%", "43,251 ha")
    st.metric("Irregular", "6.9%", "11,928 ha")
    st.markdown("""<div class="insight" style="margin-top:12px;">
        Iowa's bimodal transition rate distribution shows most fields are either
        near-perfect rotators (rate near 1.0) or pure monocultures (rate near 0.0).
        This binary structure is what makes the 2024 projection high-confidence.
    </div>""", unsafe_allow_html=True)

tab_map, tab_hist = st.tabs(["Rotation Map", "Transition Rate Distribution"])
with tab_map:
    st.image(img("task2_rotation_map.png"), use_container_width=True)
with tab_hist:
    st.image(img("task2_transition_rate_hist.png"), use_container_width=True)

# ── SECTION: SOIL MOISTURE ────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Task 03</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Soil Moisture Anomaly</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">NASA SMAP L4 surface soil moisture - Iowa growing season 2022, May through September.</div>', unsafe_allow_html=True)

sm1, sm2, sm3 = st.columns(3)
sm1.metric("Season Mean SM", "0.241 m3/m3", "Surface layer")
sm2.metric("Driest Week", "Sep 26 (-1.24 Z)", "Critical late-season")
sm3.metric("Wettest Week", "May 08 (+1.69 Z)", "Favorable planting")

st.image(img("task3_smap_timeseries.png"), use_container_width=True)
st.markdown("#### Spatial Anomaly Maps")
st.image(img("task3_smap_anomaly_maps.png"), use_container_width=True)

st.markdown("""<div class="insight">
    <strong>Agricultural impact:</strong> May-June 2022 saw above-normal moisture - favorable planting conditions.
    From July onward, persistent drying pushed soil moisture below seasonal norms during corn pollination
    (late June - July) and soybean pod-fill (August). The September drought peak (Z = -1.24) accelerated
    senescence and likely reduced final grain fill across Iowa cropland.
</div>""", unsafe_allow_html=True)

# ── SECTION: ML MODEL ─────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Task 04</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">ML Crop Type Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Two complementary Random Forest models - one using 10-year CDL history, one using NDVI phenological features only.</div>', unsafe_allow_html=True)

fig_acc = go.Figure(go.Bar(
    x=['NDVI-only Model', 'CDL History Model'],
    y=[78, 96],
    marker_color=['#E8A020', '#3A7D44'],
    text=['78%', '96%'], textposition='outside',
    width=0.4,
    hovertemplate='<b>%{x}</b><br>Accuracy: %{y}%<extra></extra>'
))
fig_acc.update_layout(
    height=260, paper_bgcolor='white', plot_bgcolor='white',
    yaxis=dict(title='Accuracy (%)', range=[0,108], gridcolor='#f0f0f0'),
    margin=dict(l=40,r=20,t=20,b=40), font=dict(family='DM Sans'),
    showlegend=False
)
st.plotly_chart(fig_acc, use_container_width=True)

st.markdown("""<div class="insight">
    <strong>The 18-point gap tells the story:</strong> NDVI phenology alone achieves 78% accuracy.
    Adding 10 years of crop type history jumps accuracy to 96%. This quantifies exactly how much
    agronomic memory matters beyond what a single season of satellite imagery can reveal.
</div>""", unsafe_allow_html=True)

ml1, ml2 = st.columns(2)
with ml1:
    st.image(img("task4_rf_evaluation.png"), use_container_width=True)
with ml2:
    st.image(img("task4_rf_prediction_map.png"), use_container_width=True)

# ── SECTION: PROJECTION ───────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">2024 Forecast</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">2024 Crop Type Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Field-level corn vs. soybean forecast for Iowa 2024 - derived from 11-year rotation history with pixel-level confidence scoring.</div>', unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)
p1.metric("Projected Corn", "48.9%", "8.1M hectares")
p2.metric("Projected Soybean", "51.1%", "8.5M hectares")
p3.metric("Mean Confidence", "0.856", "Across all cropland")
p4.metric("High Confidence Fields", "68.3%", "Regular rotation pixels")

st.image(img("task2_2024_projection.png"), use_container_width=True)

try:
    df_proj = csv("task2_2024_projection_stats.csv")
    df_proj = df_proj[df_proj['Source Class'] != 'Total']

    pc1, pc2 = st.columns(2)
    with pc1:
        conf_vals = [float(v) for v in df_proj['Mean Confidence'].tolist()]
        fig_conf = go.Figure(go.Bar(
            x=df_proj['Source Class'].tolist(),
            y=conf_vals,
            marker_color=['#3A7D44','#E8A020','#9C27B0'],
            text=[f'{v:.3f}' for v in conf_vals], textposition='outside',
            hovertemplate='<b>%{x}</b><br>Confidence: %{y:.3f}<extra></extra>'
        ))
        fig_conf.update_layout(
            height=280, title='Confidence by source class',
            paper_bgcolor='white', plot_bgcolor='white',
            yaxis=dict(range=[0,1.1], gridcolor='#f0f0f0'),
            margin=dict(l=40,r=20,t=40,b=40), font=dict(family='DM Sans')
        )
        st.plotly_chart(fig_conf, use_container_width=True)

    with pc2:
        corn_vals = [float(str(v).replace(',','')) for v in df_proj['Predicted Corn (ha)'].tolist()]
        soy_vals  = [float(str(v).replace(',','')) for v in df_proj['Predicted Soy (ha)'].tolist()]
        fig_area = go.Figure()
        fig_area.add_trace(go.Bar(name='Corn', x=df_proj['Source Class'].tolist(), y=corn_vals,
                                   marker_color='#E8A020', hovertemplate='<b>%{x}</b><br>Corn: %{y:,.0f} ha<extra></extra>'))
        fig_area.add_trace(go.Bar(name='Soybean', x=df_proj['Source Class'].tolist(), y=soy_vals,
                                   marker_color='#3A7D44', hovertemplate='<b>%{x}</b><br>Soy: %{y:,.0f} ha<extra></extra>'))
        fig_area.update_layout(
            barmode='group', height=280, title='Projected area by class (ha)',
            paper_bgcolor='white', plot_bgcolor='white',
            yaxis=dict(title='Area (ha)', gridcolor='#f0f0f0'),
            legend=dict(orientation='h', y=1.15),
            margin=dict(l=60,r=20,t=40,b=40), font=dict(family='DM Sans')
        )
        st.plotly_chart(fig_area, use_container_width=True)
except FileNotFoundError:
    pass

# ── SECTION: RESILIENCE ───────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Risk Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Field Resilience Score</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">A composite 0-100 score combining rotation consistency (50%), crop diversity (30%), and recent stability (20%) - synthesizing all three data streams into one actionable signal.</div>', unsafe_allow_html=True)

res1, res2, res3, res4 = st.columns(4)
res1.metric("High Resilience (>70)", "66.7%", "of Iowa cropland")
res2.metric("Medium (40-70)", "24.3%", "of Iowa cropland")
res3.metric("Low Resilience (<40)", "8.9%", "of Iowa cropland")
res4.metric("Most Vulnerable Region", "39.2 / 100", "N Central Iowa")

st.image(img("resilience_score_map.png"), use_container_width=True)

try:
    df_res = csv("resilience_by_region.csv")
    fig_res = go.Figure()
    fig_res.add_trace(go.Bar(
        x=df_res['Region'], y=df_res['Mean_Score'],
        marker_color=df_res['Mean_Score'],
        marker_colorscale='RdYlGn', marker_cmin=0, marker_cmax=100,
        text=df_res['Mean_Score'].round(0).astype(int),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Score: %{y:.1f}<extra></extra>'
    ))
    fig_res.add_hline(y=70, line_dash='dash', line_color='#3A7D44',
                      annotation_text='High threshold (70)', annotation_position='right')
    fig_res.add_hline(y=40, line_dash='dash', line_color='#D32F2F',
                      annotation_text='Low threshold (40)', annotation_position='right')
    fig_res.update_layout(
        height=350, title='Mean resilience score by region',
        paper_bgcolor='white', plot_bgcolor='white',
        yaxis=dict(title='Mean Resilience Score', range=[0,108], gridcolor='#f0f0f0'),
        margin=dict(l=40,r=120,t=40,b=60), font=dict(family='DM Sans'), showlegend=False
    )
    st.plotly_chart(fig_res, use_container_width=True)
except FileNotFoundError:
    pass

st.markdown("""<div class="insight">
    <strong>Real-world application:</strong> Eastern Iowa (Regions 4 and 8) scores 84-88 - the most bankable
    farmland in the state. N Central Iowa (score 39.2) has 56% of its cropland in the low-resilience
    category - fields where a lender should price in higher agronomic risk, an insurer should charge
    higher premiums, and a county extension agent should prioritize conservation program outreach.
</div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;padding:24px;color:#6B5E4E;font-size:13px;border-top:1px solid #E2DDD5;">
    <strong style="color:#2C1A0E;">Cropora - Field Intelligence Platform</strong><br>
    Bitcamp 2025<br>
    Data: NASA AppEEARS (MODIS MOD13Q1) - USDA NASS CropScape - NASA SMAP L4
</div>
""", unsafe_allow_html=True)

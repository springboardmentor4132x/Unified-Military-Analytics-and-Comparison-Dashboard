"""
Streamlit Dashboard: Quick Stats & Nation Overview
Module 5: Dashboard Development
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Military Analytics Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .metric-card { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load KPI data"""
    try:
        df = pd.read_csv('../../Milestone_2_KPI_Engineering/Module_3_KPI_Engineering/data/processed/military_final_wide.csv')
        return df
    except:
        return pd.DataFrame()

def main():
    st.title("🌍 Unified Military Analytics Dashboard")
    st.markdown("Comprehensive analysis of military capabilities across 140+ countries")
    
    # Load data
    df = load_data()
    
    if df.empty:
        st.warning("⚠️ Data not loaded. Please ensure data files are in correct location.")
        st.stop()
    
    # Sidebar filters
    st.sidebar.title("🔍 Filters")
    
    selected_region = st.sidebar.multiselect(
        "Region",
        options=df['region'].unique() if 'region' in df.columns else [],
        default=df['region'].unique() if 'region' in df.columns else None
    )
    
    # Filter data
    if selected_region:
        filtered_df = df[df['region'].isin(selected_region)]
    else:
        filtered_df = df
    
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "🌐 Nation Profile", "📈 Comparisons"])
    
    with tab1:
        st.header("Global Military Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Countries", len(filtered_df))
        with col2:
            st.metric("Avg Budget ($B)", f"{filtered_df['military_expenditure_usd'].mean()/1000:.1f}")
        with col3:
            st.metric("Total Military", f"{(filtered_df['total_military'].sum()/1e6):.1f}M")
        with col4:
            st.metric("Data Freshness", datetime.now().strftime("%Y-%m-%d"))
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Top 10 countries by budget
            top_10 = filtered_df.nlargest(10, 'military_expenditure_usd')
            fig = px.bar(
                top_10,
                x='military_expenditure_usd',
                y='country',
                orientation='h',
                title="Top 10 Countries by Military Budget",
                labels={'military_expenditure_usd': 'Budget (Millions USD)', 'country': ''}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Regional distribution
            region_data = filtered_df.groupby('region')['total_military'].sum() if 'region' in filtered_df.columns else pd.Series()
            fig = px.pie(
                values=region_data,
                names=region_data.index,
                title="Military Personnel by Region"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Nation Profile")
        
        selected_country = st.selectbox(
            "Select Country",
            options=sorted(filtered_df['country'].unique()) if 'country' in filtered_df.columns else []
        )
        
        if selected_country:
            country_data = filtered_df[filtered_df['country'] == selected_country].iloc[0]
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Military Budget", f"${country_data.get('military_expenditure_usd', 0)/1000:.1f}B")
            with col2:
                st.metric("Active Personnel", f"{country_data.get('active_military_personnel', 0):,.0f}")
            with col3:
                st.metric("Rank", f"#{country_data.get('rank', 'N/A')}")
            
            st.markdown("---")
            st.subheader("Military Assets")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Aircraft", f"{country_data.get('aircraft', 0):,.0f}")
            with col2:
                st.metric("Tanks", f"{country_data.get('tanks', 0):,.0f}")
            with col3:
                st.metric("Artillery", f"{country_data.get('artillery', 0):,.0f}")
            with col4:
                st.metric("Navy Ships", f"{country_data.get('navy_ships', 0):,.0f}")
    
    with tab3:
        st.header("Comparative Analysis")
        
        # Compare KPIs
        countries_to_compare = st.multiselect(
            "Select countries to compare",
            options=filtered_df['country'].unique() if 'country' in filtered_df.columns else [],
            default=filtered_df['country'].unique()[:5] if len(filtered_df) > 5 else filtered_df['country'].unique()
        )
        
        if countries_to_compare:
            compare_df = filtered_df[filtered_df['country'].isin(countries_to_compare)]
            
            # Budget comparison
            fig = px.bar(
                compare_df,
                x='country',
                y='military_expenditure_usd',
                title="Military Budget Comparison",
                labels={'military_expenditure_usd': 'Budget (Millions USD)'}
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Personnel comparison
            fig = px.bar(
                compare_df,
                x='country',
                y='total_military',
                title="Total Military Personnel Comparison"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"*Dashboard updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

if __name__ == "__main__":
    main()

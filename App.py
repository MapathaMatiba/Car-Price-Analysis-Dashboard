import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Page configuration
st.set_page_config(
    page_title="Car Price Dashboard",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        color: #333;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        color: #4a4a4a;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab"][data-selected="true"] {
        background-color: #3498db;
        color: white;
    }
    .metric-card {
        background-color: #f1f5f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Load the dataset
@st.cache_data
def load_data():
    file_path = 'car_prices_rsa_update_011.csv'
    df = pd.read_csv(file_path)
    
    # Additional preprocessing
    df['price_category'] = pd.cut(df['price'], 
        bins=[0, 100000, 250000, 500000, float('inf')], 
        labels=['Budget', 'Mid-Range', 'Premium', 'Luxury']
    )
    
    return df

df = load_data()

# Sidebar
def sidebar():
    st.sidebar.image("https://img.icons8.com/ios/50/000000/car.png", width=100)
    st.sidebar.title("Car Price Analytics")
    
    analysis_type = st.sidebar.radio(
        "Select Analysis", 
        ["Overview", "Price Explorer", "Brand Comparison", "Advanced Insights"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 Use filters to dive deeper into the data!")
    
    return analysis_type

# Overview Tab
def overview_tab(df):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Total Records", value=len(df))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Unique Brands", value=df['brand'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Average Price", value=f"R {df['price'].mean():,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### Dataset Overview")
    
    # Interactive DataFrame
    st.dataframe(
        df.sample(10), 
        use_container_width=True,
        column_config={
            "price": st.column_config.NumberColumn(
                "Price (ZAR)",
                format="R %d"
            )
        }
    )

# Price Explorer Tab
def price_explorer_tab(df):
    st.markdown("### Price Distribution and Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(df, x="price_category", y="price", 
                     title="Price Distribution by Category",
                     labels={"price": "Price (ZAR)", "price_category": "Price Category"})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(df, x="engine_size", y="price", color="brand",
                         title="Engine Size vs Price",
                         labels={"price": "Price (ZAR)", "engine_size": "Engine Size (L)"})
        st.plotly_chart(fig, use_container_width=True)

# Brand Comparison Tab
def brand_comparison_tab(df):
    st.markdown("### Brand Performance")
    
    # Brand Price Comparison
    brand_avg_price = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    
    fig = px.bar(
        x=brand_avg_price.index, 
        y=brand_avg_price.values,
        title="Average Price by Brand",
        labels={"x": "Brand", "y": "Average Price (ZAR)"}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Brand Model Distribution
    model_count = df.groupby("brand")["model"].count().sort_values(ascending=False)
    
    fig = px.pie(
        values=model_count.values, 
        names=model_count.index, 
        title="Brand Model Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Advanced Insights Tab
def advanced_insights_tab(df):
    st.markdown("### Advanced Analytics")
    
    # Allow user to select x and y axes dynamically
    available_numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    available_categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    st.markdown("### Interactive Scatter Plot")
    x_axis = st.selectbox("Select X-axis", available_numeric_columns, index=0)
    y_axis = st.selectbox("Select Y-axis", available_numeric_columns, index=1)
    color_axis = st.selectbox("Color by", available_categorical_columns, index=0)
    
    # Dynamic scatter plot
    fig = px.scatter(
        df, 
        x=x_axis, 
        y=y_axis, 
        color=color_axis,
        title=f"{y_axis} vs {x_axis} by {color_axis}",
        labels={x_axis: x_axis, y_axis: y_axis}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation Heatmap
    correlation_columns = available_numeric_columns
    corr_matrix = df[correlation_columns].corr()
    
    fig = px.imshow(
        corr_matrix, 
        text_auto=True, 
        title="Feature Correlation Heatmap"
    )
    st.plotly_chart(fig, use_container_width=True)

# Main App
def main():
    analysis_type = sidebar()
    
    if analysis_type == "Overview":
        overview_tab(df)
    elif analysis_type == "Price Explorer":
        price_explorer_tab(df)
    elif analysis_type == "Brand Comparison":
        brand_comparison_tab(df)
    else:
        advanced_insights_tab(df)

if __name__ == "__main__":
    main()
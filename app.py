import streamlit as st
from generator import generate_etsy_content
from pdf_export import create_pdf

# Page Config
st.set_page_config(
    page_title="Muun AI - Etsy Generator",
    page_icon="🚀",
    layout="centered"
)

# Title & Description
st.title("🚀 Etsy Listing Generator")
st.markdown("""
    Create **SEO-optimized** titles, sales-driving descriptions, and 13 high-ranking tags in seconds.
    Perfect for skyrocketing your Etsy sales.
""")
st.markdown("---")

# User Input Form
with st.form("etsy_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        product_name = st.text_input("Product Name", placeholder="e.g. Handmade Ceramic Mug")
    with col2:
        target_audience = st.text_input("Target Audience", placeholder="e.g. Coffee Lovers, Gift for Mom")
        
    product_features = st.text_area(
        "Product Features & Details", 
        placeholder="Material, size, colors, backstory... (The more details, the better the result)", 
        height=150
    )
    
    # Submit Button
    submitted = st.form_submit_button("Generate Analysis ✨", type="primary")

# Result Section
if submitted:
    if not product_name or not product_features:
        st.warning("Please fill in both Product Name and Features.")
    else:
        # Loading Spinner
        with st.spinner("AI is working its magic... (This may take 10-15 seconds)"):
            
            # 1. Generate Content
            ai_result = generate_etsy_content(product_name, product_features, target_audience)
            
            # 2. Display Results
            st.success("Success! Here is your optimized listing:")
            st.text_area("Your Results (Copy & Paste)", value=ai_result, height=400)
            
            # 3. Create PDF
            pdf_data = create_pdf(ai_result)
            
            # Download Button
            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_data,
                file_name="Etsy_SEO_Report.pdf",
                mime="application/pdf"
            )

# Footer
st.markdown("---")
st.caption("Powered by Muun AI | Developed by Ismail Arda Baran")
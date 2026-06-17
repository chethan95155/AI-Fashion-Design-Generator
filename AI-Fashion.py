import streamlit as st
import google.generativeai as genai
from PIL import Image

# ==================================================
# CONFIGURE GEMINI API
# ==================================================

GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your actual Gemini API key

genai.configure(api_key=GOOGLE_API_KEY)

# ==================================================
# GEMINI FUNCTION
# ==================================================

def get_gemini_response(prompt, image_data=None):

    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        content = [prompt]

        if image_data:
            content.extend(image_data)

        response = model.generate_content(content)

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ==================================================
# IMAGE PROCESSING
# ==================================================

def input_image_setup(uploaded_file):

    if uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return image_parts

    return None


# ==================================================
# SESSION STATE
# ==================================================

if "fashion_profile" not in st.session_state:

    st.session_state.fashion_profile = {
        "gender": "Women",
        "category": "Dress",
        "style": "Casual",
        "colors": "Black, White",
        "fabric": "Cotton"
    }

# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="AI Fashion Design Generator",
    layout="wide"
)

st.title("👗 AI Fashion Design Generator")

st.markdown(
    "Design fashion outfits, analyze clothing images, explore trends, and discover similar products."
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("⚙ Fashion Preferences")

    gender = st.selectbox(
        "Gender",
        ["Women", "Men", "Unisex"]
    )

    category = st.selectbox(
        "Clothing Type",
        [
            "T-Shirt",
            "Hoodie",
            "Dress",
            "Jacket",
            "Kurta",
            "Saree",
            "Formal Wear"
        ]
    )

    style = st.selectbox(
        "Style",
        [
            "Casual",
            "Streetwear",
            "Luxury",
            "Party Wear",
            "Sportswear"
        ]
    )

    colors = st.text_input(
        "Preferred Colors",
        value="Black, White"
    )

    fabric = st.selectbox(
        "Fabric",
        [
            "Cotton",
            "Denim",
            "Silk",
            "Polyester",
            "Linen"
        ]
    )

    if st.button("Save Preferences"):

        st.session_state.fashion_profile = {
            "gender": gender,
            "category": category,
            "style": style,
            "colors": colors,
            "fabric": fabric
        }

        st.success("Preferences Saved Successfully")

# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🎨 Fashion Designer",
        "📸 Outfit Analyzer",
        "🛍 Product Suggestions",
        "📈 Trend Insights"
    ]
)

# ==================================================
# TAB 1 - FASHION DESIGNER
# ==================================================

with tab1:

    st.subheader("Create Your Fashion Design")

    user_prompt = st.text_area(
        "Describe your fashion idea",
        placeholder="Example: Oversized black hoodie with neon blue graphics and futuristic sleeves."
    )

    st.write("### Current Fashion Profile")

    st.json(st.session_state.fashion_profile)

    if st.button("Generate Fashion Design"):

        prompt = f"""
        Act as a professional fashion designer.

        Create a detailed fashion design based on:

        Gender:
        {st.session_state.fashion_profile['gender']}

        Category:
        {st.session_state.fashion_profile['category']}

        Style:
        {st.session_state.fashion_profile['style']}

        Colors:
        {st.session_state.fashion_profile['colors']}

        Fabric:
        {st.session_state.fashion_profile['fabric']}

        User Idea:
        {user_prompt}

        Provide:

        1. Design Name
        2. Design Description
        3. Color Palette
        4. Material Recommendations
        5. Front View Details
        6. Back View Details
        7. Fashion Appeal
        8. Estimated Market Price
        """

        with st.spinner("Generating Fashion Design..."):

            response = get_gemini_response(prompt)

        st.success("Design Generated")

        st.markdown(response)

        st.download_button(
            "Download Design",
            response,
            file_name="fashion_design.txt"
        )

# ==================================================
# TAB 2 - OUTFIT ANALYZER
# ==================================================

with tab2:

    st.subheader("Analyze an Outfit")

    uploaded_file = st.file_uploader(
        "Upload an outfit image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Outfit",
            width=400
        )

        if st.button("Analyze Outfit"):

            image_data = input_image_setup(uploaded_file)

            prompt = """
            Analyze the outfit in the image.

            Provide:

            1. Clothing Type
            2. Dominant Colors
            3. Fashion Style
            4. Fabric Estimate
            5. Suitable Occasion
            6. Matching Accessories
            7. Fashion Rating (/10)
            8. Estimated Market Price
            9. Current Trend Relevance
            """

            with st.spinner("Analyzing Outfit..."):

                response = get_gemini_response(
                    prompt,
                    image_data
                )

            st.success("Analysis Complete")

            st.markdown(response)

# ==================================================
# TAB 3 - PRODUCT SUGGESTIONS
# ==================================================

with tab3:

    st.subheader("Affordable Product Suggestions")

    if st.button("Find Similar Products"):

        prompt = f"""
            Act as a fashion shopping assistant.

            Suggest 5 affordable products similar to the following design:

            Category: {st.session_state.fashion_profile['category']}
            Style: {st.session_state.fashion_profile['style']}
            Colors: {st.session_state.fashion_profile['colors']}

            For each product provide:

            1. Product Name
            2. Brand
            3. Estimated Price
            4. Why it matches the design
            5. Available Online Stores
            (Amazon, Flipkart, Myntra, Ajio, Meesho, Nykaa Fashion, etc.)
            6. Search URL if available

            Format the response as a table.
            """

        with st.spinner("Searching Products..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# ==================================================
# TAB 4 - TREND INSIGHTS
# ==================================================

with tab4:

    st.subheader("Fashion Trend Insights")

    trend_category = st.text_input(
        "Enter Fashion Category",
        placeholder="Streetwear"
    )

    if st.button("Analyze Trends"):

        prompt = f"""
        Analyze current trends in:

        {trend_category}

        Provide:

        1. Trending Colors
        2. Popular Fabrics
        3. Popular Designs
        4. Celebrity Influence
        5. Market Demand
        6. Future Predictions
        7. Best Selling Products
        """

        with st.spinner("Analyzing Trends..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")
st.caption("AI Fashion Design Generator | Streamlit + Gemini AI")
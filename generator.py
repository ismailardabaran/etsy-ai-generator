import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_etsy_content(product_name, product_features, target_audience):
    """
    Connects to OpenAI to generate English SEO content.
    """
    
    # The Prompt (Instruction to AI)
    prompt = f"""
    Act as an expert Etsy SEO specialist with 10 years of experience.
    
    PRODUCT DETAILS:
    - Name: {product_name}
    - Features: {product_features}
    - Target Audience: {target_audience}

    YOUR TASK:
    1. Write a high-ranking, SEO-optimized Etsy Title (max 140 chars). Use strong keywords at the beginning.
    2. Write a compelling, emotional, and sales-oriented Product Description (2-3 paragraphs). Focus on benefits, not just features.
    3. Generate EXACTLY 13 specific SEO Tags (comma separated). These are crucial for Etsy search.
    
    OUTPUT FORMAT:
    Please use clear headers like:
    ### TITLE
    [Title here]
    
    ### DESCRIPTION
    [Description here]
    
    ### TAGS
    [Tags here]
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that helps Etsy sellers rank higher."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
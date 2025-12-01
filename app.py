import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="The Auditor", page_icon="💔")

# Title and Vibe
st.title("💔 The Relationship Auditor")
st.caption("Powered by IIM-Grade Logic & Heartless Algorithms")

# --- FOUNDER MODE: Load Key from Secrets ---
# This grabs the key you saved in Streamlit Settings so users don't have to enter it.
try:
    api_key = st.secrets["DEEPSEEK_API_KEY"]
except:
    st.error("🚨 System Error: DeepSeek API Key not found. Please add it to Streamlit Secrets.")
    st.stop()

# The Input
user_chat = st.text_area("Paste your chat history / text log here:", height=300, placeholder="He: hey\nMe: hey what's up\nHe: u up?...")

# The "Auditor" Prompt (Optimized for DeepSeek R1)
auditor_prompt = """
You are "The Auditor." You are NOT a therapist. You are a Lean Six Sigma Master Black Belt for Relationships.
Analyze the user's relationship situation to identify "wasteful expenditure" of emotional energy.

Your Tone:
- Clinical, Financial, Brutally Direct.
- Use terms like "Sunk Cost," "Opportunity Cost," "Asset Liability."
- No fluff. No "I hope you feel better."

Your Output format:
1. Power Dynamic Analysis (Who holds the leverage?)
2. Red Flag Audit (Identify specific toxic behaviors)
3. The Verdict (Buy, Hold, or Sell/Dump immediately)
"""

# The Button
if st.button("🚨 Audit My Relationship"):
    if not user_chat:
        st.error("Paste the chat. I can't audit a blank page.")
    else:
        # Connect to DeepSeek
        client = OpenAI(
            api_key=api_key, 
            base_url="https://api.deepseek.com"
        )
        
        with st.spinner("Crunching the numbers... Analyzing Leverage..."):
            try:
                # Use DeepSeek Reasoner for "Thinking" capability
                response = client.chat.completions.create(
                    model="deepseek-reasoner",
                    messages=[
                        {"role": "system", "content": auditor_prompt},
                        {"role": "user", "content": user_chat}
                    ]
                )
                
                # Get the content
                audit_result = response.choices[0].message.content
                
                # The Result
                st.success("Audit Complete.")
                st.markdown("---")
                st.markdown(audit_result)
                st.markdown("---")
                st.info("💡 Need a strategy to fix this? DM me on the IIM Portal for a Tier 1 Consult.")
                
            except Exception as e:
                st.error(f"Error: {e}")

import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="The Auditor", page_icon="💔")

# Title and "Founder" Vibe
st.title("💔 The Relationship Auditor")
st.caption("Powered by IIM-Grade Logic & Heartless Algorithms")

# Sidebar for the API Key (Safety First)
with st.sidebar:
    st.markdown("### 🔑 Unlocking the Auditor")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.markdown("[Get an API key here](https://platform.openai.com/account/api-keys)")
    st.warning("Cost: ~$0.01 per audit. Cheap.")

# The Input
user_chat = st.text_area("Paste your chat history / text log here:", height=300, placeholder="He: hey\nMe: hey what's up\nHe: u up?...")

# The "Auditor" Prompt
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
    if not api_key:
        st.error("I need an API key to run the numbers. Check the sidebar.")
    elif not user_chat:
        st.error("Paste the chat. I can't audit a blank page.")
    else:
        client = OpenAI(
    api_key=api_key, 
    base_url="https://api.deepseek.com"  # <--- This points it to DeepSeek's server
)
        
        with st.spinner("Crunching the numbers... Analyzing Leverage..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo", # Keeping it cheap for you
                    messages=[
                        {"role": "system", "content": auditor_prompt},
                        {"role": "user", "content": user_chat}
                    ]
                )
                
                audit_result = response.choices[0].message.content
                
                # The Result
                st.success("Audit Complete.")
                st.markdown("---")
                st.markdown(audit_result)
                st.markdown("---")
                st.info("💡 Need a strategy to fix this? DM me on the IIM Portal for a Tier 1 Consult.")
                
            except Exception as e:
                st.error(f"Error: {e}")

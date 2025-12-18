import streamlit as st
import random

# --------------------------------------------
# OMEGASTREAM SMART CUSTOMER SUPPORT CHATBOT
# --------------------------------------------

st.set_page_config(page_title="OmegaStream Support Chatbot",
                   page_icon="🎬",
                   layout="wide")

# ------------ SIDEBAR ---------------
st.sidebar.title("🎬 OmegaStream Support Center")
st.sidebar.subheader("Customer Details")

name = st.sidebar.text_input("Customer Name", "Guest User")
issue_type = st.sidebar.selectbox("Issue Category", 
                                  ["Account / Login Issue",
                                   "Payment & Billing",
                                   "Streaming / Playback",
                                   "Subscription Plan",
                                   "App Settings",
                                   "Other"])

st.sidebar.write("We're here to help, " + name + "! 😊")


# ---------------- SMART FAQ KNOWLEDGE BASE ----------------
faq = {

    "unable to login": """It looks like you're having trouble logging in.
Please make sure you are using the correct email and password.
If needed, click *'Forgot Password'* on the login page and you will instantly receive a reset link.
If this doesn’t help, you can try clearing your app cache or logging in from another device.""",

    "reset password": """No worries! You can reset your password easily.
Go to the OmegaStream login page → tap 'Forgot Password' → enter your registered email.
Check your inbox (and spam folder) for the reset link.
Follow the instructions to set a new password.""",

    "payment failed": """A payment failure usually occurs due to network issues, bank outages, or insufficient wallet/card balance.
Please retry the transaction after a minute.
If money was deducted, it will be auto-refunded within 24–48 hours.
You can also try another payment method like UPI, card, or wallet.""",

    "upgrade plan": """To upgrade your plan:
1. Open OmegaStream  
2. Go to Profile  
3. Tap on Subscription  
4. Select 'Upgrade Plan'  
Premium plans offer Ultra HD quality, offline downloads, multi-device streaming, and priority support.""",

    "video not playing": """This issue may be due to unstable internet or temporary app glitches.
Try these steps:
- Check if your internet speed is above 5 Mbps  
- Clear app cache  
- Restart the app  
- Reduce video quality  
If the issue continues, try on another device or network.""",

    "buffering": """Buffering happens when your internet speed fluctuates.
Try switching to a stable Wi-Fi/mobile network, reducing video quality, or restarting your router.""",

    "cancel subscription": """You can cancel anytime by going to:
Profile → Manage Subscription → Cancel Plan.
Your current plan will remain active until the end of the billing period.
You won’t be charged again unless you reactivate it.""",

    "refund": """Refunds are processed within 5–7 business days depending on your bank.
If your payment failed or you cancelled your subscription, the refund will be initiated automatically.
If not credited after 7 days, please reach out to our support team with your transaction ID.""",

    "change language": """To change language:
Settings → Content Preferences → Select Language.
You can switch audio, subtitles, and UI language as per your preference.""",

    "download issue": """Download issues usually happen due to low storage, unstable internet, or plan restrictions.
Please free up space, check internet connection, and ensure your plan supports offline downloads."""
}


# ---------------- SMART FALLBACK RESPONSES ----------------
fallback_responses = [
    "I’m not completely sure I understood that. Could you explain your issue in more detail?",
    "I want to help you better. Can you share a little more information?",
    "That seems interesting! Could you rephrase it so I can assist more accurately?",
    "I'm here for you. Can you describe the issue a bit more clearly?"
]


# ---------------- INTELLIGENT BOT REPLY FUNCTION ----------------
def bot_reply(user_msg):
    user_msg_lower = user_msg.lower()

    # Match FAQ keywords
    for key in faq:
        if key in user_msg_lower:
            return faq[key]

    # Smart understanding for general help
    if "problem" in user_msg_lower:
        return "I understand you're facing a problem. Could you tell me what exactly is happening so I can assist better?"

    if "help" in user_msg_lower:
        return "Of course! I'm here to help. Please describe the issue you're facing with OmegaStream."

    if "hi" in user_msg_lower or "hello" in user_msg_lower:
        return "Hello! 😊 How can I assist you today with your OmegaStream account or streaming experience?"

    if "thank" in user_msg_lower:
        return "You're welcome! If you need anything else, I’m right here to help. 💙"

    # fallback
    return random.choice(fallback_responses)


# ---------------- CHAT INTERFACE ----------------
st.title("🤖 OmegaStream AI Support Chatbot")
st.write("Hello! I'm your OmegaStream Support Assistant. How can I assist you today? 😊")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input:
        st.session_state.chat.append(("You", user_input))
        response = bot_reply(user_input)
        st.session_state.chat.append(("OmegaBot", response))

# Display chat conversation
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 OmegaBot:** {msg}")

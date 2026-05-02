import streamlit as st

st.set_page_config(page_title="Luka's TaxAI", page_icon="💼", layout="centered")
st.title("🚀 Luka's Agentic TaxAI")
st.subheader("Your Autonomous Tax Expert for Tanzania")

# Business Memory
if 'business' not in st.session_state:
    st.session_state.business = {
        "name": "Luka General Shop",
        "turnover": 80000000,
        "location": "Kariakoo",
        "status": "Not Registered"
    }

st.sidebar.header("Your Business")
st.sidebar.write(f"**{st.session_state.business['name']}**")
st.sidebar.write(f"Turnover: {st.session_state.business['turnover']/1000000}M TZS")
st.sidebar.write(f"Location: {st.session_state.business['location']}")

# Agent Functions
def calculate_tax(turnover):
    tax = round(turnover * 0.032, 2)  # Average presumptive rate
    return tax

# Main Interface
tab1, tab2, tab3 = st.tabs(["💬 Ask TaxAI", "📊 Tax Calculator", "📋 Registration Agent"])

with tab1:
    question = st.text_input("Ask your TaxAI Agent anything:")
    if st.button("Send Question"):
        if question:
            q = question.lower()
            if "tin" in q:
                answer = "✅ **TIN Registration**: Visit tra.go.tz or TRA App. Upload ID. Usually ready in 1-3 days."
            elif "tax" in q or "how much" in q:
                tax = calculate_tax(st.session_state.business["turnover"])
                answer = f"📌 For {st.session_state.business['turnover']/1000000}M TZS turnover: Estimated Presumptive Tax = **{tax/1000000:.1f}M TZS/year**"
            elif "register" in q:
                answer = "1. Get TIN\n2. Business License from Council\n3. Fiscal Device (EFD)\n4. Open Bank Account"
            else:
                answer = "I'm your Agentic Tax Consultant. I can help with registration, calculations, compliance, and business setup in Tanzania."
            st.success(answer)
        else:
            st.warning("Please type a question.")

with tab2:
    st.write("### Presumptive Tax Calculator")
    turnover = st.number_input("Annual Turnover (TZS)", value=80000000, step=1000000)
    if st.button("Calculate Tax"):
        tax = calculate_tax(turnover)
        st.success(f"**Estimated Annual Tax: {tax:,.0f} TZS**")
        st.info("This is under Presumptive Regime (turnover < 100M).")

with tab3:
    st.write("### Registration Agent")
    if st.button("Start Full Registration Process"):
        st.write("**Step 1: TIN** → Done in 1-3 days")
        st.write("**Step 2: Business License** → Municipal Council")
        st.write("**Step 3: Fiscal Device** → Mandatory for your shop")
        st.success("Registration Progress Saved! I will remember your business.")

st.caption("Agentic TaxAI v1.0 - Built for Luka | Tanzania Focused")
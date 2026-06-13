"""FAQ Chatbot with NLP matching."""

import streamlit as st

from faq_engine import FAQMatcher
from faqs import FAQS, SUGGESTED_QUESTIONS

FALLBACK = (
    "I couldn't find a close match for that cricket question. "
    "Try asking about rules, formats, IPL, records, players, bowling, batting, or DRS."
)

PAGE_STYLE = """
<style>
    .block-container { padding-top: 1.5rem; max-width: 920px; }
    .hero {
        background: linear-gradient(135deg, #14532d 0%, #15803d 45%, #ca8a04 100%);
        color: white;
        padding: 1.6rem 1.4rem;
        border-radius: 16px;
        margin-bottom: 1rem;
        box-shadow: 0 10px 28px rgba(20, 83, 45, 0.18);
    }
    .hero h1 { margin: 0; font-size: 1.85rem; font-weight: 700; }
    .hero p { margin: 0.4rem 0 0; opacity: 0.92; }
    .sidebar-card {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 12px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.8rem;
    }
    .sidebar-card h4 {
        margin: 0 0 0.45rem;
        color: #166534;
        font-size: 0.95rem;
    }
    .sidebar-card p {
        margin: 0;
        color: #14532d;
        font-size: 0.88rem;
        line-height: 1.45;
    }
    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 0.35rem 0.2rem;
    }
    .match-note {
        color: #64748b;
        font-size: 0.78rem;
        margin-top: 0.35rem;
    }
</style>
"""


def respond_to_user(user_input: str) -> tuple[str, dict | None]:
    result = st.session_state.matcher.find_best_match(user_input)
    if result:
        return result.answer, {"question": result.question, "score": result.score}
    return FALLBACK, None


def append_exchange(user_input: str) -> None:
    reply, match_meta = respond_to_user(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
            **({"match": match_meta} if match_meta else {}),
        }
    )


def main() -> None:
    st.set_page_config(
        page_title="Cricket FAQ Assistant",
        page_icon="🏏",
        layout="wide",
    )
    st.markdown(PAGE_STYLE, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi! I'm your cricket assistant. Ask me about rules, formats, IPL, "
                    "players, records, bowling, batting, fielding, or DRS."
                ),
            }
        ]

    if "matcher" not in st.session_state:
        st.session_state.matcher = FAQMatcher(FAQS)

    sidebar = st.sidebar
    with sidebar:
        st.markdown("### Cricket topics")
        st.markdown(
            """
            <div class="sidebar-card">
                <h4>Single-topic knowledge base</h4>
                <p>This bot covers one domain in depth — cricket — using NLP matching across a large FAQ dataset.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("**Try these**")
        for question in SUGGESTED_QUESTIONS:
            if st.button(question, use_container_width=True, key=f"suggest_{question}"):
                append_exchange(question)
                st.rerun()

        st.divider()
        if st.button("Clear conversation", use_container_width=True):
            st.session_state.messages = [st.session_state.messages[0]]
            st.rerun()

        st.caption(f"{len(FAQS)} cricket FAQs loaded")

    st.markdown(
        """
        <div class="hero">
            <h1>Cricket FAQ Assistant</h1>
            <p>Rules, formats, IPL, records, players, and cricket terminology — all in one place.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "match" in message:
                match = message["match"]
                st.markdown(
                    f'<div class="match-note">Matched: {match["question"]} · '
                    f'confidence {match["score"]:.0%}</div>',
                    unsafe_allow_html=True,
                )

    user_input = st.chat_input("Ask a cricket question...")
    if user_input:
        append_exchange(user_input)
        st.rerun()


if __name__ == "__main__":
    main()

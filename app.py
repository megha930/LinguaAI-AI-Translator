
import streamlit as st
import requests

st.set_page_config(
    page_title="LinguaAI Translator",
    page_icon="🌍",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

# Professional design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f0fdfa);
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    background: #312e81;
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
}
.hero h1 {
    font-size: 40px;
    margin: 0;
}
.hero p {
    font-size: 17px;
}
.stButton > button {
    background: #4f46e5;
    color: white;
    border-radius: 10px;
    min-height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌍 LinguaAI</h1>
    <p>Your Simple AI Language Translator</p>
    <p>Translate text between different languages with ease.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

st.subheader("✍️ Translate Your Text")
st.write("Choose your languages and enter the text below.")

with st.form("translator_form"):
    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Translate from",
            list(languages.keys())
        )

    with col2:
        target = st.selectbox(
            "Translate to",
            list(languages.keys()),
            index=1
        )

    text = st.text_area(
        "Enter your text",
        placeholder="Example: Good morning, how are you?",
        height=150
    )

    submitted = st.form_submit_button(
        "🌐 Translate Now",
        use_container_width=True
    )

if submitted:
    if not text.strip():
        st.warning("Please enter some text first.")
        st.session_state.result = None

    elif source == target:
        result = text.strip()

        st.session_state.result = {
            "original": text.strip(),
            "translated": result,
            "source": source,
            "target": target
        }

        st.session_state.history.insert(
            0, st.session_state.result.copy()
        )

    else:
        try:
            with st.spinner("Translating... Please wait"):
                response = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={
                        "q": text.strip(),
                        "langpair": (
                            f"{languages[source]}|{languages[target]}"
                        )
                    },
                    timeout=20
                )
                response.raise_for_status()
                data = response.json()

            result = data.get(
                "responseData", {}
            ).get("translatedText", "").strip()

            if data.get("responseStatus") != 200 or not result:
                st.session_state.result = None
                st.error("Translation unavailable. Please try again.")
                if data.get("responseDetails"):
                    st.caption(data["responseDetails"])

            else:
                entry = {
                    "original": text.strip(),
                    "translated": result,
                    "source": source,
                    "target": target
                }

                st.session_state.result = entry

                # Avoid saving the same entry repeatedly
                if not any(
                    old["original"] == entry["original"]
                    and old["source"] == entry["source"]
                    and old["target"] == entry["target"]
                    for old in st.session_state.history
                ):
                    st.session_state.history.insert(0, entry.copy())

        except requests.exceptions.RequestException as error:
            st.session_state.result = None
            st.error("Could not connect to the translation service.")
            st.caption(str(error))

        except ValueError:
            st.session_state.result = None
            st.error("Invalid response from the translation service.")

# Show the latest translation
if st.session_state.result:
    item = st.session_state.result

    st.divider()
    st.subheader("✅ Translated Text")
    st.write(f"**{item['source']} → {item['target']}**")

    st.text_area(
        "Translation Result",
        value=item["translated"],
        height=120,
        key="translation_result_box"
    )

    st.download_button(
        "⬇️ Download Translation",
        data=item["translated"],
        file_name="translated_text.txt",
        mime="text/plain"
    )

# History
st.divider()
st.subheader("🕘 Translation History")

if st.session_state.history:
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.session_state.result = None
        st.rerun()

    for number, item in enumerate(
        st.session_state.history, start=1
    ):
        with st.expander(
            f"{number}. {item['source']} → {item['target']}"
        ):
            st.markdown("**Original Text**")
            st.write(item["original"])

            st.markdown("**Translated Text**")
            st.write(item["translated"])

            st.download_button(
                "Download This Translation",
                data=item["translated"],
                file_name=f"translation_{number}.txt",
                mime="text/plain",
                key=f"history_download_{number}"
            )
else:
    st.info("No translations yet. Translate your first sentence!")

# Project information
st.divider()
st.subheader("📌 About LinguaAI")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Technology**")
    st.write("Python and Streamlit")

with col2:
    st.markdown("**Languages**")
    st.write("7 language options")

with col3:
    st.markdown("**Translation**")
    st.write("MyMemory online API")

st.caption(
    "LinguaAI | Artificial Intelligence Internship Project"
)

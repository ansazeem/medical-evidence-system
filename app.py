import streamlit as st
from pipeline import run_pipeline

st.set_page_config(page_title="Medical Query Pipeline", layout="centered")
st.title("Medical Query Pipeline")
st.caption("Pakistan-specific public health question answering")

query = st.text_input("Enter your query", placeholder="e.g. What is the prevalence of hepatitis C in Punjab?")

if st.button("Search") and query.strip():
    with st.spinner("Searching..."):
        out = run_pipeline(query.strip(), debug=False)

    st.markdown(f"**Mode:** `{out['mode']}` | **Type:** `{out['query_type']}` | **Expanded:** `{out['expanded']}`")

    st.markdown("### Answer")
    st.write(out["answer"])

    if out.get("assumptions"):
        st.markdown("### Assumptions")
        for a in out["assumptions"]:
            st.markdown(f"- {a}")

    if out.get("missing"):
        st.markdown("### Missing Information")
        for m in out["missing"]:
            st.markdown(f"- {m}")

    st.markdown("### Sources")
    accepted = out.get("accepted_sources", [])
    if accepted:
        for s in accepted[:5]:
            url = s.get("url", "")
            label = s.get("reliability_label", "")
            score = s.get("reliability_score", 0)
            st.markdown(f"- [{url}]({url}) — **{label}** ({score:.2f})")
    else:
        for h in out["hits"][:5]:
            url = h["meta"].get("url", "")
            st.markdown(f"- [{url}]({url})")

    if out.get("rejected_sources"):
        with st.expander(f"Rejected sources ({len(out['rejected_sources'])})"):
            for s in out["rejected_sources"]:
                st.markdown(f"- {s.get('url','')} — {s.get('reliability_label','')}")
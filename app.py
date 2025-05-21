
import streamlit as st
from port_scanner_with_shodan import scan_ports, check_shodan

st.title("🔐 ThreatAware Port Scanner")
target = st.text_input("Enter IP address to scan")

if st.button("Start Scan") and target:
    st.info("Scanning...")
    ports = scan_ports(target)
    if ports:
        st.success(f"Open ports: {ports}")
        st.write("Fetching SHODAN data...")
        check_shodan(target)
    else:
        st.warning("No open ports found.")

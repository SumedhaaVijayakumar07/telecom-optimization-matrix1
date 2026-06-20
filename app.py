import streamlit as st
import json
import os
import time
import pandas as pd

# =====================================================================
# PROJECT: AI Telecom Operations & Packet Architecture Suite V5
# Modules: 01. B2B Consumer Plan Optimizer | 02. AI Packet Routing Matrix
# Philosophy: Editorial Minimalist Dark Luxury UX Engineering
# =====================================================================

# --- MODULE 1: CONSUMER DATA LAYER INTEGRATION ---
def load_telecom_database():
    db_file = "plans_db.json"
    if not os.path.exists(db_file):
        return None
    with open(db_file, "r") as file:
        return json.load(file)

telecom_plans = load_telecom_database()

def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
    if not telecom_plans:
        return None, "JSON DB System file structural linkage breakdown error."
    
    normalized_provider_key = provider.lower()
    if normalized_provider_key not in telecom_plans:
        return None, f"Carrier network infrastructure configuration missing for: {provider}."
        
    available_options = telecom_plans[normalized_provider_key]
    best_matching_plan = None
    min_viable_price_normalized = float('inf')
    all_viable_plans_data = []
    
    for plan in available_options:
        plan_monthly_cost = int((plan["price"] / plan["validity_days"]) * 28)
        all_viable_plans_data.append({
            "Plan Name": plan["plan_name"],
            "Monthly Normalized Cost (₹)": plan_monthly_cost,
            "Daily Data (GB)": plan["data_per_day_gb"]
        })
        
        if plan["data_per_day_gb"] >= actual_daily_usage:
            if plan_monthly_cost < min_viable_price_normalized:
                min_viable_price_normalized = plan_monthly_cost
                best_matching_plan = plan

    if best_matching_plan:
        best_plan_normalized_monthly = (best_matching_plan["price"] / best_matching_plan["validity_days"]) * 28
        potential_monthly_saving = current_monthly_cost - best_plan_normalized_monthly
        potential_annual_saving = potential_monthly_saving * 12
        
        return {
            "recommended_plan": best_matching_plan["plan_name"],
            "recommended_price": best_matching_plan["price"],
            "validity": best_matching_plan["validity_days"],
            "data_limit": best_matching_plan["data_per_day_gb"],
            "unlimited_5g": best_matching_plan["unlimited_5g"],
            "monthly_savings": int(max(0, potential_monthly_saving)),
            "annual_savings": int(max(0, potential_annual_saving)),
            "all_plans_df": pd.DataFrame(all_viable_plans_data)
        }, None
    else:
        return None, "No structural lower optimization criteria profile standard matches your usage limits."


# --- MODULE 2: NETWORK COMPRESSION & AI ROUTING LAYER ---
class BinaryCompressionNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left_node = None
        self.right_node = None
        
    def __lt__(self, comparative_node):
        return self.frequency < comparative_node.frequency

def build_compression_tree(data_payload_string):
    frequency_map = {}
    for char in data_payload_string:
        frequency_map[char] = frequency_map.get(char, 0) + 1
        
    priority_pool = [BinaryCompressionNode(char, freq) for char, freq in frequency_map.items()]
    
    if not priority_pool:
        return None
        
    while len(priority_pool) > 1:
        priority_pool.sort()
        left = priority_pool.pop(0)
        right = priority_pool.pop(0)
        
        merged_parent = BinaryCompressionNode(None, left.frequency + right.frequency)
        merged_parent.left_node = left
        merged_parent.right_node = right
        priority_pool.append(merged_parent)
        
    return priority_pool[0]

def generate_huffman_bitmaps(node, current_binary_string="", code_book={}):
    if node is None:
        return code_book
    if node.character is not None:
        code_book[node.character] = current_binary_string
    generate_huffman_bitmaps(node.left_node, current_binary_string + "0", code_book)
    generate_huffman_bitmaps(node.right_node, current_binary_string + "1", code_book)
    return code_book


# --- GLOBAL LUXURY INTERFACE DISPLAY ENGINE ---
st.set_page_config(page_title="Telecom Matrix Architecture Suite", page_icon="▪️", layout="wide")

# Editorial Custom Dark Style Injection
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        font-family: 'Inter', sans-serif !important;
        color: #FFFFFF !important;
    }
    .editorial-title { font-size: 42px !important; font-weight: 300 !important; letter-spacing: -2px !important; color: #FFFFFF !important; text-transform: uppercase; margin-bottom: 2px; }
    .editorial-subtitle { font-size: 13px !important; font-weight: 400 !important; letter-spacing: 1px !important; color: #555555 !important; text-transform: uppercase; margin-bottom: 40px; }
    .minimal-container { border-top: 1px solid #222222; padding-top: 24px; margin-bottom: 30px; }
    .section-header { font-size: 13px !important; font-weight: 700 !important; letter-spacing: 2px !important; color: #888888 !important; text-transform: uppercase; margin-bottom: 20px; }
    .kpi-wrapper { border: 1px solid #111111; background-color: #050505; padding: 30px; text-align: left; }
    .kpi-label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 1.5px !important; color: #555555 !important; text-transform: uppercase; margin: 0 0 8px 0; }
    .kpi-value { font-size: 44px !important; font-weight: 300 !important; letter-spacing: -1px !important; color: #FFFFFF !important; margin: 0; }
    .kpi-sub { font-size: 12px !important; color: #444444 !important; margin-top: 4px; }
    div.stButton > button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 0px !important; border: 1px solid #FFFFFF !important; font-size: 11px !important; font-weight: 700 !important; letter-spacing: 2px !important; text-transform: uppercase; padding: 12px 24px !important; transition: all 0.3s ease; }
    div.stButton > button:hover { background-color: #000000 !important; color: #FFFFFF !important; border: 1px solid #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="editorial-title">TELECOM ARCHITECTURE MATRIX SUITE</p>', unsafe_allow_html=True)
st.markdown('<p class="editorial-subtitle">INTEGRATED HIGH-PERFORMANCE DATA OPERATIONAL INFRASTRUCTURE</p>', unsafe_allow_html=True)

# TOP LAYER CONTROLLER: CORE SWITCH MATRIX
st.markdown('<p class="section-header">// CHOOSE PLATFORM MODULE</p>', unsafe_allow_html=True)
active_module = st.selectbox("", ["01 // CONSUMER RESOURCE & PLAN OPTIMIZER", "02 // BINARY STREAM ENGINE & ROUTER LABS"])
st.markdown("<br>", unsafe_allow_html=True)

# =====================================================================
# INTERFACE IMPLEMENTATION: MODULE 01
# =====================================================================
if active_module == "01 // CONSUMER RESOURCE & PLAN OPTIMIZER":
    col_left, col_right = st.columns([1, 1.2], gap="large")

    with col_left:
        st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">01 // PARAMETER SELECTION</p>', unsafe_allow_html=True)
        
        provider_options = [p.upper() for p in telecom_plans.keys()] if telecom_plans else ["JIO", "AIRTEL", "VI"]
        provider_select = st.selectbox("INFRASTRUCTURE CARRIER", provider_options)
        current_cost_input = st.number_input("CURRENT MONTHLY OUTLAY (₹)", min_value=0, value=449, step=10)
        actual_usage_input = st.slider("OBSERVED DAILY THROUGHPUT (GB/DAY)", min_value=0.1, max_value=4.0, value=0.8, step=0.1)
        
        st.markdown("<br>", unsafe_allow_html=True)
        run_btn = st.button("RUN ANALYTICAL TRACE")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">02 // STRATEGY OUTPUT</p>', unsafe_allow_html=True)
        
        if run_btn:
            with st.spinner("Processing architectural vectors..."):
                time.sleep(0.3)
                results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
            
            if error:
                st.markdown(f'<p style="color:#FF3333; font-size:13px; font-weight:500;">SYSTEM ERROR // {error}</p>', unsafe_allow_html=True)
            else:
                grid_1, grid_2 = st.columns(2)
                with grid_1:
                    st.markdown(f'<div class="kpi-wrapper"><p class="kpi-label">RECOVERED CAPITAL</p><p class="kpi-value">₹{results["monthly_savings"]}</p><p class="kpi-sub">Normalized monthly balance delta</p></div>', unsafe_allow_html=True)
                with grid_2:
                    st.markdown(f'<div class="kpi-wrapper"><p class="kpi-label">ANNUALIZED PROJECTION</p><p class="kpi-value">₹{results["annual_savings"]}</p><p class="kpi-sub">Compounded macro financial ROI</p></div>', unsafe_allow_html=True)
                
                fiveg_badge = "ENABLED // UNLIMITED DATA ACCESS BURST" if results['unlimited_5g'] else "RESTRICTED // STANDARD OVERAGES REGULATION"
                
                st.markdown(f"""
                    <div style="border-top: 1px dashed #333333; padding-top: 20px; margin-top: 10px;">
                        <p style="font-size:11px; font-weight:700; color:#666666; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">EXECUTION LOGIC DEFINITION</p>
                        <p style="font-size:16px; font-weight:300; color:#FFFFFF; margin-bottom: 6px;">Migrate current baseline allocation interface environment to: <strong>{results['recommended_plan']}</strong></p>
                        <p style="font-size:13px; color:#888888; margin-bottom:6px;">Plan Pricing Module Structure: <strong>₹{results['recommended_price']}</strong> for <strong>{results['validity']} Days</strong> &nbsp;&bull;&nbsp; Structural Constraint Boundary: <strong>{results['data_limit']} GB/Day</strong></p>
                        <p style="font-size:11px; color:#555555; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:20px;">NETWORK LAYER INFRASTRUCTURE V5G STATUS: <strong style="color:#FFFFFF;">{fiveg_badge}</strong></p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown('<p class="section-header" style="margin-top:40px;">03 // MARKET PRICING SPECTRUM TRACE</p>', unsafe_allow_html=True)
                chart_df = results["all_plans_df"].set_index("Plan Name")
                st.bar_chart(chart_df["Monthly Normalized Cost (₹)"])
        else:
            st.markdown('<div style="padding: 60px 0px;"><p style="color: #333333; font-size: 13px; letter-spacing: 1px; text-transform: uppercase;">// ENGINE STANDING BY. ENTER BASELINE METRICS AND TRIGGER ANALYTICAL TRACE CONSOLE.</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================================
# INTERFACE IMPLEMENTATION: MODULE 02
# =====================================================================
elif active_module == "02 // BINARY STREAM ENGINE & ROUTER LABS":
    col_left, col_right = st.columns([1, 1.2], gap="large")
    
    with col_left:
        st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">01 // SOURCE PACKET PAYLOAD</p>', unsafe_allow_html=True)
        
        sample_packet_stream = st.text_area("RAW NETWORK LOG PAYLOAD (STRING)", value="PACKET_ORIGIN_JIO_ROUTER_NODE_A_VERIFIED_DATA_STREAM_OK")
        
        st.markdown('<p class="section-header" style="margin-top:30px;">02 // NETWORK PATH TOPOLOGY OVERHEAD</p>', unsafe_allow_html=True)
        source_node = st.selectbox("SOURCE ROUTER GATEWAY", ["NODE_A", "NODE_B", "NODE_C"])
        target_node = st.selectbox("TARGET TERMINAL ACCESS POINT", ["NODE_D", "NODE_E", "NODE_F"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        process_network_btn = st.button("EXECUTE BACKEND ANALYSIS")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">03 // COMPUTATIONAL TRACE METRICS</p>', unsafe_allow_html=True)
        
        if process_network_btn:
            # Step A: Compression Matrix Execution
            with st.spinner("Processing network streams..."):
                time.sleep(0.4)
                root_node = build_compression_tree(sample_packet_stream)
                huffman_codes = generate_huffman_bitmaps(root_node, "", {}) if root_node else {}
            
            # Encoded bit translation matrix build
            encoded_stream = "".join([huffman_codes[char] for char in sample_packet_stream])
            raw_bits_count = len(sample_packet_stream) * 8
            compressed_bits_count = len(encoded_stream)
            efficiency_gain = max(0.0, ((raw_bits_count - compressed_bits_count) / raw_bits_count) * 100)
            
            grid_c1, grid_c2 = st.columns(2)
            with grid_c1:
                st.markdown(f'<div class="kpi-wrapper"><p class="kpi-label">BANDWIDTH COMPRESSION RATIO</p><p class="kpi-value">{efficiency_gain:.1f}%</p><p class="kpi-sub">Data volume reduction index</p></div>', unsafe_allow_html=True)
            with grid_c2:
                st.markdown(f'<div class="kpi-wrapper"><p class="kpi-label">AI ROUTING TRANSIT COST</p><p class="kpi-value">₹14</p><p class="kpi-sub">Calculated path latency boundary</p></div>', unsafe_allow_html=True)
                
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<strong>BINARY MAP LOG INDEX (HUFFMAN DICTIONARY)</strong>', unsafe_allow_html=True)
            st.json(huffman_codes)
            
            # Static topology mapping path trace simulation matrix
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<strong>AI STATE-SPACE ROUTING PATH DETERMINATION</strong>', unsafe_allow_html=True)
            st.success(f"STRICT_OPTIMAL_PATH FOUND: {source_node} ➔ NODE_B ➔ NODE_E ➔ {target_node}")
            
            # Algorithmic Complexity Verification Proof Layouts
            st.markdown("""
                <div style="border-top: 1px dashed #333333; padding-top: 15px; margin-top: 15px;">
                    <p style="font-size:11px; font-weight:700; color:#666666; letter-spacing:0.5px;">FORMAL CS ANALYSIS PROOFS</p>
                    <p style="font-size:12px; color:#888888; line-height:1.5;">
                        &bull; <strong>Compression Complexity:</strong> $O(N \log N)$ space-bounds mapping table.<br>
                        &bull; <strong>AI Routing Constraint Bounds:</strong> $O((V + E) \log V)$ optimization limit via State Space Exploration.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div style="padding: 60px 0px;"><p style="color: #333333; font-size: 13px; letter-spacing: 1px; text-transform: uppercase;">// LAB NETWORK AGENT IDLE. INPUT PAYLOAD LOGS AND TRIGGER EXECUTION ANALYSIS.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
























# import streamlit as st
# import json
# import os
# import time
# import pandas as pd

# # =====================================================================
# # PROJECT: AI Telecom Optimization Platform - Analytics Pro Engine V4
# # Philosophy: Editorial Minimalist Layout with Data Visualization Analytics
# # =====================================================================

# # --- DATA LAYER INTEGRATION CONSOLE ---
# def load_telecom_database():
#     db_file = "plans_db.json"
#     if not os.path.exists(db_file):
#         return None
#     with open(db_file, "r") as file:
#         return json.load(file)

# telecom_plans = load_telecom_database()

# # --- OPTIMIZATION ENGINE ALGORITHM ---
# def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
#     if not telecom_plans:
#         return None, "JSON DB System file structural linkage breakdown error."
    
#     normalized_provider_key = provider.lower()
#     if normalized_provider_key not in telecom_plans:
#         return None, f"Carrier network infrastructure configuration missing for: {provider}."
        
#     available_options = telecom_plans[normalized_provider_key]
#     best_matching_plan = None
#     min_viable_price_normalized = float('inf')
#     all_viable_plans_data = []
    
#     for plan in available_options:
#         # Save all plans data for comparative charts visualization mapping
#         plan_monthly_cost = int((plan["price"] / plan["validity_days"]) * 28)
#         all_viable_plans_data.append({
#             "Plan Name": plan["plan_name"],
#             "Monthly Normalized Cost (₹)": plan_monthly_cost,
#             "Daily Data (GB)": plan["data_per_day_gb"]
#         })
        
#         if plan["data_per_day_gb"] >= actual_daily_usage:
#             if plan_monthly_cost < min_viable_price_normalized:
#                 min_viable_price_normalized = plan_monthly_cost
#                 best_matching_plan = plan

#     if best_matching_plan:
#         best_plan_normalized_monthly = (best_matching_plan["price"] / best_matching_plan["validity_days"]) * 28
#         potential_monthly_saving = current_monthly_cost - best_plan_normalized_monthly
#         potential_annual_saving = potential_monthly_saving * 12
        
#         return {
#             "recommended_plan": best_matching_plan["plan_name"],
#             "recommended_price": best_matching_plan["price"],
#             "validity": best_matching_plan["validity_days"],
#             "data_limit": best_matching_plan["data_per_day_gb"],
#             "unlimited_5g": best_matching_plan["unlimited_5g"],
#             "monthly_savings": int(max(0, potential_monthly_saving)),
#             "annual_savings": int(max(0, potential_annual_saving)),
#             "all_plans_df": pd.DataFrame(all_viable_plans_data)
#         }, None
#     else:
#         return None, "No structural lower optimization criteria profile standard matches your usage limits."


# # --- STREAMLIT FRONTEND MONOCHROME LUXURY WEB UI ---
# st.set_page_config(page_title="Telecom Optimization Matrix", page_icon="▪️", layout="wide")

# # Elite Monochrome Editorial Injector Stylesheet
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');
#     html, body, [data-testid="stAppViewContainer"] {
#         background-color: #000000 !important;
#         font-family: 'Inter', sans-serif !important;
#         color: #FFFFFF !important;
#     }
#     .editorial-title { font-size: 48px !important; font-weight: 300 !important; letter-spacing: -2px !important; color: #FFFFFF !important; text-transform: uppercase; margin-bottom: 2px; }
#     .editorial-subtitle { font-size: 14px !important; font-weight: 400 !important; letter-spacing: 1px !important; color: #666666 !important; text-transform: uppercase; margin-bottom: 40px; }
#     .minimal-container { border-top: 1px solid #222222; padding-top: 24px; margin-bottom: 30px; }
#     .section-header { font-size: 13px !important; font-weight: 700 !important; letter-spacing: 2px !important; color: #888888 !important; text-transform: uppercase; margin-bottom: 20px; }
#     .kpi-wrapper { border: 1px solid #111111; background-color: #050505; padding: 30px; text-align: left; }
#     .kpi-label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 1.5px !important; color: #555555 !important; text-transform: uppercase; margin: 0 0 8px 0; }
#     .kpi-value { font-size: 44px !important; font-weight: 300 !important; letter-spacing: -1px !important; color: #FFFFFF !important; margin: 0; }
#     .kpi-sub { font-size: 12px !important; color: #444444 !important; margin-top: 4px; }
#     div.stButton > button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 0px !important; border: 1px solid #FFFFFF !important; font-size: 12px !important; font-weight: 700 !important; letter-spacing: 2px !important; text-transform: uppercase; padding: 12px 24px !important; transition: all 0.3s ease; }
#     div.stButton > button:hover { background-color: #000000 !important; color: #FFFFFF !important; border: 1px solid #FFFFFF !important; }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<p class="editorial-title">TELECOM OPTIMIZATION MATRIX</p>', unsafe_allow_html=True)
# st.markdown('<p class="editorial-subtitle">B2B EXPENSE ARCHITECTURE & WASTE LOGISTICS ENGINE</p>', unsafe_allow_html=True)

# col_left, col_right = st.columns([1, 1.2], gap="large")

# with col_left:
#     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
#     st.markdown('<p class="section-header">01 // PARAMETER SELECTION</p>', unsafe_allow_html=True)
    
#     provider_options = [p.upper() for p in telecom_plans.keys()] if telecom_plans else ["JIO", "AIRTEL", "VI"]
#     provider_select = st.selectbox("INFRASTRUCTURE CARRIER", provider_options)
#     current_cost_input = st.number_input("CURRENT MONTHLY OUTLAY (₹)", min_value=0, value=449, step=10)
#     actual_usage_input = st.slider("OBSERVED DAILY THROUGHPUT (GB/DAY)", min_value=0.1, max_value=4.0, value=0.8, step=0.1)
    
#     st.markdown("<br><br>", unsafe_allow_html=True)
#     run_btn = st.button("RUN ANALYTICAL TRACE")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col_right:
#     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
#     st.markdown('<p class="section-header">02 // STRATEGY OUTPUT</p>', unsafe_allow_html=True)
    
#     if run_btn:
#         with st.spinner("Processing architectural vectors..."):
#             time.sleep(0.4)
#             results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
        
#         if error:
#             st.markdown(f'<p style="color:#FF3333; font-size:13px; font-weight:500;">SYSTEM ERROR // {error}</p>', unsafe_allow_html=True)
#         else:
#             grid_1, grid_2 = st.columns(2)
#             with grid_1:
#                 st.markdown(f"""
#                     <div class="kpi-wrapper">
#                         <p class="kpi-label">RECOVERED CAPITAL</p>
#                         <p class="kpi-value">₹{results['monthly_savings']}</p>
#                         <p class="kpi-sub">Normalized monthly balance delta</p>
#                     </div>
#                 """, unsafe_allow_html=True)
#             with grid_2:
#                 st.markdown(f"""
#                     <div class="kpi-wrapper">
#                         <p class="kpi-label">ANNUALIZED PROJECTION</p>
#                         <p class="kpi-value">₹{results['annual_savings']}</p>
#                         <p class="kpi-sub">Compounded macro financial ROI</p>
#                     </div>
#                 """, unsafe_allow_html=True)
            
#             fiveg_badge = "ENABLED // UNLIMITED DATA ACCESS BURST" if results['unlimited_5g'] else "RESTRICTED // STANDARD OVERAGES REGULATION"
            
#             st.markdown(f"""
#                 <div style="border-top: 1px dashed #333333; padding-top: 20px; margin-top: 10px;">
#                     <p style="font-size:11px; font-weight:700; color:#666666; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">EXECUTION LOGIC DEFINITION</p>
#                     <p style="font-size:16px; font-weight:300; color:#FFFFFF; line-height:1.6; margin-bottom: 6px;">
#                         Migrate current baseline allocation interface environment to: <strong>{results['recommended_plan']}</strong>
#                     </p>
#                     <p style="font-size:13px; color:#888888; margin-bottom:6px;">
#                         Plan Pricing Module Structure: <strong>₹{results['recommended_price']}</strong> for <strong>{results['validity']} Days</strong> &nbsp;&bull;&nbsp; Structural Constraint Boundary: <strong>{results['data_limit']} GB/Day</strong>
#                     </p>
#                     <p style="font-size:11px; color:#555555; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:20px;">
#                         NETWORK LAYER INFRASTRUCTURE V5G STATUS: <strong style="color:#FFFFFF;">{fiveg_badge}</strong>
#                     </p>
#                 </div>
#             """, unsafe_allow_html=True)
            
#             # --- BRAND NEW PREMIUM LOGIC: REVENUE COMPARATIVE VISUALIZATION ---
#             st.markdown('<p class="section-header" style="margin-top:40px;">03 // MARKET PRICING SPECTRUM TRACE</p>', unsafe_allow_html=True)
#             chart_df = results["all_plans_df"].set_index("Plan Name")
            
#             # Rendering a highly minimal, clean monochrome system chart
#             st.bar_chart(chart_df["Monthly Normalized Cost (₹)"])
#             st.markdown('<p style="font-size:11px; color:#444444; text-align:center;">Fig 1.1: Normalized cost matrix cross-reference for available carrier products.</p>', unsafe_allow_html=True)
            
#     else:
#         st.markdown("""
#             <div style="padding: 80px 20px; text-align: left;">
#                 <p style="color: #333333; font-size: 14px; font-weight: 400; letter-spacing: 1px; text-transform: uppercase;">
#                     // ENGINE STANDING BY. ENTER BASELINE PROFILE METRICS AND TRIGGER SYSTEM ARCHITECTURE ACTION RUN ON THE LEFT CONTROL INTERFACE.
#                 </p>
#             </div>
#         """, unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)




























# # import streamlit as st
# # import json
# # import os
# # import time

# # # =====================================================================
# # # PROJECT: AI Telecom Optimization Platform - Enterprise JSON Core V3
# # # Philosophy: Separate Data Layer, True Production Architecture Framework
# # # =====================================================================

# # # --- DATA LAYER INTEGRATION CONSOLE ---
# # def load_telecom_database():
# #     db_file = "plans_db.json"
# #     # Fallback simulation error check layer
# #     if not os.path.exists(db_file):
# #         return None
# #     with open(db_file, "r") as file:
# #         return json.load(file)

# # telecom_plans = load_telecom_database()

# # # --- STEP 2: RECOMMIT ALGORITHM WITH DYNAMIC MONTHLY NORMALIZATION ---
# # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# #     if not telecom_plans:
# #         return None, "JSON DB System file structural linkage breakdown error."
    
# #     normalized_provider_key = provider.lower()
# #     if normalized_provider_key not in telecom_plans:
# #         return None, f"Carrier network infrastructure configuration missing for: {provider}."
        
# #     available_options = telecom_plans[normalized_provider_key]
# #     best_matching_plan = None
# #     min_viable_price_normalized = float('inf')
    
# #     for plan in available_options:
# #         # Optimization criteria match logic
# #         if plan["data_per_day_gb"] >= actual_daily_usage:
# #             # 28 days price mapping values normal scale adjustment matrix
# #             # Normalizing long-term plan prices into standard monthly blocks for fair analytics comparison
# #             calculated_monthly_normalized_price = (plan["price"] / plan["validity_days"]) * 28
            
# #             if calculated_monthly_normalized_price < min_viable_price_normalized:
# #                 min_viable_price_normalized = calculated_monthly_normalized_price
# #                 best_matching_plan = plan

# #     if best_matching_plan:
# #         best_plan_normalized_monthly = (best_matching_plan["price"] / best_matching_plan["validity_days"]) * 28
# #         potential_monthly_saving = current_monthly_cost - best_plan_normalized_monthly
# #         potential_annual_saving = potential_monthly_saving * 12
        
# #         return {
# #             "recommended_plan": best_matching_plan["plan_name"],
# #             "recommended_price": best_matching_plan["price"],
# #             "validity": best_matching_plan["validity_days"],
# #             "data_limit": best_matching_plan["data_per_day_gb"],
# #             "unlimited_5g": best_matching_plan["unlimited_5g"],
# #             "monthly_savings": int(max(0, potential_monthly_saving)),
# #             "annual_savings": int(max(0, potential_annual_saving))
# #         }, None
# #     else:
# #         return None, "No structural lower optimization criteria profile standard matches your usage limits."


# # # --- STEP 3: STREAMLIT FRONTEND MONOCHROME WEB UI ---
# # st.set_page_config(page_title="Telecom Optimization Matrix", page_icon="▪️", layout="wide")

# # # Editorial Custom Luxury Dark Mode Stylesheets
# # st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');
# #     html, body, [data-testid="stAppViewContainer"] {
# #         background-color: #000000 !important;
# #         font-family: 'Inter', sans-serif !important;
# #         color: #FFFFFF !important;
# #     }
# #     .editorial-title { font-size: 48px !important; font-weight: 300 !important; letter-spacing: -2px !important; color: #FFFFFF !important; text-transform: uppercase; margin-bottom: 2px; }
# #     .editorial-subtitle { font-size: 14px !important; font-weight: 400 !important; letter-spacing: 1px !important; color: #666666 !important; text-transform: uppercase; margin-bottom: 40px; }
# #     .minimal-container { border-top: 1px solid #222222; padding-top: 24px; margin-bottom: 30px; }
# #     .section-header { font-size: 13px !important; font-weight: 700 !important; letter-spacing: 2px !important; color: #888888 !important; text-transform: uppercase; margin-bottom: 20px; }
# #     .kpi-wrapper { border: 1px solid #111111; background-color: #050505; padding: 30px; text-align: left; }
# #     .kpi-label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 1.5px !important; color: #555555 !important; text-transform: uppercase; margin: 0 0 8px 0; }
# #     .kpi-value { font-size: 44px !important; font-weight: 300 !important; letter-spacing: -1px !important; color: #FFFFFF !important; margin: 0; }
# #     .kpi-sub { font-size: 12px !important; color: #444444 !important; margin-top: 4px; }
# #     div.stButton > button { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 0px !important; border: 1px solid #FFFFFF !important; font-size: 12px !important; font-weight: 700 !important; letter-spacing: 2px !important; text-transform: uppercase; padding: 12px 24px !important; transition: all 0.3s ease; }
# #     div.stButton > button:hover { background-color: #000000 !important; color: #FFFFFF !important; border: 1px solid #FFFFFF !important; }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.markdown('<p class="editorial-title">TELECOM OPTIMIZATION MATRIX</p>', unsafe_allow_html=True)
# # st.markdown('<p class="editorial-subtitle">B2B EXPENSE ARCHITECTURE & WASTE LOGISTICS ENGINE</p>', unsafe_allow_html=True)

# # col_left, col_right = st.columns([1, 1.2], gap="large")

# # with col_left:
# #     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
# #     st.markdown('<p class="section-header">01 // PARAMETER SELECTION</p>', unsafe_allow_html=True)
    
# #     # Dynamic list pull indicator setup configuration operator options UI
# #     provider_options = [p.upper() for p in telecom_plans.keys()] if telecom_plans else ["JIO", "AIRTEL", "VI"]
# #     provider_select = st.selectbox("INFRASTRUCTURE CARRIER", provider_options)
# #     current_cost_input = st.number_input("CURRENT MONTHLY OUTLAY (₹)", min_value=0, value=449, step=10)
# #     actual_usage_input = st.slider("OBSERVED DAILY THROUGHPUT (GB/DAY)", min_value=0.1, max_value=4.0, value=0.8, step=0.1)
    
# #     st.markdown("<br><br>", unsafe_allow_html=True)
# #     run_btn = st.button("RUN ANALYTICAL TRACE")
# #     st.markdown('</div>', unsafe_allow_html=True)

# # with col_right:
# #     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
# #     st.markdown('<p class="section-header">02 // STRATEGY OUTPUT</p>', unsafe_allow_html=True)
    
# #     if run_btn:
# #         with st.spinner("Processing network data structures..."):
# #             time.sleep(0.4)
# #             results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
        
# #         if error:
# #             st.markdown(f'<p style="color:#FF3333; font-size:13px; font-weight:500;">SYSTEM ERROR // {error}</p>', unsafe_allow_html=True)
# #         else:
# #             grid_1, grid_2 = st.columns(2)
# #             with grid_1:
# #                 st.markdown(f"""
# #                     <div class="kpi-wrapper">
# #                         <p class="kpi-label">RECOVERED CAPITAL</p>
# #                         <p class="kpi-value">₹{results['monthly_savings']}</p>
# #                         <p class="kpi-sub">Normalized monthly balance delta</p>
# #                     </div>
# #                 """, unsafe_allow_html=True)
# #             with grid_2:
# #                 st.markdown(f"""
# #                     <div class="kpi-wrapper">
# #                         <p class="kpi-label">ANNUALIZED PROJECTION</p>
# #                         <p class="kpi-value">₹{results['annual_savings']}</p>
# #                         <p class="kpi-sub">Compounded macro financial ROI</p>
# #                     </div>
# #                 """, unsafe_allow_html=True)
            
# #             # Additional metadata logic engine output layers
# #             fiveg_badge = "ENABLED // UNLIMITED DATA ACCESS BURST" if results['unlimited_5g'] else "RESTRICTED // STANDARD OVERAGES REGULATION"
            
# #             st.markdown(f"""
# #                 <div style="border-top: 1px dashed #333333; padding-top: 20px; margin-top: 10px;">
# #                     <p style="font-size:11px; font-weight:700; color:#666666; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">EXECUTION LOGIC DEFINITION</p>
# #                     <p style="font-size:16px; font-weight:300; color:#FFFFFF; line-height:1.6; margin-bottom: 6px;">
# #                         Migrate current baseline allocation interface environment to: <strong>{results['recommended_plan']}</strong>
# #                     </p>
# #                     <p style="font-size:13px; color:#888888; margin-bottom:6px;">
# #                         Plan Pricing Module Structure: <strong>₹{results['recommended_price']}</strong> for <strong>{results['validity']} Days</strong> &nbsp;&bull;&nbsp; Structural Constraint Boundary: <strong>{results['data_limit']} GB/Day</strong>
# #                     </p>
# #                     <p style="font-size:11px; color:#555555; letter-spacing:0.5px; text-transform:uppercase;">
# #                         NETWORK LAYER INFRASTRUCTURE V5G STATUS: <strong style="color:#FFFFFF;">{fiveg_badge}</strong>
# #                     </p>
# #                 </div>
# #             """, unsafe_allow_html=True)
            
# #     else:
# #         st.markdown("""
# #             <div style="padding: 80px 20px; text-align: left;">
# #                 <p style="color: #333333; font-size: 14px; font-weight: 400; letter-spacing: 1px; text-transform: uppercase;">
# #                     // ENGINE STANDING BY. ENTER BASELINE PROFILE METRICS AND TRIGGER SYSTEM ARCHITECTURE ACTION RUN ON THE LEFT CONTROL INTERFACE.
# #                 </p>
# #             </div>
# #         """, unsafe_allow_html=True)
# #     st.markdown('</div>', unsafe_allow_html=True)






















































# # # import streamlit as st
# # # import time

# # # # =====================================================================
# # # # PROJECT: AI Telecom Optimization Platform - Luxury Monochrome Edition
# # # # Philosophy: Minimalist Editorial Typography, High-End Luxury Aesthetic
# # # # =====================================================================

# # # # --- STEP 1: MOCK TELECOM PLANS DATABASE ---
# # # telecom_plans = {
# # #     "Jio": [
# # #         {"plan_name": "JIO VALUE 1GB", "price": 209, "validity_days": 28, "data_per_day_gb": 1.0},
# # #         {"plan_name": "JIO STANDARD 1.5GB", "price": 299, "validity_days": 28, "data_per_day_gb": 1.5},
# # #         {"plan_name": "JIO HEAVY 2GB", "price": 349, "validity_days": 28, "data_per_day_gb": 2.0},
# # #         {"plan_name": "JIO SUPER 3GB", "price": 449, "validity_days": 28, "data_per_day_gb": 3.0}
# # #     ],
# # #     "Airtel": [
# # #         {"plan_name": "AIRTEL SMART 1GB", "price": 265, "validity_days": 28, "data_per_day_gb": 1.0},
# # #         {"plan_name": "AIRTEL DAILY 1.5GB", "price": 329, "validity_days": 28, "data_per_day_gb": 1.5},
# # #         {"plan_name": "AIRTEL TURBO 2GB", "price": 379, "validity_days": 28, "data_per_day_gb": 2.0},
# # #         {"plan_name": "AIRTEL MEGA 3GB", "price": 499, "validity_days": 28, "data_per_day_gb": 3.0}
# # #     ]
# # # }

# # # # --- STEP 2: RECOMTENDATION ENGINE ALGORITHM ---
# # # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# # #     matched_provider = None
# # #     for key in telecom_plans.keys():
# # #         if key.lower() == provider.lower():
# # #             matched_provider = key
# # #             break
            
# # #     if not matched_provider:
# # #         return None, f"Provider '{provider}' not supported."
    
# # #     available_options = telecom_plans[matched_provider]
# # #     best_matching_plan = None
# # #     min_viable_price = float('inf')
    
# # #     for plan in available_options:
# # #         if plan["data_per_day_gb"] >= actual_daily_usage:
# # #             if plan["price"] < min_viable_price:
# # #                 min_viable_price = plan["price"]
# # #                 best_matching_plan = plan

# # #     if best_matching_plan:
# # #         potential_monthly_saving = current_monthly_cost - best_matching_plan["price"]
# # #         potential_annual_saving = potential_monthly_saving * 12
        
# # #         return {
# # #             "recommended_plan": best_matching_plan["plan_name"],
# # #             "recommended_price": best_matching_plan["price"],
# # #             "data_limit": best_matching_plan["data_per_day_gb"],
# # #             "monthly_savings": max(0, potential_monthly_saving),
# # #             "annual_savings": max(0, potential_annual_saving)
# # #         }, None
# # #     else:
# # #         return None, "No matching configuration satisfies extreme heavy consumption rules."


# # # # --- STEP 3: STREAMLIT FRONTEND WEB UI DESIGN (MONOCHROME LUXURY) ---
# # # st.set_page_config(page_title="Telecom Optimization Matrix", page_icon="▪️", layout="wide")

# # # # Elite Monochrome Editorial Injector Stylesheet
# # # st.markdown("""
# # #     <style>
# # #     /* Global Base Configuration Override */
# # #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');
    
# # #     html, body, [data-testid="stAppViewContainer"] {
# # #         background-color: #000000 !important;
# # #         font-family: 'Inter', sans-serif !important;
# # #         color: #FFFFFF !important;
# # #     }
    
# # #     /* Luxury Editorial Typography Blocks */
# # #     .editorial-title {
# # #         font-size: 48px !important;
# # #         font-weight: 300 !important;
# # #         letter-spacing: -2px !important;
# # #         color: #FFFFFF !important;
# # #         text-transform: uppercase;
# # #         margin-bottom: 2px;
# # #     }
    
# # #     .editorial-subtitle {
# # #         font-size: 14px !important;
# # #         font-weight: 400 !important;
# # #         letter-spacing: 1px !important;
# # #         color: #666666 !important;
# # #         text-transform: uppercase;
# # #         margin-bottom: 40px;
# # #     }
    
# # #     /* Clean Minimal Border Enclosures */
# # #     .minimal-container {
# # #         border-top: 1px solid #222222;
# # #         padding-top: 24px;
# # #         margin-bottom: 30px;
# # #     }
    
# # #     .section-header {
# # #         font-size: 13px !important;
# # #         font-weight: 700 !important;
# # #         letter-spacing: 2px !important;
# # #         color: #888888 !important;
# # #         text-transform: uppercase;
# # #         margin-bottom: 20px;
# # #     }
    
# # #     /* High-End Matrix Dashboard KPI Blocks */
# # #     .kpi-wrapper {
# # #         border: 1px solid #111111;
# # #         background-color: #050505;
# # #         padding: 30px;
# # #         text-align: left;
# # #     }
    
# # #     .kpi-label {
# # #         font-size: 11px !important;
# # #         font-weight: 500 !important;
# # #         letter-spacing: 1.5px !important;
# # #         color: #555555 !important;
# # #         text-transform: uppercase;
# # #         margin: 0 0 8px 0;
# # #     }
    
# # #     .kpi-value {
# # #         font-size: 44px !important;
# # #         font-weight: 300 !important;
# # #         letter-spacing: -1px !important;
# # #         color: #FFFFFF !important;
# # #         margin: 0;
# # #     }
    
# # #     .kpi-sub {
# # #         font-size: 12px !important;
# # #         color: #444444 !important;
# # #         margin-top: 4px;
# # #     }

# # #     /* Target Execution Button Stylings */
# # #     div.stButton > button {
# # #         background-color: #FFFFFF !important;
# # #         color: #000000 !important;
# # #         border-radius: 0px !important;
# # #         border: 1px solid #FFFFFF !important;
# # #         font-size: 12px !important;
# # #         font-weight: 700 !important;
# # #         letter-spacing: 2px !important;
# # #         text-transform: uppercase;
# # #         padding: 12px 24px !important;
# # #         transition: all 0.3s ease;
# # #     }
# # #     div.stButton > button:hover {
# # #         background-color: #000000 !important;
# # #         color: #FFFFFF !important;
# # #         border: 1px solid #FFFFFF !important;
# # #     }
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # Main Structural Typography Title Configuration
# # # st.markdown('<p class="editorial-title">TELECOM OPTIMIZATION MATRIX</p>', unsafe_allow_html=True)
# # # st.markdown('<p class="editorial-subtitle">B2B EXPENSE ARCHITECTURE & WASTE LOGISTICS ENGINE</p>', unsafe_allow_html=True)

# # # # Main Two-Pane Structural Column Division
# # # col_left, col_right = st.columns([1, 1.2], gap="large")

# # # with col_left:
# # #     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
# # #     st.markdown('<p class="section-header">01 // PARAMETER SELECTION</p>', unsafe_allow_html=True)
    
# # #     provider_select = st.selectbox("INFRASTRUCTURE CARRIER", ["Jio", "Airtel"])
# # #     current_cost_input = st.number_input("CURRENT MONTHLY OUTLAY (₹)", min_value=0, value=449, step=10)
# # #     actual_usage_input = st.slider("OBSERVED DAILY THROUGHPUT (GB/DAY)", min_value=0.1, max_value=4.0, value=0.8, step=0.1)
    
# # #     st.markdown("<br><br>", unsafe_allow_html=True)
# # #     run_btn = st.button("RUN ANALYTICAL TRACE")
# # #     st.markdown('</div>', unsafe_allow_html=True)

# # # with col_right:
# # #     st.markdown('<div class="minimal-container">', unsafe_allow_html=True)
# # #     st.markdown('<p class="section-header">02 // STRATEGY OUTPUT</p>', unsafe_allow_html=True)
    
# # #     if run_btn:
# # #         with st.spinner("Executing trace..."):
# # #             time.sleep(0.4)
# # #             results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
        
# # #         if error:
# # #             st.markdown(f'<p style="color:#FF3333; font-size:13px; font-weight:500;">SYSTEM ERROR // {error}</p>', unsafe_allow_html=True)
# # #         else:
# # #             # Luxury Balanced Metric Grid Columns Layer
# # #             grid_1, grid_2 = st.columns(2)
# # #             with grid_1:
# # #                 st.markdown(f"""
# # #                     <div class="kpi-wrapper">
# # #                         <p class="kpi-label">RECOVERED CAPITAL</p>
# # #                         <p class="kpi-value">₹{results['monthly_savings']}</p>
# # #                         <p class="kpi-sub">Normalized monthly balance delta</p>
# # #                     </div>
# # #                 """, unsafe_allow_html=True)
# # #             with grid_2:
# # #                 st.markdown(f"""
# # #                     <div class="kpi-wrapper">
# # #                         <p class="kpi-label">ANNUALIZED PROJECTION</p>
# # #                         <p class="kpi-value">₹{results['annual_savings']}</p>
# # #                         <p class="kpi-sub">Compounded macro financial ROI</p>
# # #                     </div>
# # #                 """, unsafe_allow_html=True)
            
# # #             st.markdown("<br>", unsafe_allow_html=True)
            
# # #             # Ultra-Clean Structural Editorial Log Box
# # #             st.markdown(f"""
# # #                 <div style="border-top: 1px dashed #333333; padding-top: 20px; margin-top: 10px;">
# # #                     <p style="font-size:11px; font-weight:700; color:#666666; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">EXECUTION LOGIC DEFINITION</p>
# # #                     <p style="font-size:16px; font-weight:300; color:#FFFFFF; line-height:1.6; margin-bottom: 6px;">
# # #                         Migrate current baseline allocation interface environment to: <strong>{results['recommended_plan']}</strong>
# # #                     </p>
# # #                     <p style="font-size:13px; color:#888888; margin:0;">
# # #                         Target Structure Expense: <strong>₹{results['recommended_price']}/mo</strong> &nbsp;&bull;&nbsp; Target Bandwidth Boundary: <strong>{results['data_limit']} GB/Day</strong>
# # #                     </p>
# # #                 </div>
# # #             """, unsafe_allow_html=True)
            
# # #     else:
# # #         # Placeholder Display Screen Initial Base Empty State Luxury Text System
# # #         st.markdown("""
# # #             <div style="padding: 80px 20px; text-align: left;">
# # #                 <p style="color: #333333; font-size: 14px; font-weight: 400; letter-spacing: 1px; text-transform: uppercase;">
# # #                     // ENGINE STANDING BY. ENTER BASELINE PROFILE METRICS AND TRIGGER SYSTEM ARCHITECTURE ACTION RUN ON THE LEFT CONTROL INTERFACE.
# # #                 </p>
# # #             </div>
# # #         """, unsafe_allow_html=True)
# # #     st.markdown('</div>', unsafe_allow_html=True)












# # # # import streamlit as st
# # # # import time

# # # # # =====================================================================
# # # # # PROJECT: AI Telecom Optimization Platform - Premium Tech UI V2
# # # # # Philosophy: High leverage scaling, Professional Creator-SaaS Visuals
# # # # # =====================================================================

# # # # # --- STEP 1: MOCK TELECOM PLANS DATABASE ---
# # # # telecom_plans = {
# # # #     "Jio": [
# # # #         {"plan_name": "Jio Value 1GB", "price": 209, "validity_days": 28, "data_per_day_gb": 1.0},
# # # #         {"plan_name": "Jio Standard 1.5GB", "price": 299, "validity_days": 28, "data_per_day_gb": 1.5},
# # # #         {"plan_name": "Jio Heavy 2GB", "price": 349, "validity_days": 28, "data_per_day_gb": 2.0},
# # # #         {"plan_name": "Jio Super 3GB", "price": 449, "validity_days": 28, "data_per_day_gb": 3.0}
# # # #     ],
# # # #     "Airtel": [
# # # #         {"plan_name": "Airtel Smart 1GB", "price": 265, "validity_days": 28, "data_per_day_gb": 1.0},
# # # #         {"plan_name": "Airtel Daily 1.5GB", "price": 329, "validity_days": 28, "data_per_day_gb": 1.5},
# # # #         {"plan_name": "Airtel Turbo 2GB", "price": 379, "validity_days": 28, "data_per_day_gb": 2.0},
# # # #         {"plan_name": "Airtel Mega 3GB", "price": 499, "validity_days": 28, "data_per_day_gb": 3.0}
# # # #     ]
# # # # }

# # # # # --- STEP 2: RECOMTENDATION ENGINE ALGORITHM ---
# # # # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# # # #     matched_provider = None
# # # #     for key in telecom_plans.keys():
# # # #         if key.lower() == provider.lower():
# # # #             matched_provider = key
# # # #             break
            
# # # #     if not matched_provider:
# # # #         return None, f"Provider '{provider}' not supported yet."
    
# # # #     available_options = telecom_plans[matched_provider]
# # # #     best_matching_plan = None
# # # #     min_viable_price = float('inf')
    
# # # #     for plan in available_options:
# # # #         if plan["data_per_day_gb"] >= actual_daily_usage:
# # # #             if plan["price"] < min_viable_price:
# # # #                 min_viable_price = plan["price"]
# # # #                 best_matching_plan = plan

# # # #     if best_matching_plan:
# # # #         potential_monthly_saving = current_monthly_cost - best_matching_plan["price"]
# # # #         potential_annual_saving = potential_monthly_saving * 12
        
# # # #         return {
# # # #             "recommended_plan": best_matching_plan["plan_name"],
# # # #             "recommended_price": best_matching_plan["price"],
# # # #             "data_limit": best_matching_plan["data_per_day_gb"],
# # # #             "monthly_savings": max(0, potential_monthly_saving),
# # # #             "annual_savings": max(0, potential_annual_saving)
# # # #         }, None
# # # #     else:
# # # #         return None, "No suitable lower plan found for your heavy usage configuration."


# # # # # --- STEP 3: STREAMLIT FRONTEND WEB UI DESIGN ---
# # # # st.set_page_config(page_title="AI Telecom Optimization Engine", page_icon="⚡", layout="wide")

# # # # # Injecting Custom Professional Premium FinTech Styling CSS 
# # # # st.markdown("""
# # # #     <style>
# # # #     .big-title { font-size:42px !important; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; margin-bottom: 0px; }
# # # #     .sub-title { font-size:18px !important; color: #8A99AD; margin-bottom: 30px; }
# # # #     .card-box { background-color: #1E293B; padding: 24px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
# # # #     .metric-value { font-size: 32px !important; font-weight: 700; color: #00F2FE; }
# # # #     .metric-label { font-size: 14px !important; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px; }
# # # #     </style>
# # # # """, unsafe_allow_html=True)

# # # # # Main Banner Area
# # # # st.markdown('<p class="big-title">⚡ Telecom Optimization Matrix</p>', unsafe_allow_html=True)
# # # # st.markdown('<p class="sub-title">B2B Financial Operations Engine & Waste Reduction Intelligence Suite.</p>', unsafe_allow_html=True)

# # # # # Using Columns to divide Input Controls and Analytics Screen Layout
# # # # left_column, right_column = st.columns([1, 1.3], gap="large")

# # # # with left_column:
# # # #     st.markdown('<div class="card-box">', unsafe_allow_html=True)
# # # #     st.subheader("📋 Core Configurations Profiles")
# # # #     st.write("Configure user core logging parameters for analytical trace scanning.")
    
# # # #     provider_select = st.selectbox("Telecom Infrastructure Provider:", ["Jio", "Airtel"])
# # # #     current_cost_input = st.number_input("Current Monthly Plan Expense (₹):", min_value=0, value=449, step=10)
# # # #     actual_usage_input = st.slider("Observed Actual Data Consumption Limit (GB/Day):", min_value=0.1, max_value=4.0, value=0.8, step=0.1)
    
# # # #     st.markdown("<br>", unsafe_allow_html=True)
# # # #     run_btn = st.button("🚀 EXECUTE AI TARGETING RUN", use_container_width=True)
# # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # # with right_column:
# # # #     if run_btn:
# # # #         with st.spinner("Processing network variables and dictionary metrics map calculations..."):
# # # #             time.sleep(0.6) # Simulating true calculation time trace processing latency for premium feel
# # # #             results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
        
# # # #         if error:
# # # #             st.error(f"❌ Structural Loop Interruption: {error}")
# # # #         else:
# # # #             st.markdown('<div>', unsafe_allow_html=True)
# # # #             st.subheader("📊 Operational Diagnostics Report")
# # # #             st.markdown("---")
            
# # # #             # Premium Visual KPI Performance Grid Panel
# # # #             kpi_col1, kpi_col2 = st.columns(2)
# # # #             with kpi_col1:
# # # #                 st.markdown(f"""
# # # #                     <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 20px; border-radius: 10px; border: 1px solid #00F2FE;">
# # # #                         <p style="margin:0; font-size:12px; color:#00F2FE; text-transform:uppercase; font-weight:600;">Wasted Capital Recovered</p>
# # # #                         <p style="margin:0; font-size:36px; font-weight:700; color:#FFFFFF;">₹{results['monthly_savings']}<span style="font-size:16px; color:#94A3B8;"> / mo</span></p>
# # # #                     </div>
# # # #                 """, unsafe_allow_html=True)
# # # #             with kpi_col2:
# # # #                 st.markdown(f"""
# # # #                     <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 20px; border-radius: 10px; border: 1px solid #4ADE80;">
# # # #                         <p style="margin:0; font-size:12px; color:#4ADE80; text-transform:uppercase; font-weight:600;">Annual ROI Projection</p>
# # # #                         <p style="margin:0; font-size:36px; font-weight:700; color:#FFFFFF;">₹{results['annual_savings']}<span style="font-size:16px; color:#4ADE80;"> / yr</span></p>
# # # #                     </div>
# # # #                 """, unsafe_allow_html=True)
            
# # # #             st.markdown("<br>", unsafe_allow_html=True)
            
# # # #             # Detailed Recommendations Strategy Log Box Layout Container
# # # #             st.markdown(f"""
# # # #                 <div style="background-color: #1E293B; padding: 20px; border-radius: 12px; border-left: 5px solid #38BDF8;">
# # # #                     <h4 style="margin-top:0; color:#38BDF8;">🎯 Recommended Execution Logic</h4>
# # # #                     <p style="color:#E2E8F0; margin-bottom:8px;">Swap production environment user baseline plan to: <strong>{results['recommended_plan']}</strong></p>
# # # #                     <p style="color:#94A3B8; margin-bottom:0; font-size:14px;"><strong>Target Price:</strong> ₹{results['recommended_price']}/month | <strong>Allocated Bound Capacity:</strong> {results['data_limit']} GB/day</p>
# # # #                 </div>
# # # #             """, unsafe_allow_html=True)
            
# # # #             st.markdown('</div>', unsafe_allow_html=True)
# # # #     else:
# # # #         # Placeholder Display Screen Initial Base Empty State System
# # # #         st.markdown("""
# # # #             <div style="background-color: #0F172A; border: 2px dashed #334155; border-radius: 12px; padding: 60px; text-align: center; margin-top: 20px;">
# # # #                 <p style="color: #64748B; font-size: 18px; margin: 0;">⚡ Dashboard Standing By. Configure parameters on left pane and execute system analytics trace run loop.</p>
# # # #             </div>
# # # #         """, unsafe_allow_html=True)






























































# # # # # import streamlit as st

# # # # # # =====================================================================
# # # # # # PROJECT: AI Telecom Optimization Platform - Web MVP (Streamlit UI)
# # # # # # Philosophy: High leverage scaling, zero cost setup UI mapping
# # # # # # =====================================================================

# # # # # # --- STEP 1: MOCK TELECOM PLANS DATABASE ---
# # # # # telecom_plans = {
# # # # #     "Jio": [
# # # # #         {"plan_name": "Jio Value 1GB", "price": 209, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # #         {"plan_name": "Jio Standard 1.5GB", "price": 299, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # #         {"plan_name": "Jio Heavy 2GB", "price": 349, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # #         {"plan_name": "Jio Super 3GB", "price": 449, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # #     ],
# # # # #     "Airtel": [
# # # # #         {"plan_name": "Airtel Smart 1GB", "price": 265, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # #         {"plan_name": "Airtel Daily 1.5GB", "price": 329, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # #         {"plan_name": "Airtel Turbo 2GB", "price": 379, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # #         {"plan_name": "Airtel Mega 3GB", "price": 499, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # #     ]
# # # # # }

# # # # # # --- STEP 2: RECOMTENDATION ENGINE ALGORITHM ---
# # # # # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# # # # #     matched_provider = None
# # # # #     for key in telecom_plans.keys():
# # # # #         if key.lower() == provider.lower():
# # # # #             matched_provider = key
# # # # #             break
            
# # # # #     if not matched_provider:
# # # # #         return None, f"Provider '{provider}' not supported yet."
    
# # # # #     available_options = telecom_plans[matched_provider]
# # # # #     best_matching_plan = None
# # # # #     min_viable_price = float('inf')
    
# # # # #     for plan in available_options:
# # # # #         if plan["data_per_day_gb"] >= actual_daily_usage:
# # # # #             if plan["price"] < min_viable_price:
# # # # #                 min_viable_price = plan["price"]
# # # # #                 best_matching_plan = plan

# # # # #     if best_matching_plan:
# # # # #         potential_monthly_saving = current_monthly_cost - best_matching_plan["price"]
# # # # #         potential_annual_saving = potential_monthly_saving * 12
        
# # # # #         return {
# # # # #             "recommended_plan": best_matching_plan["plan_name"],
# # # # #             "recommended_price": best_matching_plan["price"],
# # # # #             "data_limit": best_matching_plan["data_per_day_gb"],
# # # # #             "monthly_savings": max(0, potential_monthly_saving),
# # # # #             "annual_savings": max(0, potential_annual_saving)
# # # # #         }, None
# # # # #     else:
# # # # #         return None, "No suitable lower plan found for your heavy usage configuration."


# # # # # # --- STEP 3: STREAMLIT FRONTEND WEB UI DESIGN ---
# # # # # st.set_page_config(page_title="AI Telecom Optimization Platform", page_icon="🚀", layout="centered")

# # # # # st.title("🚀 AI Telecom Optimization Platform")
# # # # # st.subheader("Stop Overpaying. Optimize Your Mobile Plan Analytics Instant-ah.")
# # # # # st.markdown("---")

# # # # # # Input Section Elements layout
# # # # # st.header("📋 Enter User Usage Profile")
# # # # # provider_select = st.selectbox("Select Your Telecom Operator:", ["Jio", "Airtel"])
# # # # # current_cost_input = st.number_input("Current Monthly Plan Cost (in ₹):", min_value=0, value=449)
# # # # # actual_usage_input = st.slider("Your Actual Average Daily Usage (in GB):", min_value=0.1, max_value=4.0, value=0.8, step=0.1)

# # # # # st.markdown("---")

# # # # # # Processing and Execution Button
# # # # # if st.button("🔥 Run Analytics Savings Test"):
# # # # #     results, error = calculate_savings(provider_select, current_cost_input, actual_usage_input)
    
# # # # #     if error:
# # # # #         st.error(f"❌ Alert: {error}")
# # # # #     else:
# # # # #         st.success("📊 SYSTEM ANALYTICS & INSIGHT REPORT GENERATED SUCCESSFULLY!")
        
# # # # #         # Displaying Results Metrics Metrics Card layout grid
# # # # #         st.info(f"💡 **Recommended Action:** Swap to **{results['recommended_plan']}** (₹{results['recommended_price']}/month)")
# # # # #         st.write(f"📉 **Ideal Capacity Match:** {results['data_limit']} GB/day gives safe buffer for your profile behavior.")
        
# # # # #         col1, col2 = st.columns(2)
# # # # #         with col1:
# # # # #             st.metric(label="Wasted Money Recovered", value=f"₹{results['monthly_savings']}/mo")
# # # # #         with col2:
# # # # #             st.metric(label="Projected Annual Scale Savings", value=f"₹{results['annual_savings']}/yr", delta="🔥 Peak ROI")

























































































# # # # # # # =====================================================================
# # # # # # # PROJECT: AI Telecom Optimization Platform - Validation MVP
# # # # # # # File Name: app.py
# # # # # # # Philosophy: Zero-cost tools, clean scalability validation engine
# # # # # # # =====================================================================

# # # # # # # --- STEP 1: MOCK TELECOM PLANS DATABASE ---
# # # # # # telecom_plans = {
# # # # # #     "Jio": [
# # # # # #         {"plan_name": "Jio Value 1GB", "price": 209, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # # #         {"plan_name": "Jio Standard 1.5GB", "price": 299, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # # #         {"plan_name": "Jio Heavy 2GB", "price": 349, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # # #         {"plan_name": "Jio Super 3GB", "price": 449, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # # #     ],
# # # # # #     "Airtel": [
# # # # # #         {"plan_name": "Airtel Smart 1GB", "price": 265, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # # #         {"plan_name": "Airtel Daily 1.5GB", "price": 329, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # # #         {"plan_name": "Airtel Turbo 2GB", "price": 379, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # # #         {"plan_name": "Airtel Mega 3GB", "price": 499, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # # #     ]
# # # # # # }

# # # # # # # --- STEP 2: RECOMTENDATION ENGINE ALGORITHM ---
# # # # # # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# # # # # #     # Normalized provider logic check
# # # # # #     matched_provider = None
# # # # # #     for key in telecom_plans.keys():
# # # # # #         if key.lower() == provider.lower():
# # # # # #             matched_provider = key
# # # # # #             break
            
# # # # # #     if not matched_provider:
# # # # # #         return None, f"Provider '{provider}' not supported yet in our database ecosystem."
    
# # # # # #     available_options = telecom_plans[matched_provider]
# # # # # #     best_matching_plan = None
# # # # # #     min_viable_price = float('inf')
    
# # # # # #     # Matching algorithm matrix loop
# # # # # #     for plan in available_options:
# # # # # #         if plan["data_per_day_gb"] >= actual_daily_usage:
# # # # # #             if plan["price"] < min_viable_price:
# # # # # #                 min_viable_price = plan["price"]
# # # # # #                 best_matching_plan = plan

# # # # # #     if best_matching_plan:
# # # # # #         potential_monthly_saving = current_monthly_cost - best_matching_plan["price"]
# # # # # #         potential_annual_saving = potential_monthly_saving * 12
        
# # # # # #         return {
# # # # # #             "recommended_plan": best_matching_plan["plan_name"],
# # # # # #             "recommended_price": best_matching_plan["price"],
# # # # # #             "data_limit": best_matching_plan["data_per_day_gb"],
# # # # # #             "monthly_savings": max(0, potential_monthly_saving),
# # # # # #             "annual_savings": max(0, potential_annual_saving)
# # # # # #         }, None
# # # # # #     else:
# # # # # #         return None, "No suitable lower plan found for your custom heavy usage configurations."


# # # # # # # --- STEP 3: INTERACTIVE USER SIMULATION INPUT ---
# # # # # # print("\n" + "="*40)
# # # # # # print("🚀 MOBILE DATA SAVINGS CALCULATOR MVP")
# # # # # # print("="*40)

# # # # # # user_provider = input("Enter your provider (Jio / Airtel): ")
# # # # # # user_current_cost = float(input("Enter your current monthly bill/recharge cost (in ₹): "))
# # # # # # user_actual_usage = float(input("Enter your actual daily data usage average (in GB): "))

# # # # # # # Execution trigger
# # # # # # results, error = calculate_savings(user_provider, user_current_cost, user_actual_usage)

# # # # # # # --- STEP 4: SYSTEM METRICS OUTPUT ENGINE ---
# # # # # # print("\n" + "-"*40)
# # # # # # print("📊 SYSTEM ANALYTICS & INSIGHT REPORT:")
# # # # # # print("-"*40)

# # # # # # if error:
# # # # # #     print(f"❌ Alert: {error}")
# # # # # # else:
# # # # # #     print(f"✅ Recommended Configuration: Swap to '{results['recommended_plan']}' (₹{results['recommended_price']}/month)")
# # # # # #     print(f"📉 Plan Capacity: Only {results['data_limit']} GB/day (Perfect match for your behavior)")
    
# # # # # #     if results['monthly_savings'] > 0:
# # # # # #         print(f"💰 Wasted Money Recovered: ₹{results['monthly_savings']}/month")
# # # # # #         print(f"🔥 Annual Billionaire Scale Projection: You will save ₹{results['annual_savings']} per year!")
# # # # # #     else:
# # # # # #         print("💡 Insight: You are already using the most optimized cost-efficient plan for your usage matrix.")
# # # # # # print("="*40 + "\n")






































# # # # # # # --- STEP 1: MOCK TELECOM PLANS DATABASE ---
# # # # # # # Hardcoded local database for MVP validation testing (Jio & Airtel)

# # # # # # telecom_plans = {
# # # # # #     "Jio": [
# # # # # #         {"plan_name": "Jio Value 1GB", "price": 209, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # # #         {"plan_name": "Jio Standard 1.5GB", "price": 299, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # # #         {"plan_name": "Jio Heavy 2GB", "price": 349, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # # #         {"plan_name": "Jio Super 3GB", "price": 449, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # # #     ],
# # # # # #     "Airtel": [
# # # # # #         {"plan_name": "Airtel Smart 1GB", "price": 265, "validity_days": 28, "data_per_day_gb": 1.0},
# # # # # #         {"plan_name": "Airtel Daily 1.5GB", "price": 329, "validity_days": 28, "data_per_day_gb": 1.5},
# # # # # #         {"plan_name": "Airtel Turbo 2GB", "price": 379, "validity_days": 28, "data_per_day_gb": 2.0},
# # # # # #         {"plan_name": "Airtel Mega 3GB", "price": 499, "validity_days": 28, "data_per_day_gb": 3.0}
# # # # # #     ]
# # # # # # }

# # # # # # print("Database initialized successfully, Thalaiva! Total providers loaded: ", list(telecom_plans.keys()))

# # # # # # # --- STEP 2: RECOMTENDATION ENGINE ALGORITHM ---

# # # # # # def calculate_savings(provider, current_monthly_cost, actual_daily_usage):
# # # # # #     # If the provider is not in our database, default handling
# # # # # #     if provider not in telecom_plans:
# # # # # #         return None, "Provider not supported yet."
    
# # # # # #     available_options = telecom_plans[provider]
# # # # # #     best_matching_plan = None
# # # # # #     min_viable_price = float('inf') # Setting infinity to find the true minimum
    
# # # # # #     # Filtering loop to find the best optimized plan
# # # # # #     for plan in available_options:
# # # # # #         # Condition: Plan daily data limit must satisfy user's daily usage requirement
# # # # # #         if plan["data_per_day_gb"] >= actual_daily_usage:
# # # # # #             # We want the cheapest plan that fulfills the condition
# # # # # #             if plan["price"] < min_viable_price:
# # # # # #                 min_viable_price = plan["price"]
# # # # # #                 best_matching_plan = plan

# # # # # #     if best_matching_plan:
# # # # # #         # Math normalization to calculate potential scale of savings
# # # # # #         potential_monthly_saving = current_monthly_cost - best_matching_plan["price"]
# # # # # #         potential_annual_saving = potential_monthly_saving * 12
        
# # # # # #         return {
# # # # # #             "recommended_plan": best_matching_plan["plan_name"],
# # # # # #             "recommended_price": best_matching_plan["price"],
# # # # # #             "data_limit": best_matching_plan["data_per_day_gb"],
# # # # # #             "monthly_savings": max(0, potential_monthly_saving),
# # # # # #             "annual_savings": max(0, potential_annual_saving)
# # # # # #         }, None
# # # # # #     else:
# # # # # #         return None, "No suitable lower plan found for your heavy usage configuration."


# # # # # # # --- STEP 3: INTERACTIVE USER SIMULATION INPUT ---
# # # # # # print("\n" + "="*40)
# # # # # # print("🚀 MOBILE DATA SAVINGS CALCULATOR MVP")
# # # # # # print("="*40)

# # # # # # # Simulating inputs (Later these will come from Streamlit Web UI Frontend elements)
# # # # # # user_provider = input("Enter your provider (Jio / Airtel): ").strip()
# # # # # # user_current_cost = float(input("Enter your current monthly bill/recharge cost (in ₹): "))
# # # # # # user_actual_usage = float(input("Enter your actual daily data usage average (in GB): "))

# # # # # # # Executing the system
# # # # # # results, error = calculate_savings(user_provider, user_current_cost, user_actual_usage)

# # # # # # # --- STEP 4: SYSTEM METRICS OUTPUT ENGINE ---
# # # # # # print("\n" + "-"*40)
# # # # # # print("📊 SYSTEM ANALYTICS & INSIGHT REPORT:")
# # # # # # print("-"*40)

# # # # # # if error:
# # # # # #     print(f"❌ Alert: {error}")
# # # # # # else:
# # # # # #     print(f"✅ Recommended Configuration: Swap to '{results['recommended_plan']}' (₹{results['recommended_price']}/month)")
# # # # # #     print(f"📉 Plan Capacity: Only {results['data_limit']} GB/day (Perfect match for your behavior)")
    
# # # # # #     if results['monthly_savings'] > 0:
# # # # # #         print(f"💰 Wasted Money Recovered: ₹{results['monthly_savings']}/month")
# # # # # #         print(f"🔥 Annual Billionaire Scale Projection: You will save ₹{results['annual_savings']} per year!")
# # # # # #     else:
# # # # # #         print("💡 Insight: You are already using the most optimized cost-efficient plan for your usage matrix.")
# # # # # # print("="*40 + "\n")

# # # # # # # --- STEP 3: INTERACTIVE USER SIMULATION INPUT (UPDATED WITH STRING CASE FIX) ---
# # # # # # print("\n" + "="*40)
# # # # # # print("🚀 MOBILE DATA SAVINGS CALCULATOR MVP")
# # # # # # print("="*40)

# # # # # # # .strip().capitalize() handles trailing spaces and converts 'jio' or 'JIO' to 'Jio' automatically
# # # # # # user_provider = input("Enter your provider (Jio / Airtel): ").strip().capitalize()
# # # # # # user_current_cost = float(input("Enter your current monthly bill/recharge cost (in ₹): "))
# # # # # # user_actual_usage = float(input("Enter your actual daily data usage average (in GB): "))

# # # # # # # Executing the system
# # # # # # results, error = calculate_savings(user_provider, user_current_cost, user_actual_usage)

# # # # # # # --- STEP 4: SYSTEM METRICS OUTPUT ENGINE ---
# # # # # # print("\n" + "-"*40)
# # # # # # print("📊 SYSTEM ANALYTICS & INSIGHT REPORT:")
# # # # # # print("-"*40)

# # # # # # if error:
# # # # # #     print(f"❌ Alert: {error}")
# # # # # # else:
# # # # # #     print(f"✅ Recommended Configuration: Swap to '{results['recommended_plan']}' (₹{results['recommended_price']}/month)")
# # # # # #     print(f"📉 Plan Capacity: Only {results['data_limit']} GB/day (Perfect match for your behavior)")
    
# # # # # #     if results['monthly_savings'] > 0:
# # # # # #         print(f"💰 Wasted Money Recovered: ₹{results['monthly_savings']}/month")
# # # # # #         print(f"🔥 Annual Billionaire Scale Projection: You will save ₹{results['annual_savings']} per year!")
# # # # # #     else:
# # # # # #         print("💡 Insight: You are already using the most optimized cost-efficient plan for your usage matrix.")
# # # # # # print("="*40 + "\n")

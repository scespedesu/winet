#!/usr/bin/env python3
"""
One-off script used to seed the _publications/ collection from a draft
list compiled from public indexes (ResearchGate) on 2026-09-10.

This is NOT meant to run automatically as part of the site build --
it's kept here only so it's clear how the initial draft files were
generated, and in case it's useful as a starting point for a future
bulk import. To add a single new publication, just copy an existing
file in _publications/ instead of running this script.
"""
import re
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "_publications")

# (year, title, venue, type)
PUBS = [
    (2026, "Evaluating SCHC Under Intermittent Connectivity: Insights From Satellite IoT", "IEEE Internet of Things Journal", "journal"),
    (2026, "Contact Plan Design For Optical Interplanetary Communications", "Preprint", "preprint"),
    (2026, "GEMINIS Observability Module: Monitoring the Environmental Sustainability of IoT Infrastructures", "Book Chapter", "chapter"),
    (2026, "WASY: A Distributed Time Slot Synchronization Mechanism for Direct-to-Satellite IoT Systems", "IEEE Wireless Communications Letters", "journal"),
    (2026, "RLQO: Reinforcement Learning-Based AQM for Fluctuating mmWave RAN Links in 5G-A/6G", "IEEE Access", "journal"),
    (2025, "Modeling Pointing, Acquisition, and Tracking Delays in Free-Space Optical Satellite Networks", "Preprint / Conference Paper", "conference"),
    (2025, "From 5G RAN Queue Dynamics to Playback: A Performance Analysis for QUIC Video Streaming", "IEEE Transactions on Networking", "journal"),
    (2025, "Nonorthogonal Multiple-Access Strategies for Direct-to-Satellite IoT Networks", "IEEE Transactions on Aerospace and Electronic Systems", "journal"),
    (2025, "A Framework for Secure Autonomic IoT Device Management in Constrained Networks", "Conference Paper", "conference"),
    (2025, "QUIC Adaptive Video Streaming Performance with 5G RAN Queue Management", "Conference Paper", "conference"),
    (2025, "Network Size Estimation in DtS-IoT: A LoRaWAN Approach for Satellite Constellations", "Conference Paper", "conference"),
    (2025, "Enhancing Urban Road Safety: A 5G NR Model for Vulnerable Road Users Awareness", "IEEE Access", "journal"),
    (2025, "Enhancing LEO Direct-to-Satellite Channel Modeling with the Shadowing Effect via K-Distribution", "ICT Express", "journal"),
    (2025, "Accurate Lane Change Prediction on Highways through Bidirectional Driving Profile Modeling", "Preprint", "preprint"),
    (2025, "Toward Safer Mines: A Robust Wireless Sensor Network Placement for Real-World Underground Conditions", "IEEE Access", "journal"),
    (2024, "Autonomous Max-Flow Interplanetary Laser Link Scheduling for Martian Exploration", "Conference Paper", "conference"),
    (2024, "True Rays Model Integration in OMNeT++ for IIoT Network Planning in Underground Mines", "Conference Paper", "conference"),
    (2024, "GEMINIS — Green Evaluation Methodology for IoT and Network Infrastructure Sustainability", "Conference Paper", "conference"),
    (2024, "SCHC over DtS-IoT: Performance of SCHC Confirmation Modes in Satellite IoT", "Conference Paper", "conference"),
    (2024, "Unlocking DtS-IoT Medium Access Through the Massively Scalable Distributed Queuing Protocol", "Conference Paper", "conference"),
    (2024, "Work in Progress: Congestion Control in mmWave Fluctuating Scenarios in 5G-A/6G", "Conference Paper", "conference"),
    (2024, "DtS-IoT Resource Allocation Analysis Framework: Assessing DQ and RESS-IoT", "Conference Paper", "conference"),
    (2024, "A Deep Dive into Congestion Control and Buffer Management for Fluctuation-Prone 5G-A/6G Links", "Conference Paper", "conference"),
    (2024, "First Workshop on Connected Micromobility for Safe and Sustainable Communities", "Conference Paper", "conference"),
    (2024, "Evaluating Propagation Models for IIoT in Underground Mining: an Experimental Comparative Study in Underground Coal Mines", "Conference Paper", "conference"),
    (2024, "Satellite Visibility Prediction for Constrained Devices in Direct-to-Satellite IoT Systems", "IEEE Sensors Journal", "journal"),
    (2024, "Road Incident Detection Under Rate Adaptation-Based Congestion Control in Cooperative Vehicular Systems", "IEEE Access", "journal"),
    (2024, "Optimizing Quality and Energy Efficiency in WebRTC with ML-Powered Adaptive FEC", "Conference Paper", "conference"),
    (2024, "On the Role of Delay Tolerant Networks and Contact Graph Routing in Direct-to-Satellite IoT", "Conference Paper", "conference"),
    (2024, "A Survey on Error Exponents in Distributed Hypothesis Testing", "Entropy", "journal"),
    (2024, "Sailing the Cosmic Seas: Improving Dependability in IoT-Based Deep Space Exploration", "Conference Paper", "conference"),
    (2023, "Know Your Vulnerable Neighbors: Awareness Model for 5G C-V2X Communications Mode 2", "Conference Paper", "conference"),
    (2023, "Performance Evaluation of Congestion Control Over B5G/6G Fluctuating Scenarios", "Conference Paper", "conference"),
    (2023, "Network Size Estimation for LoRa-Based Direct-to-Satellite IoT", "Conference Paper", "conference"),
    (2023, "Network Size Estimation for Direct-to-Satellite IoT", "IEEE Internet of Things Journal", "journal"),
    (2022, "Modeling SCHC ACK-on-Error Fragment Delivery over Sigfox", "Conference Paper", "conference"),
    (2022, "Toward the Coexistence of Cognitive Networks for Vehicular Communications on TVWS for IEEE Std. 802.22", "IEEE Transactions on Cognitive Communications and Networking", "journal"),
    (2022, "Uplink Transmission Policies for LoRa-Based Direct-to-Satellite IoT", "IEEE Access", "journal"),
    (2022, "Survey of Cooperative Advanced Driver Assistance Systems: From a Holistic and Systemic Vision", "Sensors", "journal"),
    (2022, "SCHC over LoRaWAN Efficiency: Evaluation and Experimental Performance of Packet Fragmentation", "Sensors", "journal"),
    (2022, "Impact of Diversity Combining Schemes in a Multi-Cell VLC System with Angle Diversity Receivers", "Photonic Network Communications", "journal"),
    (2022, "Optimal Traffic Load Allocation for Aloha-Based IoT LEO Constellations", "IEEE Sensors Journal", "journal"),
    (2022, "Packet Fragmentation over Sigfox: Implementation and Performance Evaluation of SCHC ACK-on-Error", "IEEE Internet of Things Journal", "journal"),
    (2022, "RESS-IoT: A Scalable Energy-Efficient MAC Protocol for Direct-to-Satellite IoT", "IEEE Access", "journal"),
    (2022, "Performance Evaluation of IEEE 802.11ax for Residential Networks", "Conference Paper", "conference"),
    (2022, "Guest Editorial Special Issue on Cybertwin-Driven 6G", "IEEE Internet of Things Journal", "journal"),
    (2021, "Direct-to-Satellite IoT Slotted Aloha Systems with Multiple Satellites and Unequal Erasure Probabilities", "Sensors", "journal"),
    (2021, "Analysis of Channel Models for LoRa-based Direct-to-Satellite IoT Networks Served by LEO Nanosatellites", "Conference Paper", "conference"),
    (2021, "Network Size Estimation in Direct-to-Satellite IoT", "Conference Paper", "conference"),
    (2021, "Impact of Safety Message Generation Rules on the Awareness of Vulnerable Road Users", "Sensors", "journal"),
    (2021, "Impact of Awareness Control on V2V-Based Overtaking Application in Autonomous Driving", "IEEE Communications Letters", "journal"),
    (2021, "A Comprehensive Survey on Vehicular Networks for Smart Roads: A Focus on IP-Based Approaches", "Vehicular Communications", "journal"),
    (2021, "Automated Decision System to Exploit Network Diversity for Connected Vehicles", "IEEE Transactions on Vehicular Technology", "journal"),
    (2021, "Pedestrians Also Have Something to Say: Integration of Connected VRU in Bidirectional Simulations", "Conference Paper", "conference"),
    (2021, "Evaluation of Opportunistic Access Strategies for Vehicular Networking Over TVWS", "Conference Paper", "conference"),
    (2021, "Increasing Safety at Vehicular Intersections with a Controlled Retransmission of Beacons", "Conference Paper", "conference"),
    (2021, "On MAC Protocols Performance for M2M Communications", "Conference Paper", "conference"),
    (2021, "Analysis and Evaluation of HTTP/2 Flow Control Algorithm for IoT", "Conference Paper", "conference"),
    (2021, "Communication Requirements in Microgrids: A Practical Survey", "IEEE Access", "journal"),
    (2021, "POSACC: Position-Accuracy Based Adaptive Beaconing Algorithm for Cooperative Vehicular Safety Systems", "IEEE Access", "journal"),
]

def slugify(title, year):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    words = s.split("-")[:8]
    return f"{year}-" + "-".join(words) + ".md"

os.makedirs(OUT_DIR, exist_ok=True)
for year, title, venue, ptype in PUBS:
    fname = slugify(title, year)
    path = os.path.join(OUT_DIR, fname)
    title_escaped = title.replace('"', '\\"')
    venue_escaped = venue.replace('"', '\\"')
    content = f'''---
title: "{title_escaped}"
authors: "S. Céspedes, et al."
venue: "{venue_escaped}"
year: {year}
type: {ptype}
verified: false
---
'''
    with open(path, "w") as f:
        f.write(content)

print(f"Wrote {len(PUBS)} publication files to {OUT_DIR}")

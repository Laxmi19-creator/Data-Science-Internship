"""
Script: generate_diagrams.py
Description: Generates 300 DPI high-resolution strategic architecture diagrams
for Week 2: Exploratory Data Analysis (EDA) and Visualization Framework Design.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

def create_eda_workflow_pipeline():
    """Generates the 6-stage end-to-end EDA execution pipeline."""
    fig, ax = plt.subplots(figsize=(15, 8), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Title & Subtitle
    plt.text(0.5, 0.94, "END-TO-END EXPLORATORY DATA ANALYSIS (EDA) FRAMEWORK",
             fontsize=16, fontweight='bold', ha='center', color='#0F172A', transform=fig.transFigure)
    plt.text(0.5, 0.90, "Standardized 6-Stage Analytical Lifecycle for Enterprise Data Understanding & Model Readiness",
             fontsize=10.5, ha='center', color='#475569', transform=fig.transFigure)

    stages = [
        {
            "num": "01",
            "title": "Ingestion & Type Audit",
            "color": "#1E3A8A",
            "bg": "#EFF6FF",
            "border": "#3B82F6",
            "items": [
                "- Schema & Memory Inspection",
                "- High-Cardinality Auditing",
                "- Continuous vs Discrete Casts",
                "- Datetime & UTC Normalization"
            ]
        },
        {
            "num": "02",
            "title": "Data Integrity & Cleaning",
            "color": "#0D9488",
            "bg": "#F0FDFA",
            "border": "#14B8A6",
            "items": [
                "- Missingness Mechanisms (MCAR/MAR)",
                "- Null Imputation Protocols",
                "- Duplicate Record Elimination",
                "- Structural Error Rectification"
            ]
        },
        {
            "num": "03",
            "title": "Univariate Profiling",
            "color": "#D97706",
            "bg": "#FFFBEB",
            "border": "#F59E0B",
            "items": [
                "- Skewness & Kurtosis Checks",
                "- IQR & Z-score Outlier Caps",
                "- Frequency & Pareto Analysis",
                "- Normality & Q-Q Diagnostics"
            ]
        },
        {
            "num": "04",
            "title": "Bivariate Interactions",
            "color": "#7C3AED",
            "bg": "#FAF5FF",
            "border": "#8B5CF6",
            "items": [
                "- Pearson, Spearman & Kendall",
                "- ANOVA & Kruskal-Wallis Tests",
                "- Chi-Square & Cramers V",
                "- Target-Feature Associations"
            ]
        },
        {
            "num": "05",
            "title": "Multivariate Analysis",
            "color": "#E11D48",
            "bg": "#FFF1F2",
            "border": "#FB7185",
            "items": [
                "- Multicollinearity & VIF Filters",
                "- High-Order Interactions",
                "- PCA / t-SNE Projections",
                "- Unsupervised Cluster Profiling"
            ]
        },
        {
            "num": "06",
            "title": "Synthesis & Modeling Gate",
            "color": "#047857",
            "bg": "#ECFDF5",
            "border": "#10B981",
            "items": [
                "- Feature Selection Roadmap",
                "- Transformation Recommendations",
                "- Data Dictionary Validation",
                "- Executive EDA Deliverable"
            ]
        }
    ]

    card_width = 2.1
    card_height = 4.2
    start_x = 0.6
    spacing = 2.35
    y_pos = 1.8

    for i, s in enumerate(stages):
        cx = start_x + i * spacing

        # Outer Shadow Box
        shadow = patches.FancyBboxPatch((cx + 0.04, y_pos - 0.04), card_width, card_height,
                                        boxstyle="round,pad=0.08,rounding_size=0.15",
                                        facecolor='#E2E8F0', edgecolor='none', zorder=1)
        ax.add_patch(shadow)

        # Main Card Box
        card = patches.FancyBboxPatch((cx, y_pos), card_width, card_height,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=s["bg"], edgecolor=s["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Header Badge
        badge = patches.FancyBboxPatch((cx + 0.15, y_pos + card_height - 0.65), card_width - 0.3, 0.45,
                                       boxstyle="round,pad=0.05,rounding_size=0.08",
                                       facecolor=s["color"], edgecolor='none', zorder=3)
        ax.add_patch(badge)

        ax.text(cx + card_width/2, y_pos + card_height - 0.42, f"STAGE {s['num']}",
                fontsize=9.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

        # Card Title
        ax.text(cx + card_width/2, y_pos + card_height - 0.95, s["title"],
                fontsize=10.5, fontweight='bold', color='#0F172A', ha='center', va='center', zorder=4)

        # Divider line
        ax.plot([cx + 0.2, cx + card_width - 0.2], [y_pos + card_height - 1.25, y_pos + card_height - 1.25],
                color=s["border"], linewidth=0.8, linestyle='--', zorder=4)

        # Items list
        for j, item in enumerate(s["items"]):
            ax.text(cx + 0.18, y_pos + card_height - 1.6 - (j * 0.6), item,
                    fontsize=8.5, color='#334155', ha='left', va='center', zorder=4)

        # Connecting Arrow (except last)
        if i < len(stages) - 1:
            ax.annotate('', xy=(cx + card_width + 0.22, y_pos + card_height/2),
                        xytext=(cx + card_width + 0.02, y_pos + card_height/2),
                        arrowprops=dict(facecolor='#64748B', edgecolor='none', width=2.5, headwidth=7),
                        zorder=5)

    # Feedback loop arc
    arc = patches.FancyArrowPatch((start_x + 5 * spacing + card_width/2, y_pos - 0.2),
                                  (start_x + spacing + card_width/2, y_pos - 0.2),
                                  connectionstyle="arc3,rad=-0.22",
                                  color="#64748B", linestyle=":", linewidth=1.5,
                                  arrowstyle="->", mutation_scale=15, zorder=6)
    ax.add_patch(arc)
    ax.text(start_x + 3 * spacing, y_pos - 0.9,
            "Iterative Feedback: Data Cleaning & Feature Transformation Re-evaluation",
            fontsize=9, color="#475569", ha='center', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=0.8))

    ax.set_xlim(0, 15)
    ax.set_ylim(0.5, 7.2)
    ax.axis('off')

    output_path = os.path.join(OUTPUT_DIR, "eda_workflow_pipeline.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")


def create_missing_data_outlier_decision_tree():
    """Generates the decision tree for handling Missing Data & Outliers."""
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    plt.text(0.5, 0.95, "DATA ANOMALY RESOLUTION & IMPUTATION ARCHITECTURE",
             fontsize=16, fontweight='bold', ha='center', color='#0F172A', transform=fig.transFigure)
    plt.text(0.5, 0.91, "Deterministic Decision Protocols for Missingness Mechanisms (MCAR/MAR/MNAR) and Outlier Treatment",
             fontsize=10.5, ha='center', color='#475569', transform=fig.transFigure)

    # Split into Two Pillars: Left = Missing Data, Right = Outlier Treatment
    # Pillar 1: Missing Data
    p1_box = patches.FancyBboxPatch((0.5, 0.8), 6.7, 6.2,
                                    boxstyle="round,pad=0.1,rounding_size=0.15",
                                    facecolor="#F0FDF4", edgecolor="#16A34A", linewidth=1.5)
    ax.add_patch(p1_box)

    ax.text(3.85, 6.7, "PILLAR I: MISSING DATA TAXONOMY & RESOLUTION",
            fontsize=12, fontweight='bold', color="#166534", ha='center')

    m_nodes = [
        {"x": 1.0, "y": 5.2, "w": 5.7, "h": 1.1, "title": "1. Diagnosis & Mechanism Testing",
         "desc": "Little's MCAR Test | Missingno Matrix | Correlation Heatmap\nCheck if missingness depends on observed or unobserved data"},
        {"x": 1.0, "y": 3.7, "w": 5.7, "h": 1.2, "title": "2. Mechanism-Specific Routing",
         "desc": "MCAR (<5%): Complete Case Analysis / Listwise Deletion\nMAR: Multivariate Imputation by Chained Equations (MICE) / KNN\nMNAR: Pattern-Submodel Flagging + Domain Imputation"},
        {"x": 1.0, "y": 1.2, "w": 5.7, "h": 2.1, "title": "3. Production Imputation Framework",
         "desc": "* Numerical: Median + Missingness Indicator flag\n* Categorical: Mode or Dedicated 'Missing' / 'Unknown' Token\n* Sequential/TS: Forward/Backward Fill or Spline Interpolation\n* Complex/Tabular: MissForest (Random Forest) / IterativeImputer\n* Leakage Guard: Fit imputers STRICTLY on Training folds"}
    ]

    for node in m_nodes:
        box = patches.FancyBboxPatch((node["x"], node["y"]), node["w"], node["h"],
                                     boxstyle="round,pad=0.08,rounding_size=0.1",
                                     facecolor="#FFFFFF", edgecolor="#86EFAC", linewidth=1.2)
        ax.add_patch(box)
        ax.text(node["x"] + 0.2, node["y"] + node["h"] - 0.25, node["title"],
                fontsize=10, fontweight='bold', color="#15803D")
        ax.text(node["x"] + 0.2, node["y"] + node["h"] - 0.65, node["desc"],
                fontsize=8.5, color="#1E293B", va="top")

    # Arrows between missing nodes
    ax.annotate('', xy=(3.85, 4.9), xytext=(3.85, 5.2),
                arrowprops=dict(facecolor='#16A34A', edgecolor='none', width=2, headwidth=6))
    ax.annotate('', xy=(3.85, 3.3), xytext=(3.85, 3.6),
                arrowprops=dict(facecolor='#16A34A', edgecolor='none', width=2, headwidth=6))

    # Pillar 2: Outliers
    p2_box = patches.FancyBboxPatch((7.8, 0.8), 6.7, 6.2,
                                    boxstyle="round,pad=0.1,rounding_size=0.15",
                                    facecolor="#EFF6FF", edgecolor="#2563EB", linewidth=1.5)
    ax.add_patch(p2_box)

    ax.text(11.15, 6.7, "PILLAR II: OUTLIER DETECTION & TREATMENT",
            fontsize=12, fontweight='bold', color="#1E40AF", ha='center')

    o_nodes = [
        {"x": 8.3, "y": 5.2, "w": 5.7, "h": 1.1, "title": "1. Multi-Tier Detection Protocols",
         "desc": "Univariate: Tukey's IQR (1.5x / 3x) & Modified Z-Score (MAD)\nMultivariate: Mahalanobis Distance (Covariance) & Cook's D\nHigh-Dimensional: Isolation Forest & Local Outlier Factor (LOF)"},
        {"x": 8.3, "y": 3.7, "w": 5.7, "h": 1.2, "title": "2. Validation & Classification",
         "desc": "True Anomalies vs Natural Heavy-Tailed Extremes\n* Measurement Error / Sensor Glitch: Discard or Remediate\n* Rare Valid Event (Fraud/Spikes): Preserve with Transformation\n* Target Sensitivity: Gauge model algorithm vulnerability"},
        {"x": 8.3, "y": 1.2, "w": 5.7, "h": 2.1, "title": "3. Systematic Remediation Protocols",
         "desc": "* Winsorization / Spatial Capping (99th / 1st Percentile)\n* Non-Linear Transformation: Log1p, Box-Cox, Yeo-Johnson\n* Robust Scaling: QuantileTransformer / RobustScaler\n* Algorithmic Resilience: Tree ensembles over linear hyperplanes\n* Dedicated Anomaly Flag: Add binary indicator feature"}
    ]

    for node in o_nodes:
        box = patches.FancyBboxPatch((node["x"], node["y"]), node["w"], node["h"],
                                     boxstyle="round,pad=0.08,rounding_size=0.1",
                                     facecolor="#FFFFFF", edgecolor="#93C5FD", linewidth=1.2)
        ax.add_patch(box)
        ax.text(node["x"] + 0.2, node["y"] + node["h"] - 0.25, node["title"],
                fontsize=10, fontweight='bold', color="#1D4ED8")
        ax.text(node["x"] + 0.2, node["y"] + node["h"] - 0.65, node["desc"],
                fontsize=8.5, color="#1E293B", va="top")

    # Arrows between outlier nodes
    ax.annotate('', xy=(11.15, 4.9), xytext=(11.15, 5.2),
                arrowprops=dict(facecolor='#2563EB', edgecolor='none', width=2, headwidth=6))
    ax.annotate('', xy=(11.15, 3.3), xytext=(11.15, 3.6),
                arrowprops=dict(facecolor='#2563EB', edgecolor='none', width=2, headwidth=6))

    ax.set_xlim(0, 15)
    ax.set_ylim(0.5, 7.5)
    ax.axis('off')

    output_path = os.path.join(OUTPUT_DIR, "missing_data_outlier_decision_tree.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")


def create_visualization_strategy_taxonomy():
    """Generates the Visualization Strategy Matrix across Data Types & Analysis Goals."""
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    plt.text(0.5, 0.95, "VISUALIZATION STRATEGY & EXPLORATORY PLOTTING TAXONOMY",
             fontsize=16, fontweight='bold', ha='center', color='#0F172A', transform=fig.transFigure)
    plt.text(0.5, 0.91, "Mapping Analytical Objectives and Dimensionalities to Statistical Visual Archetypes",
             fontsize=10.5, ha='center', color='#475569', transform=fig.transFigure)

    categories = [
        {
            "category": "DISTRIBUTION & SPREAD",
            "goal": "Uncover shape, central tendency, variance & kurtosis",
            "color": "#1E3A8A",
            "bg": "#EFF6FF",
            "border": "#3B82F6",
            "plots": [
                ("Histogram + KDE", "Continuous frequency & estimated density curve"),
                ("Box & Violin Plots", "Median, IQR, whiskers & multimodal kernel distributions"),
                ("Normal Q-Q Plot", "Theoretical quantile mapping for Gaussian testing"),
                ("Empirical CDF (ECDF)", "Non-parametric cumulative proportion tracing")
            ],
            "tools": "Seaborn (histplot, violinplot) | Matplotlib | Statsmodels (qqplot)"
        },
        {
            "category": "COMPARISON & PROPORTIONS",
            "goal": "Benchmark discrete groups, cohorts & category shares",
            "color": "#0D9488",
            "bg": "#F0FDFA",
            "border": "#14B8A6",
            "plots": [
                ("Grouped / Stacked Bar", "Category counts across binary or multi-class factors"),
                ("Pareto Chart (80/20)", "Rank-ordered discrete volume with cumulative line"),
                ("Treemap & Sunburst", "Hierarchical composition and relative nested volumes"),
                ("Radar / Spider Chart", "Multi-attribute benchmark against peer averages")
            ],
            "tools": "Plotly Express (treemap, bar) | Seaborn (barplot, countplot)"
        },
        {
            "category": "RELATIONSHIP & CORRELATION",
            "goal": "Evaluate associations, dependencies & functional curves",
            "color": "#7C3AED",
            "bg": "#FAF5FF",
            "border": "#8B5CF6",
            "plots": [
                ("Scatter + Marginal KDE", "Bivariate interactions with univariate boundary density"),
                ("Hierarchical Clustermap", "Clustered Pearson/Spearman matrix with dendrograms"),
                ("Pairplot / Scatter Matrix", "Full cross-feature interaction grid with hue coloring"),
                ("Partial Dependence Plot", "Non-linear feature impact marginalizing other predictors")
            ],
            "tools": "Seaborn (pairplot, clustermap, regplot) | Scikit-Learn (PDP)"
        },
        {
            "category": "TEMPORAL & HIGH-DIMENSIONAL",
            "goal": "Track longitudinal trends and compress dense manifolds",
            "color": "#C026D3",
            "bg": "#FDF4FF",
            "border": "#E879F9",
            "plots": [
                ("Decomposed Time-Series", "Longitudinal line with Trend, Seasonality & Residuals"),
                ("Heatmap Matrix (Day/Hour)", "Temporal intensity surface across cyclic time bins"),
                ("Parallel Coordinates", "High-dimensional multivariate profile across all features"),
                ("t-SNE / UMAP Projections", "Non-linear 2D/3D manifold embeddings for clustering")
            ],
            "tools": "Plotly (parallel_coordinates) | Statsmodels (seasonal_decompose) | UMAP"
        }
    ]

    x_positions = [0.6, 4.2, 7.8, 11.4]
    card_width = 3.3
    card_height = 5.8
    y_pos = 1.0

    for i, cat in enumerate(categories):
        cx = x_positions[i]

        # Shadow
        shadow = patches.FancyBboxPatch((cx + 0.05, y_pos - 0.05), card_width, card_height,
                                        boxstyle="round,pad=0.08,rounding_size=0.15",
                                        facecolor='#E2E8F0', edgecolor='none', zorder=1)
        ax.add_patch(shadow)

        # Card
        card = patches.FancyBboxPatch((cx, y_pos), card_width, card_height,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=cat["bg"], edgecolor=cat["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Header Box
        header = patches.FancyBboxPatch((cx + 0.15, y_pos + card_height - 0.75), card_width - 0.3, 0.55,
                                        boxstyle="round,pad=0.05,rounding_size=0.08",
                                        facecolor=cat["color"], edgecolor='none', zorder=3)
        ax.add_patch(header)

        ax.text(cx + card_width/2, y_pos + card_height - 0.48, cat["category"],
                fontsize=9.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

        ax.text(cx + card_width/2, y_pos + card_height - 1.05, cat["goal"],
                fontsize=8, color='#475569', ha='center', style='italic', zorder=4)

        ax.plot([cx + 0.2, cx + card_width - 0.2], [y_pos + card_height - 1.35, y_pos + card_height - 1.35],
                color=cat["border"], linewidth=0.8, linestyle='--', zorder=4)

        # Plots list
        for j, (p_title, p_desc) in enumerate(cat["plots"]):
            py = y_pos + card_height - 1.7 - (j * 0.85)

            p_box = patches.FancyBboxPatch((cx + 0.15, py - 0.25), card_width - 0.3, 0.75,
                                           boxstyle="round,pad=0.04,rounding_size=0.06",
                                           facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=0.8, zorder=3)
            ax.add_patch(p_box)

            ax.text(cx + 0.25, py + 0.28, f"* {p_title}",
                    fontsize=8.5, fontweight='bold', color='#0F172A', zorder=4)
            ax.text(cx + 0.25, py + 0.05, p_desc,
                    fontsize=7.5, color='#475569', zorder=4)

        # Bottom Tools Box
        t_box = patches.FancyBboxPatch((cx + 0.15, y_pos + 0.2), card_width - 0.3, 0.65,
                                       boxstyle="round,pad=0.04,rounding_size=0.06",
                                       facecolor='#F1F5F9', edgecolor='#94A3B8', linewidth=0.8, zorder=3)
        ax.add_patch(t_box)
        ax.text(cx + card_width/2, y_pos + 0.62, "Primary Library Stack:",
                fontsize=7.5, fontweight='bold', color='#1E293B', ha='center', zorder=4)
        ax.text(cx + card_width/2, y_pos + 0.38, cat["tools"],
                fontsize=7, color='#0F172A', ha='center', zorder=4)

    ax.set_xlim(0, 15.3)
    ax.set_ylim(0.5, 7.5)
    ax.axis('off')

    output_path = os.path.join(OUTPUT_DIR, "visualization_strategy_taxonomy.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")


def create_eda_reporting_governance_architecture():
    """Generates the Multi-tier EDA Reporting and Stakeholder Communication Architecture."""
    fig, ax = plt.subplots(figsize=(15, 8), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    plt.text(0.5, 0.94, "EDA DOCUMENTATION, GOVERNANCE & REPORTING ARCHITECTURE",
             fontsize=16, fontweight='bold', ha='center', color='#0F172A', transform=fig.transFigure)
    plt.text(0.5, 0.90, "Multi-Tier Artifact Hierarchy Bridging Technical Rigor and Strategic Decision-Making",
             fontsize=10.5, ha='center', color='#475569', transform=fig.transFigure)

    tiers = [
        {
            "tier": "TIER 1: AUTOMATED AUDIT & BASELINE PROFILING",
            "desc": "Rapid algorithmic reconnaissance & static data health verification",
            "color": "#0284C7",
            "bg": "#F0F9FF",
            "border": "#38BDF8",
            "outputs": [
                "Automated YData-Profiling / Sweetviz HTML Health Dossier",
                "Automated Nullity Density Matrix via Missingno",
                "Schema Data Dictionary (Data Types, Memory Footprint, Cardinality)",
                "Preliminary Zero-Variance & Leakage Red Flag Audits"
            ],
            "audience": "Data Engineering & Core Data Science Team"
        },
        {
            "tier": "TIER 2: TECHNICAL DEEP-DIVE JUPYTER BLUEPRINT",
            "desc": "Exhaustive hypothesis testing, mathematical proofs & transformation recipes",
            "color": "#4F46E5",
            "bg": "#EEF2FF",
            "border": "#818CF8",
            "outputs": [
                "Reproducible Jupyter / Quarto Notebook with Parameterized Steps",
                "Bivariate Correlation Matrices, VIF Thresholds & Multicollinearity Pruning",
                "Non-parametric Tests (Kruskal-Wallis, Mann-Whitney U, Cramers V)",
                "Mathematical Justification for Yeo-Johnson / Robust Scaler Transforms"
            ],
            "audience": "Lead Data Scientists, ML Engineers & Peer Reviewers"
        },
        {
            "tier": "TIER 3: INTERACTIVE EXPLORATORY DASHBOARD",
            "desc": "Dynamic visual discovery tool for multi-factor slice-and-dice exploration",
            "color": "#9333EA",
            "bg": "#FAF5FF",
            "border": "#C084FC",
            "outputs": [
                "Streamlit / Plotly Dash Interactive Web Application",
                "Dynamic Cohort Filtering across Geographies, Tiers & Tenures",
                "What-If Interactive Feature Distribution Sliders",
                "Real-Time Cross-Tabulation & Exportable Anomaly Drilldowns"
            ],
            "audience": "Product Managers, Domain SMEs & Business Analysts"
        },
        {
            "tier": "TIER 4: EXECUTIVE STRATEGY DOSSIER & ML READINESS GATE",
            "desc": "C-suite strategic summary, business risk matrix & modeling authorization",
            "color": "#0F766E",
            "bg": "#F0FDFA",
            "border": "#2DD4BF",
            "outputs": [
                "Executive Summary Word / PDF Deliverable with Key Hypotheses",
                "Data Quality Scorecard (Completeness, Accuracy, Representation)",
                "Business Impact & ROI Valuation of Identified Feature Drivers",
                "Formal Modeling Sign-Off & Data Readiness Certification"
            ],
            "audience": "Chief Data Officer (CDO), Business Sponsors & VP of Engineering"
        }
    ]

    y_start = 5.3
    row_height = 1.35
    row_spacing = 1.45

    for i, t in enumerate(tiers):
        ry = y_start - (i * row_spacing)

        # Shadow
        shadow = patches.FancyBboxPatch((0.74, ry - 0.04), 13.52, row_height,
                                        boxstyle="round,pad=0.08,rounding_size=0.12",
                                        facecolor='#E2E8F0', edgecolor='none', zorder=1)
        ax.add_patch(shadow)

        # Card
        card = patches.FancyBboxPatch((0.7, ry), 13.5, row_height,
                                      boxstyle="round,pad=0.08,rounding_size=0.12",
                                      facecolor=t["bg"], edgecolor=t["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Tier Tag
        tag = patches.FancyBboxPatch((0.9, ry + row_height - 0.38), 5.5, 0.28,
                                     boxstyle="round,pad=0.04,rounding_size=0.06",
                                     facecolor=t["color"], edgecolor='none', zorder=3)
        ax.add_patch(tag)
        ax.text(3.65, ry + row_height - 0.24, t["tier"],
                fontsize=8.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

        ax.text(6.6, ry + row_height - 0.24, f"Purpose: {t['desc']}",
                fontsize=8.5, color='#475569', style='italic', zorder=4)

        # Outputs (2 columns of 2 items)
        col1_x = 1.0
        col2_x = 7.4

        ax.text(col1_x, ry + 0.70, f"[+] {t['outputs'][0]}", fontsize=8, color='#1E293B', zorder=4)
        ax.text(col1_x, ry + 0.35, f"[+] {t['outputs'][1]}", fontsize=8, color='#1E293B', zorder=4)

        ax.text(col2_x, ry + 0.70, f"[+] {t['outputs'][2]}", fontsize=8, color='#1E293B', zorder=4)
        ax.text(col2_x, ry + 0.35, f"[+] {t['outputs'][3]}", fontsize=8, color='#1E293B', zorder=4)

        # Target Audience Pill
        aud_box = patches.FancyBboxPatch((11.4, ry + 0.25), 2.6, 0.85,
                                         boxstyle="round,pad=0.04,rounding_size=0.08",
                                         facecolor='#FFFFFF', edgecolor=t["border"], linewidth=1.0, zorder=3)
        ax.add_patch(aud_box)
        ax.text(12.7, ry + 0.8, "Target Stakeholders",
                fontsize=7.5, fontweight='bold', color=t["color"], ha='center', zorder=4)
        ax.text(12.7, ry + 0.48, t["audience"],
                fontsize=7, color='#334155', ha='center', wrap=True, zorder=4)

        # Connector to next tier
        if i < len(tiers) - 1:
            ax.annotate('', xy=(7.45, ry - 0.08), xytext=(7.45, ry + 0.02),
                        arrowprops=dict(facecolor='#64748B', edgecolor='none', width=1.8, headwidth=5),
                        zorder=5)

    ax.set_xlim(0, 15)
    ax.set_ylim(0.5, 7.2)
    ax.axis('off')

    output_path = os.path.join(OUTPUT_DIR, "eda_reporting_governance_architecture.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    print("Starting Week 2 Diagram Generation...")
    create_eda_workflow_pipeline()
    create_missing_data_outlier_decision_tree()
    create_visualization_strategy_taxonomy()
    create_eda_reporting_governance_architecture()
    print("All 4 strategic diagrams generated successfully at 300 DPI.")

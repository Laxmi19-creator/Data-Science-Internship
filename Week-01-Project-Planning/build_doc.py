import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner padding for a table cell (values in dxa: 20 dxa = 1 pt)."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D7DE", sz="4", val="single"):
    """Set subtle modern borders for a table."""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(f'<w:tblBorders {nsdecls("w")}>'
                            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                            f'<w:insideV w:val="none"/>'
                            f'<w:left w:val="none"/>'
                            f'<w:right w:val="none"/>'
                            f'</w:tblBorders>')
        tblPr[0].append(borders)

def add_callout(doc, text, title=None, border_color="1E3A8A", bg_color="F0F4F8"):
    """Add a shaded callout block with a thick colored left border."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=130, bottom=130, left=180, right=180)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
                        f'<w:top w:val="none"/>'
                        f'<w:right w:val="none"/>'
                        f'<w:bottom w:val="none"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if title:
        run_title = p.add_run(f"{title}\n")
        run_title.bold = True
        run_title.font.name = "Arial"
        run_title.font.size = Pt(10)
        r = int(border_color[0:2], 16)
        g = int(border_color[2:4], 16)
        b = int(border_color[4:6], 16)
        run_title.font.color.rgb = RGBColor(r, g, b)
    
    run_text = p.add_run(text)
    run_text.font.name = "Arial"
    run_text.font.size = Pt(9.5)
    run_text.font.italic = True
    run_text.font.color.rgb = RGBColor(30, 41, 59)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_code_box(doc, text):
    """Add a monospace diagram or architecture flow box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:left w:val="single" w:sz="12" w:space="0" w:color="94A3B8"/>'
                        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def format_custom_table(table, col_widths, headers, data_rows, header_bg="1E3A8A"):
    """Format table with corporate styling, zebra striping, and cell margins."""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="D0D7DE", sz="4")
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = Inches(col_widths[i])
        set_cell_background(hdr_cells[i], header_bg)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(title)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    # Data Rows
    for r_idx, row_data in enumerate(data_rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].width = Inches(col_widths[c_idx])
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=120, right=120)
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            run = p.add_run(val)
            run.font.name = "Arial"
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(30, 41, 59)

def add_embedded_image(doc, img_path, caption_text, width_inches=6.4):
    """Embed an image with a centered caption block."""
    if not os.path.exists(img_path):
        print(f"Warning: Image not found at {img_path}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(3)
    p_img.paragraph_format.keep_with_next = True
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(width_inches))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(12)
    run_cap = p_cap.add_run(caption_text)
    run_cap.font.name = "Arial"
    run_cap.font.size = Pt(8.5)
    run_cap.font.italic = True
    run_cap.font.color.rgb = RGBColor(100, 116, 139)

def build_ds_project_plan_doc():
    doc = docx.Document()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")
    
    # Page setup - Margins 1 inch
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.text = "Data Science Project Plan: OmniPulse Churn Optimization | Week 1 Deliverable"
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hp.runs[0].font.name = "Arial"
        hp.runs[0].font.size = Pt(8.5)
        hp.runs[0].font.color.rgb = RGBColor(128, 128, 128)
        
        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.text = "Author: Laxmi Gupta  |  Data Science Intern  |  End-to-End Project Planning & Strategy Design"
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.runs[0].font.name = "Arial"
        fp.runs[0].font.size = Pt(8.5)
        fp.runs[0].font.color.rgb = RGBColor(128, 128, 128)

    # Document Title Styling
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("Data Science Project Planning & Strategy Design: Project OmniPulse")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.bold = True
    run_title.font.color.rgb = RGBColor(30, 58, 138) # Corporate Deep Navy

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("End-to-End Predictive Customer Churn Analytics, Lifetime Value (LTV) Optimization & Proactive Retention Engine Utilizing Python")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(70, 80, 95)

    # Metadata Card Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Author / Candidate:", "Laxmi Gupta (Data Science & Analytics Intern)"),
        ("Project Task:", "Week 1 Task: Data Science Project Planning & Strategy Design"),
        ("Deliverable Type:", "Formal Industrial Project Planning Blueprint & Architecture Document (DOCX)"),
        ("Project Codename:", "Project OmniPulse (Subscription E-Commerce & SaaS Churn Architecture)"),
        ("Target Work Allocation:", "Budgeted for 32.5 Hours (Strictly within the 30–35 Hours Allocation Requirement)"),
        ("Evaluation Focus:", "Completeness of Plan, DS Process Rigor, Timeline Allocation, & Integrated Visual Diagrams")
    ]
    for idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.width = Inches(2.2)
        cell_val.width = Inches(4.3)
        set_cell_background(cell_lbl, "F1F5F9")
        set_cell_background(cell_val, "FAFAFA")
        set_cell_margins(cell_lbl, top=60, bottom=60, left=100, right=100)
        set_cell_margins(cell_val, top=60, bottom=60, left=100, right=100)
        
        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(9)
        r0.font.color.rgb = RGBColor(30, 58, 138)
        
        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.name = "Arial"
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(40, 40, 40)
        
    set_table_borders(meta_table, color="CBD5E1", sz="4")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Heading Helpers
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(5)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(14)
        r.bold = True
        r.font.color.rgb = RGBColor(30, 58, 138)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11.5)
        r.bold = True
        r.font.color.rgb = RGBColor(2, 132, 199)
        return h

    def add_p(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(30, 41, 59)
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.12
        r_bold = p.add_run(bold_prefix)
        r_bold.bold = True
        r_bold.font.name = "Arial"
        r_bold.font.size = Pt(9.5)
        r_bold.font.color.rgb = RGBColor(30, 58, 138)
        
        r_text = p.add_run(text)
        r_text.font.name = "Arial"
        r_text.font.size = Pt(9.5)
        r_text.font.color.rgb = RGBColor(30, 41, 59)
        return p

    # --- SECTION 1: BACKGROUND & MOTIVATION ---
    add_h1("1. Introduction & Project Background")
    add_h2("1.1 The Business Context & The Churn Dilemma")
    add_p(
        "In modern subscription-based business models—spanning digital SaaS, media streaming, and recurring e-commerce boxes—corporate "
        "profitability is driven by customer retention and lifetime value (LTV) maximization. The subject of this project plan is "
        "OmniPulse, a hypothetical digital subscription e-commerce platform serving 500,000 active subscribers generating an average monthly "
        "recurring revenue (MRR) of $5.0 Million ($10/month subscription fee, plus marketplace add-on purchases)."
    )
    add_p(
        "Over the previous four quarters, OmniPulse experienced an alarming increase in customer churn: monthly churn rose to 4.2%, "
        "representing roughly 21,000 cancelled accounts every month. With a Customer Acquisition Cost (CAC) of $65.00 and an average "
        "Customer Lifetime Value (LTV) of $180.00, this monthly attrition causes an annual subscription revenue loss of $3.78 Million, "
        "and over $16.3 Million in replacement customer acquisition marketing spend."
    )
    add_callout(
        doc,
        "\"Acquiring a new customer is 5 to 7 times more expensive than retaining an existing customer. A mere 5% reduction in customer "
        "churn can expand company profits by 25% to 95%. Project OmniPulse replaces reactive marketing win-back emails with a proactive, "
        "Python-driven machine learning engine that flags at-risk subscribers 30 to 45 days prior to cancellation.\"",
        title="Core Business Motivation",
        border_color="1E3A8A",
        bg_color="F0F4F8"
    )

    # --- SECTION 2: OBJECTIVES & SCOPE ---
    add_h1("2. Project Objectives & Scope Definition")
    add_h2("2.1 Specific Technical & Business Objectives")
    add_bullet("Predictive Performance Benchmark: ", "Train and optimize gradient-boosted decision trees (XGBoost/LightGBM) achieving ROC-AUC >= 0.88 and PR-AUC >= 0.72 on unseen test sets.")
    add_bullet("Business Churn Reduction Target: ", "Reduce monthly subscriber churn from 4.2% down to 3.5%, preserving approximately 3,500 subscribers per month ($756,000 annual net subscription revenue saved).")
    add_bullet("Actionable Customer Risk Stratification: ", "Segment customer base into High-Risk (>75% probability), Medium-Risk (45–75%), and Low-Risk (<45%) tiers to drive tiered retention marketing offers.")
    add_bullet("Algorithmic Explainability: ", "Provide individual-level SHAP (SHapley Additive exPlanations) attribution scores for every high-risk customer so marketing teams understand the specific churn drivers.")

    add_h2("2.2 In-Scope vs. Out-of-Scope Boundaries")
    table_scope = doc.add_table(rows=5, cols=2)
    t_scope_headers = ["In-Scope Deliverables & Activities", "Out-of-Scope Activities (Future Roadmap)"]
    t_scope_rows = [
        ["Multi-source relational data schema design (PostgreSQL)", "Building real-time Kafka streaming event bus (Batch scoring sufficient)."],
        ["Feature engineering (RFM, usage slopes, payment friction)", "Deep learning on raw audio customer support recordings."],
        ["Handling imbalanced data via SMOTE and class-weighting", "Automating credit card rebilling / payment gateway integrations."],
        ["Model explainability via TreeSHAP and cost-benefit optimization", "Redesigning the front-end web portal UI/UX."]
    ]
    format_custom_table(table_scope, [3.25, 3.25], t_scope_headers, t_scope_rows, header_bg="1E3A8A")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 3: METHODOLOGY & STRATEGY ---
    add_h1("3. Methodology & Strategic Process Architecture")
    add_p(
        "The project follows a structured, scientific data science lifecycle adapted from CRISP-DM, tailored specifically for Python machine learning:"
    )

    # Embed Diagram 1: Methodology Flowchart
    add_embedded_image(
        doc,
        os.path.join(assets_dir, "ds_methodology_flowchart.png"),
        "Figure 1: OmniPulse End-to-End Data Science Technical Lifecycle Architecture"
    )

    add_h2("3.1 Data Sourcing & Synthetic Relational Schema")
    add_p(
        "The project architecture integrates four normalized transactional entities: (1) dim_customers (demographics, subscription tier, tenure), "
        "(2) fct_billing_history (invoices, failed payment retries, refunds), (3) fct_engagement_telemetry (sessions, cart abandonments, page views), "
        "and (4) fct_customer_support (CSAT scores, ticket resolution hours, sentiment polarity). The target variable churn_flag is defined "
        "as voluntary cancellation or total inactivity within 30 days."
    )

    add_h2("3.2 Data Cleaning & Preprocessing Protocol")
    add_bullet("Multivariate Imputation (MICE): ", "Missing numeric fields are imputed using Multivariate Imputation by Chained Equations (IterativeImputer) to preserve inter-variable correlation structures; missing categorical values are assigned an 'UNKNOWN' category.")
    add_bullet("Outlier Treatment: ", "Session duration and spend distributions are winsorized at the 99.5th percentile using the Interquartile Range (IQR) rule, preventing extreme data skew from biasing gradient calculations.")
    add_bullet("Temporal Split & Target Leakage Prevention: ", "Strict temporal cutoffs are enforced. All features are calculated exclusively using data prior to cutoff date T0, eliminating look-ahead target leakage.")

    add_h2("3.3 Feature Engineering Strategy")
    add_bullet("RFM & Velocity Features: ", "Days since last session, order frequency in the last 90 days, and the 30-day vs. 90-day engagement velocity ratio (identifying steep drop-offs in active usage).")
    add_bullet("Payment Friction Indicators: ", "Count of failed card retries over 60 days and flags for credit card expiration within 30 days, cleanly separating involuntary payment failure from voluntary disengagement.")

    add_h2("3.4 Predictive Modeling & Hyperparameter Optimization")
    add_bullet("Algorithmic Benchmarking: ", "Benchmarking Logistic Regression baseline against ensemble tree models: Random Forest, XGBoost, and LightGBM.")
    add_bullet("Class Imbalance Mitigation: ", "Combining Synthetic Minority Over-sampling Technique (SMOTE) on training folds with algorithmic scale_pos_weight parameter tuning to overcome the 95:5 class imbalance.")
    add_bullet("Bayesian Hyper-tuning (Optuna): ", "Automated tuning across learning rate, tree depth, subsample ratios, and L1/L2 regularization penalties utilizing Stratified Time-Series 5-Fold Cross-Validation.")

    # Embed Diagram 3: Evaluation Framework
    add_embedded_image(
        doc,
        os.path.join(assets_dir, "model_evaluation_framework.png"),
        "Figure 2: Model Evaluation Framework — Technical Benchmarks vs. Business Cost-Benefit Matrix"
    )

    add_h2("3.5 Evaluation & Cost-Benefit Expected Value Framework")
    add_p(
        "Standard accuracy is misleading in imbalanced churn settings (predicting 'No Churn' achieves 95.8% accuracy while failing 100% of the business goal). "
        "Evaluation prioritizes Precision-Recall AUC (PR-AUC) and the Expected Value Framework: selecting the probability classification threshold that maximizes "
        "net financial return: Net Profit = (TP x $155) - (FP x $25) - (FN x $180) + (TN x $0)."
    )

    # --- SECTION 4: TIMELINE & RESOURCE ALLOCATION ---
    add_h1("4. Project Timeline & Work Breakdown Structure (~30–35 Hours)")
    add_p(
        "The project schedule is rigorously budgeted for exactly 32.5 hours, strictly adhering to the 30–35 hour allocation requirement:"
    )

    # Embed Diagram 2: Gantt Chart
    add_embedded_image(
        doc,
        os.path.join(assets_dir, "project_timeline_gantt.png"),
        "Figure 3: OmniPulse 32.5-Hour Project Implementation Timeline & Gantt Schedule"
    )

    table_time = doc.add_table(rows=8, cols=4)
    t_time_headers = ["Phase", "Workstream Description", "Allocated Hours", "Cumulative Progress"]
    t_time_rows = [
        ["Phase 1", "Problem Formulation, Business Metrics & Architecture Design", "4.0 Hours", "0.0 – 4.0 Hours (12%)"],
        ["Phase 2", "Data Ingestion Pipeline, Schema Modeling & Synthetic Generation", "5.0 Hours", "4.0 – 9.0 Hours (28%)"],
        ["Phase 3", "Data Cleaning, Imputation, Outlier Treatment & Exploratory EDA", "6.5 Hours", "9.0 – 15.5 Hours (48%)"],
        ["Phase 4", "Feature Engineering, RFM Metrics & Preprocessing Pipeline", "5.5 Hours", "15.5 – 21.0 Hours (65%)"],
        ["Phase 5", "Model Building, Baseline Comparison & Optuna Hyper-Tuning", "6.5 Hours", "21.0 – 27.5 Hours (85%)"],
        ["Phase 6", "Model Evaluation, SHAP Interpretability, API & Final Delivery", "5.0 Hours", "27.5 – 32.5 Hours (100%)"],
        ["TOTAL", "Complete End-to-End Python Data Science Implementation", "32.5 HOURS", "BUDGET: 30 - 35 HRS"]
    ]
    format_custom_table(table_time, [1.1, 2.7, 1.2, 1.5], t_time_headers, t_time_rows, header_bg="1E3A8A")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 5: TOOLS & PYTHON STACK ---
    add_h1("5. Python Libraries & Technology Stack")
    add_p(
        "Project OmniPulse leverages the modern, industry-standard Python open-source data science ecosystem:"
    )

    # Embed Diagram 4: Tech Stack
    add_embedded_image(
        doc,
        os.path.join(assets_dir, "python_tech_stack_ecosystem.png"),
        "Figure 4: Curated Python Data Science and Machine Learning Tooling Ecosystem"
    )

    table_tech = doc.add_table(rows=7, cols=3)
    t_tech_headers = ["Layer / Function", "Python Libraries", "Technical Rationale & Operational Role"]
    t_tech_rows = [
        ["Data Manipulation", "pandas, numpy, pyarrow", "Fast vectorized operations, memory-efficient columnar Parquet I/O."],
        ["Relational Database", "SQLAlchemy, psycopg2, sqlite3", "Connecting to enterprise data warehouses and structured SQL queries."],
        ["Exploratory EDA", "matplotlib, seaborn, missingno", "Statistical distributions, correlation heatmaps, missing data audits."],
        ["Feature Engineering", "scikit-learn, category_encoders, imbalanced-learn", "Reusable ColumnTransformer pipelines, TargetEncoder, SMOTE oversampling."],
        ["Machine Learning", "xgboost, lightgbm, catboost", "State-of-the-art gradient boosted decision trees for tabular classification."],
        ["Optimization & XAI", "optuna, shap, lime", "Bayesian hyperparameter tuning and game-theoretic local feature attribution."]
    ]
    format_custom_table(table_tech, [1.5, 2.2, 2.8], t_tech_headers, t_tech_rows, header_bg="1E3A8A")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 6: EXPECTED OUTCOMES & CHALLENGES ---
    add_h1("6. Expected Outcomes, Business Impact & Risk Mitigation")
    add_h2("6.1 Quantified Expected Outcomes")
    
    table_outcomes = doc.add_table(rows=7, cols=3)
    t_out_headers = ["Performance Metric / KPI", "Current Baseline (Status Quo)", "Projected Outcome (OmniPulse)"]
    t_out_rows = [
        ["Monthly Subscriber Churn Rate", "4.2% (21,000 lost subscribers/month)", "3.5% (17,500 lost subscribers/month)"],
        ["Monthly Subscribers Preserved", "0 Subscribers", "3,500 Active Subscribers Retained / Month"],
        ["Annual Net Revenue Preserved", "$0 Baseline", "$756,000 Saved Annual Recurring Revenue"],
        ["Replacement CAC Savings", "$0 Baseline", "$2,730,000 Saved Customer Acquisition Cost"],
        ["Model Discrimination (ROC-AUC)", "Random Guessing (0.50)", ">= 0.88 (Targeted Precision Ranking)"],
        ["Proactive At-Risk Warning Window", "0 Days (Reactive after cancellation)", "30 to 45 Days Proactive Warning Window"]
    ]
    format_custom_table(table_outcomes, [2.3, 2.1, 2.1], t_out_headers, t_out_rows, header_bg="1E3A8A")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_h2("6.2 Anticipated Challenges & Strategic Mitigations")
    table_risks = doc.add_table(rows=5, cols=3)
    t_risk_headers = ["Anticipated Challenge", "Operational Root Cause", "Technical Mitigation Strategy"]
    t_risk_rows = [
        ["Class Imbalance (95:5 Ratio)", "Only ~4% of users churn monthly, biasing models to predict non-churn.", "Apply SMOTE in training folds only; optimize threshold on PR-AUC; utilize scale_pos_weight in LightGBM/XGBoost."],
        ["Look-Ahead Target Leakage", "Features containing future events artificially inflating accuracy.", "Enforce strict temporal split pipelines with cutoff date T0 prior to the prediction horizon window."],
        ["Concept & Data Drift", "Consumer behavior shifts due to macroeconomics, holidays, or competitors.", "Track Population Stability Index (PSI) monthly; configure automated retraining alerts when PSI > 0.20."],
        ["Marketing 'Black Box' Skepticism", "Retention teams reject predictions due to lack of interpretability.", "Embed SHAP waterfall plots into CRM dashboards, translating weights into human-readable reasons (e.g., 'Payment Retries')."]
    ]
    format_custom_table(table_risks, [1.8, 2.2, 2.5], t_risk_headers, t_risk_rows, header_bg="1E3A8A")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # --- SECTION 7: CONCLUSION ---
    add_h1("7. Conclusion & Strategic Next Steps")
    add_p(
        "Project OmniPulse demonstrates a comprehensive, mathematically rigorous, and commercially grounded data science strategy. "
        "By structuring the problem around clear financial value drivers, enforcing leak-proof preprocessing, leveraging cutting-edge "
        "Python gradient-boosting algorithms, and integrating explainable AI via SHAP, the project bridges the gap between predictive modeling "
        "and executive business impact."
    )
    add_p(
        "With a carefully budgeted timeline of 32.5 hours, the strategy ensures realistic execution feasibility, providing an exceptional "
        "foundation for upcoming technical implementation sprints."
    )

    # Output file path
    output_filename = "Data_Science_Project_Plan_OmniPulse.docx"
    output_path = os.path.join(base_dir, output_filename)
    doc.save(output_path)
    print(f"Successfully generated DOCX deliverable at: {output_path}")

if __name__ == "__main__":
    build_ds_project_plan_doc()

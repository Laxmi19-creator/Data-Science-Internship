import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_methodology_flowchart(output_path):
    """Generate End-to-End Data Science Project Architecture Flowchart."""
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    
    stages = [
        {"title": "1. Business Understanding", "desc": "Problem formulation\nROI & churn metrics\nScope boundaries", "color": "#1E3A8A"},
        {"title": "2. Data Ingestion & Schema", "desc": "Multi-source synthesis\nPostgreSQL & APIs\nData dictionary", "color": "#0284C7"},
        {"title": "3. Cleaning & Wrangling", "desc": "Imputation strategies\nOutlier treatment\nTemporal alignment", "color": "#0D9488"},
        {"title": "4. Exploratory Analysis", "desc": "Hypothesis testing\nCorrelation matrices\nChurn driver discovery", "color": "#059669"},
        {"title": "5. Feature Engineering", "desc": "RFM segmentation\nRolling aggregations\nOne-Hot & Scaling", "color": "#D97706"},
        {"title": "6. Predictive Modeling", "desc": "XGBoost, LightGBM\nCross-validation\nBayesian Optuna tune", "color": "#7C3AED"},
        {"title": "7. Evaluation & SHAP", "desc": "PR-AUC, ROC-AUC\nCost-Benefit Matrix\nSHAP feature impact", "color": "#E11D48"},
        {"title": "8. Strategy & Deployment", "desc": "FastAPI microservice\nRetention trigger rules\nContinuous monitor", "color": "#334155"}
    ]
    
    n = len(stages)
    box_width = 1.35
    box_height = 2.8
    y_center = 3.5
    
    # Title
    ax.text(7.0, 6.3, "OmniPulse: End-to-End Data Science Lifecycle & Technical Architecture", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0F172A', fontfamily='sans-serif')
    ax.text(7.0, 5.8, "A Systematic Python-Driven Engineering Pipeline from Ingestion to Value Realization", 
            ha='center', va='center', fontsize=10.5, fontstyle='italic', color='#64748B', fontfamily='sans-serif')

    for i, stage in enumerate(stages):
        x = 0.5 + i * 1.65
        
        # Outer Card Shadow
        shadow = patches.FancyBboxPatch((x + 0.04, y_center - box_height/2 - 0.04), box_width, box_height,
                                        boxstyle="round,pad=0.08,rounding_size=0.15",
                                        facecolor='#E2E8F0', edgecolor='none')
        ax.add_patch(shadow)
        
        # Main Card Box
        card = patches.FancyBboxPatch((x, y_center - box_height/2), box_width, box_height,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor='#FFFFFF', edgecolor=stage['color'], linewidth=2)
        ax.add_patch(card)
        
        # Header Badge
        badge = patches.FancyBboxPatch((x + 0.05, y_center + box_height/2 - 0.65), box_width - 0.1, 0.55,
                                       boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor=stage['color'], edgecolor='none')
        ax.add_patch(badge)
        
        # Badge Text
        ax.text(x + box_width/2, y_center + box_height/2 - 0.38, stage['title'],
                ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF', fontfamily='sans-serif')
        
        # Body Description
        ax.text(x + box_width/2, y_center - 0.35, stage['desc'],
                ha='center', va='center', fontsize=8, color='#334155', fontfamily='sans-serif', linespacing=1.4)
        
        # Arrow connector to next step
        if i < n - 1:
            arrow_x = x + box_width + 0.03
            arrow_y = y_center
            ax.annotate('', xy=(arrow_x + 0.24, arrow_y), xytext=(arrow_x, arrow_y),
                        arrowprops=dict(facecolor='#94A3B8', edgecolor='#94A3B8', width=2, headwidth=6, headlength=6, shrink=0.05))

    # Bottom Architecture Bar
    feedback_box = patches.FancyBboxPatch((0.5, 0.4), 12.8, 0.75,
                                          boxstyle="round,pad=0.06,rounding_size=0.12",
                                          facecolor='#EFF6FF', edgecolor='#3B82F6', linestyle='--', linewidth=1.5)
    ax.add_patch(feedback_box)
    ax.text(6.9, 0.78, "🔄 Continuous Feedback & MLOps Loop: Model Drift Detection -> Automated Retraining Trigger -> Dynamic Retargeting",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1E40AF', fontfamily='sans-serif')

    ax.set_xlim(-0.2, 14.0)
    ax.set_ylim(0.0, 7.0)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def create_timeline_gantt(output_path):
    """Generate 32.5-Hour Project Timeline Gantt Chart."""
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    
    tasks = [
        {"name": "Phase 1: Problem Definition & Architecture Design", "start": 0.0, "duration": 4.0, "hours": "4.0 hrs", "color": "#1E3A8A"},
        {"name": "Phase 2: Data Sourcing, Ingestion & Schema Synthesis", "start": 4.0, "duration": 5.0, "hours": "5.0 hrs", "color": "#0284C7"},
        {"name": "Phase 3: Data Cleaning, Preprocessing & EDA", "start": 9.0, "duration": 6.5, "hours": "6.5 hrs", "color": "#0D9488"},
        {"name": "Phase 4: Feature Engineering & Selection Pipeline", "start": 15.5, "duration": 5.5, "hours": "5.5 hrs", "color": "#D97706"},
        {"name": "Phase 5: Model Development, Baselines & Hyper-tuning", "start": 21.0, "duration": 6.5, "hours": "6.5 hrs", "color": "#7C3AED"},
        {"name": "Phase 6: Evaluation, SHAP Explainability & Final Delivery", "start": 27.5, "duration": 5.0, "hours": "5.0 hrs", "color": "#E11D48"}
    ]
    
    y_pos = np.arange(len(tasks))
    
    for i, task in enumerate(tasks):
        # Background track
        ax.barh(i, 35.0, left=0, height=0.55, color='#F1F5F9', edgecolor='none')
        # Active bar
        bar = ax.barh(i, task['duration'], left=task['start'], height=0.55, 
                      color=task['color'], edgecolor='#0F172A', linewidth=0.5, alpha=0.92)
        # Hour label inside/beside bar
        ax.text(task['start'] + task['duration']/2, i, task['hours'], 
                ha='center', va='center', color='#FFFFFF', fontweight='bold', fontsize=9.5, fontfamily='sans-serif')
        # End hour milestone marker
        ax.plot(task['start'] + task['duration'], i, marker='D', markersize=6, color='#0F172A')

    # Total hours summary badge
    total_hours_box = patches.FancyBboxPatch((24.0, 5.7), 10.5, 0.8,
                                            boxstyle="round,pad=0.05,rounding_size=0.1",
                                            facecolor='#EFF6FF', edgecolor='#1D4ED8', linewidth=1.5)
    ax.add_patch(total_hours_box)
    ax.text(29.25, 6.1, "Total Allocated Work: 32.5 Hours", 
            ha='center', va='center', fontsize=10, fontweight='bold', color='#1E40AF')

    ax.set_yticks(y_pos)
    ax.set_yticklabels([t['name'] for t in tasks], fontsize=10, fontweight='bold', color='#1E293B', fontfamily='sans-serif')
    ax.invert_yaxis()  # Top-down order
    
    ax.set_xlabel("Cumulative Project Hours (Total Budget: 30 - 35 Hours)", fontsize=11, fontweight='bold', color='#334155', labelpad=10)
    ax.set_xlim(-0.5, 36.0)
    ax.set_xticks(np.arange(0, 36, 5))
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#94A3B8')
    
    # Title
    plt.title("OmniPulse Data Science Project Work Breakdown & Timeline Schedule\n(Structured 32.5-Hour Implementation Roadmap)", 
              fontsize=14, fontweight='bold', color='#0F172A', pad=18)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def create_model_evaluation_diagram(output_path):
    """Generate Model Evaluation & Cost-Benefit Framework Diagram."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    
    # --- Subplot 1: Technical Metrics vs Thresholds ---
    ax1.set_facecolor('#F8FAFC')
    metrics = ['Precision (Churn)', 'Recall (Churn)', 'F1-Score', 'ROC-AUC', 'PR-AUC', 'Brier Score (Calib)']
    baseline_scores = [0.45, 0.52, 0.48, 0.68, 0.40, 0.22]
    target_scores =   [0.72, 0.81, 0.76, 0.88, 0.75, 0.08]
    
    y = np.arange(len(metrics))
    width = 0.35
    
    ax1.barh(y - width/2, baseline_scores, width, label='Baseline (Logistic Regression)', color='#94A3B8', alpha=0.85)
    ax1.barh(y + width/2, target_scores, width, label='Target (Tuned LightGBM/XGBoost)', color='#0284C7', alpha=0.95)
    
    for i in range(len(metrics)):
        ax1.text(baseline_scores[i] + 0.02, y[i] - width/2, f"{baseline_scores[i]:.2f}", va='center', fontsize=8.5, color='#475569')
        ax1.text(target_scores[i] + 0.02, y[i] + width/2, f"{target_scores[i]:.2f}", va='center', fontsize=8.5, fontweight='bold', color='#0369A1')
        
    ax1.set_yticks(y)
    ax1.set_yticklabels(metrics, fontsize=9.5, fontweight='bold', color='#1E293B')
    ax1.set_xlim(0, 1.05)
    ax1.set_xlabel("Performance Metric Score (0.0 to 1.0)", fontsize=10, fontweight='bold', color='#334155')
    ax1.set_title("A. Technical Metric Benchmarks", fontsize=12, fontweight='bold', color='#0F172A', pad=12)
    ax1.legend(loc='lower right', frameon=True, facecolor='#FFFFFF')
    ax1.grid(axis='x', linestyle=':', alpha=0.6)

    # --- Subplot 2: Financial Cost-Benefit Matrix ---
    ax2.set_facecolor('#F8FAFC')
    ax2.axis('off')
    
    # Title
    ax2.text(0.5, 0.95, "B. Business Cost-Benefit Matrix (Expected Value Framework)", 
             ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A')
    
    # 2x2 Matrix visualization
    # TP
    card_tp = patches.FancyBboxPatch((0.05, 0.50), 0.42, 0.35, boxstyle="round,pad=0.03", facecolor='#ECFDF5', edgecolor='#059669', linewidth=2)
    ax2.add_patch(card_tp)
    ax2.text(0.26, 0.77, "TRUE POSITIVE (TP)\nTargeted Retention Success", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#065F46')
    ax2.text(0.26, 0.60, "• Customer Saved: +$180 CLV\n• Retention Offer: -$25 Cost\n• Net Profit: +$155 / user", ha='center', va='center', fontsize=8.5, color='#047857')

    # FP
    card_fp = patches.FancyBboxPatch((0.53, 0.50), 0.42, 0.35, boxstyle="round,pad=0.03", facecolor='#FFFBEB', edgecolor='#D97706', linewidth=2)
    ax2.add_patch(card_fp)
    ax2.text(0.74, 0.77, "FALSE POSITIVE (FP)\nUnnecessary Incentive", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#92400E')
    ax2.text(0.74, 0.60, "• User would have stayed\n• Wasted Voucher: -$25 Cost\n• Net Impact: -$25 / user", ha='center', va='center', fontsize=8.5, color='#B45309')

    # FN
    card_fn = patches.FancyBboxPatch((0.05, 0.08), 0.42, 0.35, boxstyle="round,pad=0.03", facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax2.add_patch(card_fn)
    ax2.text(0.26, 0.35, "FALSE NEGATIVE (FN)\nCatastrophic Missed Churn", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#991B1B')
    ax2.text(0.26, 0.18, "• Model predicted retention\n• Customer churns away\n• Lost Revenue: -$180 CLV", ha='center', va='center', fontsize=8.5, color='#B91C1C')

    # TN
    card_tn = patches.FancyBboxPatch((0.53, 0.08), 0.42, 0.35, boxstyle="round,pad=0.03", facecolor='#F1F5F9', edgecolor='#64748B', linewidth=2)
    ax2.add_patch(card_tn)
    ax2.text(0.74, 0.35, "TRUE NEGATIVE (TN)\nOrganic Loyal Customer", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#334155')
    ax2.text(0.74, 0.18, "• Healthy active user\n• No marketing intervention\n• Net Cost: $0 (Baseline)", ha='center', va='center', fontsize=8.5, color='#475569')

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

def create_tech_stack_diagram(output_path):
    """Generate Python Data Science Tooling Ecosystem Diagram."""
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    
    categories = [
        {"cat": "1. Data Processing\n& Storage", "tools": "• Pandas (DataFrames)\n• NumPy (Vectorization)\n• SQLAlchemy / PostgreSQL\n• PyArrow / Parquet", "color": "#0284C7"},
        {"cat": "2. Exploratory EDA\n& Visualization", "tools": "• Matplotlib & Seaborn\n• Plotly (Interactive)\n• Missingno (Null audit)\n• YData Profiling", "color": "#0D9488"},
        {"cat": "3. Feature Eng. &\nPre-processing", "tools": "• Scikit-learn Pipelines\n• Imbalanced-learn (SMOTE)\n• Category Encoders\n• Feature-engine", "color": "#D97706"},
        {"cat": "4. Modeling &\nHyper-tuning", "tools": "• XGBoost & LightGBM\n• Scikit-Learn Classifiers\n• Optuna (Bayesian Tune)\n• CatBoost", "color": "#7C3AED"},
        {"cat": "5. Explainability &\nModel Governance", "tools": "• SHAP (TreeExplainer)\n• LIME (Local surrogate)\n• MLflow (Experiment Run)\n• Evidently AI (Drift)", "color": "#E11D48"},
        {"cat": "6. Deployment &\nDelivery Layer", "tools": "• FastAPI (REST Engine)\n• Docker (Container)\n• Pydantic (Type schema)\n• Streamlit (Dashboard)", "color": "#334155"}
    ]
    
    ax.text(6.5, 5.8, "OmniPulse Python Data Science Tooling & Technology Stack", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0F172A', fontfamily='sans-serif')
    ax.text(6.5, 5.3, "Curated Open-Source Python Ecosystem for Scalable Machine Learning", 
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#64748B', fontfamily='sans-serif')

    width = 1.9
    height = 4.2
    
    for i, cat in enumerate(categories):
        x = 0.35 + i * 2.1
        y = 0.6
        
        # Shadow
        shadow = patches.FancyBboxPatch((x + 0.04, y - 0.04), width, height,
                                        boxstyle="round,pad=0.06,rounding_size=0.12",
                                        facecolor='#E2E8F0', edgecolor='none')
        ax.add_patch(shadow)
        
        # Main Box
        box = patches.FancyBboxPatch((x, y), width, height,
                                     boxstyle="round,pad=0.06,rounding_size=0.12",
                                     facecolor='#FFFFFF', edgecolor=cat['color'], linewidth=2)
        ax.add_patch(box)
        
        # Header Badge
        badge = patches.FancyBboxPatch((x + 0.05, y + height - 0.95), width - 0.1, 0.85,
                                       boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor=cat['color'], edgecolor='none')
        ax.add_patch(badge)
        
        ax.text(x + width/2, y + height - 0.52, cat['cat'], 
                ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF', fontfamily='sans-serif')
        
        ax.text(x + 0.15, y + height - 1.3, cat['tools'], 
                ha='left', va='top', fontsize=8.8, color='#334155', fontfamily='sans-serif', linespacing=1.6)

    ax.set_xlim(0, 13.0)
    ax.set_ylim(0, 6.4)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    create_methodology_flowchart(os.path.join(assets_dir, "ds_methodology_flowchart.png"))
    create_timeline_gantt(os.path.join(assets_dir, "project_timeline_gantt.png"))
    create_model_evaluation_diagram(os.path.join(assets_dir, "model_evaluation_framework.png"))
    create_tech_stack_diagram(os.path.join(assets_dir, "python_tech_stack_ecosystem.png"))
    print("All diagrams generated successfully.")

#!/usr/bin/env python3
"""Generate a Delegate & Elevate pie chart."""
import argparse, json, sys
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
except ImportError:
    print("pip3 install matplotlib"); sys.exit(1)

COLORS = {"Q1":"#2E7D32","Q2":"#1565C0","Q3":"#EF6C00","Q4":"#C62828"}
NAMES = ["Q1: Love It & Great At It","Q2: Like It & Good At It","Q3: Don't Like & Good At It","Q4: Don't Like & Not Good At It"]
TARGETS = {"Q1":80,"Q2":15,"Q3":5,"Q4":0}

def build_chart(hours, title, output, details=None):
    total = sum(hours.values())
    if total == 0: print("Error: 0 hours"); sys.exit(1)
    sizes = [hours[f"Q{i+1}"] for i in range(4)]
    pcts = [h/total*100 for h in sizes]
    colors = [COLORS[f"Q{i+1}"] for i in range(4)]
    fig, ax = plt.subplots(figsize=(10,8))
    wedges, texts, autotexts = ax.pie(sizes, labels=None,
        autopct=lambda p: f"{p:.1f}%\n({p*total/100:.0f}h)" if p > 0 else "",
        colors=colors, startangle=90, counterclock=False, pctdistance=0.65,
        wedgeprops={"edgecolor":"white","linewidth":2})
    for at in autotexts: at.set_fontsize(11); at.set_fontweight("bold"); at.set_color("white")
    ax.add_artist(plt.Circle((0,0),0.40,fc="white"))
    ax.text(0,0.06,f"{total:.0f}",ha="center",va="center",fontsize=28,fontweight="bold",color="#333")
    ax.text(0,-0.10,"total hours",ha="center",va="center",fontsize=11,color="#666")
    legend_labels = []
    for i in range(4):
        qk=f"Q{i+1}"; gap=pcts[i]-TARGETS[qk]; gs=f"+{gap:.0f}pp" if gap>=0 else f"{gap:.0f}pp"
        legend_labels.append(f"{NAMES[i]}\n  {hours[qk]:.0f}h ({pcts[i]:.1f}%) — target {TARGETS[qk]}% [{gs}]")
    patches=[mpatches.Patch(facecolor=colors[i],edgecolor="white",label=legend_labels[i]) for i in range(4)]
    ax.legend(handles=patches,loc="lower center",bbox_to_anchor=(0.5,-0.22),ncol=2,fontsize=9,frameon=True,fancybox=True)
    ax.set_title(title,fontsize=16,fontweight="bold",pad=20,color="#333")
    if pcts[0]<80:
        ax.annotate(f"Q1 Gap: {80-pcts[0]:.0f}pp to reach 80% target",xy=(0.5,-0.02),
            xycoords="axes fraction",ha="center",fontsize=10,fontstyle="italic",color=COLORS["Q3"])
    plt.tight_layout(); fig.savefig(output,dpi=150,bbox_inches="tight",facecolor="white"); plt.close(fig)
    print(f"Chart saved to {output}")
    if details:
        build_detail(hours, details, title, output.replace(".png","_detail.png"), total)

def build_detail(hours, details, title, output, total):
    all_items, bar_colors = [], []
    for qk in ["Q1","Q2","Q3","Q4"]:
        for item in details.get(qk,[]):
            if ":" in item:
                name,val=item.rsplit(":",1)
                try: h=float(val.strip().rstrip("h"))
                except: h=0
                all_items.append((f"[{qk}] {name.strip()}",h)); bar_colors.append(COLORS[qk])
    if not all_items: return
    sorted_items=sorted(all_items,key=lambda x:x[1],reverse=True)
    labels=[x[0] for x in sorted_items]; vals=[x[1] for x in sorted_items]
    lmap=dict(zip([x[0] for x in all_items],bar_colors))
    sc=[lmap[l] for l in labels]
    fig,ax=plt.subplots(figsize=(12,max(8,len(labels)*0.4+2)))
    ax.barh(range(len(labels)),vals,color=sc,edgecolor="white",height=0.7)
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels,fontsize=9); ax.invert_yaxis()
    ax.set_xlabel("Hours",fontsize=11)
    ax.set_title(f"{title} — Function Breakdown",fontsize=14,fontweight="bold",pad=15)
    for i,v in enumerate(vals): ax.text(v+0.3,i,f"{v:.0f}h",va="center",fontsize=9,color="#333")
    plt.tight_layout(); fig.savefig(output,dpi=150,bbox_inches="tight",facecolor="white"); plt.close(fig)
    print(f"Detail chart saved to {output}")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--q1",type=float,required=True); p.add_argument("--q2",type=float,required=True)
    p.add_argument("--q3",type=float,required=True); p.add_argument("--q4",type=float,required=True)
    p.add_argument("--title",default="Delegate & Elevate Time Audit")
    p.add_argument("--output",default="/tmp/de_audit_pie_chart.png")
    p.add_argument("--details",type=str,default=None)
    a=p.parse_args()
    hours={"Q1":a.q1,"Q2":a.q2,"Q3":a.q3,"Q4":a.q4}
    build_chart(hours,a.title,a.output,json.loads(a.details) if a.details else None)

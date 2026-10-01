"""Generate project diagrams and PDF guides using matplotlib and reportlab."""
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
ROOT=Path(__file__).resolve().parents[1]
def diagram(name,title,nodes,edges):
    fig,ax=plt.subplots(figsize=(11,8));ax.set_xlim(0,11);ax.set_ylim(0,8);ax.axis('off');ax.set_title(title,fontsize=18,color='#10243a',pad=20)
    for a,b in edges:
        x,y,_=nodes[a];u,v,_=nodes[b];ax.annotate('',xy=(u,v+.36),xytext=(x,y-.36),arrowprops=dict(arrowstyle='->',color='#64748b',lw=1.4),zorder=1)
    for x,y,label in nodes.values():
        ax.add_patch(FancyBboxPatch((x-1.22,y-.36),2.44,.72,boxstyle='round,pad=.06',facecolor='#e5f3f2',edgecolor='#0d9488',zorder=2));ax.text(x,y,label,ha='center',va='center',fontsize=9,color='#10243a',zorder=3)
    ax.text(.1,.1,'Synthetic portfolio project | Power BI Desktop build required',fontsize=9,color='#526477')
    for ext in ['png','svg']:fig.savefig(ROOT/f'diagrams/{name}.{ext}',dpi=160,bbox_inches='tight')
    plt.close(fig)
def build():
    (ROOT/'diagrams').mkdir(exist_ok=True)
    diagram('workflow','Data processing and reporting workflow',{'raw':(5.5,7,'Raw campaign CSV'),'clean':(5.5,5.8,'Clean and validate'),'q':(9,4.6,'Quarantine CSV'),'accepted':(5.5,4.6,'Clean campaign CSV'),'sql':(2,3.3,'SQLite and SQL'),'py':(5.5,3.3,'Python analysis'),'bi':(9,3.3,'Excel / Power BI\nsource imports'),'check':(2,2,'Reconcile SQL / Python'),'dash':(5.5,2,'Charts and offline HTML'),'report':(5.5,.8,'Report and recommendations')},[('raw','clean'),('clean','q'),('clean','accepted'),('accepted','sql'),('accepted','py'),('accepted','bi'),('sql','check'),('py','check'),('py','dash'),('check','report'),('dash','report'),('bi','report')])
    diagram('kpi_dependencies','Revenue, costs and KPI dependencies',{'revenue':(2,7,'Attributed revenue'),'margin':(5.5,7,'Assumed margin 55%'),'spend':(9,7,'Marketing spend'),'contrib':(3.8,5.3,'Contribution before\nmarketing'),'net':(5.5,3.5,'Net contribution'),'roi':(5.5,1.6,'ROI = net / spend'),'roas':(1.6,1.6,'ROAS = revenue / spend'),'cpa':(9,1.6,'CPA = spend / acquisitions'),'acq':(9,3.5,'Attributed acquisitions')},[('revenue','contrib'),('margin','contrib'),('contrib','net'),('spend','net'),('net','roi'),('spend','roi'),('revenue','roas'),('spend','roas'),('spend','cpa'),('acq','cpa')])
    diagram('project_structure','Project structure and responsibilities',{'root':(5.5,7,'marketing-roi'),'data':(1.5,5.3,'data / sql'),'code':(4.2,5.3,'src / notebooks'),'report':(6.9,5.3,'excel / powerbi / outputs'),'docs':(9.6,5.3,'docs / diagrams'),'d1':(1.5,3.3,'Raw, clean, quarantine\nSQL queries'),'c1':(4.2,3.3,'Pipeline, HTML template\nEDA notebook'),'r1':(6.9,3.3,'Workbook, DAX, theme\nDatabase, charts, HTML'),'g1':(9.6,3.3,'Guides, reports, PDFs\nSVG and PNG diagrams'),'delivery':(5.5,1.3,'GitHub repository\nand complete ZIP bundle')},[('root','data'),('root','code'),('root','report'),('root','docs'),('data','d1'),('code','c1'),('report','r1'),('docs','g1'),('d1','delivery'),('c1','delivery'),('r1','delivery'),('g1','delivery')])
    styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyProject',fontName='Helvetica',fontSize=10,leading=15,spaceAfter=10,textColor=colors.HexColor('#24364b')));styles['Title'].textColor=colors.HexColor('#10243a');styles['Heading2'].textColor=colors.HexColor('#0d817b');styles['Heading2'].spaceBefore=15
    def footer(c,d):
        c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#526477'));c.drawString(44,26,'Marketing ROI Analytics | Synthetic portfolio project');c.drawRightString(550,26,str(d.page))
    def md(path):
        story=[]
        for block in path.read_text().split('\n\n'):
            block=block.strip().replace('—','-').replace('−','-')
            if not block:continue
            if block.startswith('# '):style=styles['Title'];block=block[2:]
            elif block.startswith('## '):
                head,_,body=block.partition('\n');story.append(Paragraph(escape(head[3:]),styles['Heading2']))
                if body:story.append(Paragraph(escape(body).replace('\n','<br/>'),styles['BodyProject']))
                continue
            else:style=styles['BodyProject']
            story.append(Paragraph(escape(block).replace('\n','<br/>'),style))
        return story
    guide=md(ROOT/'docs/COMPLETE_PROJECT_GUIDE.md')
    for name,title in [('workflow','Workflow diagram'),('kpi_dependencies','KPI dependency diagram'),('project_structure','Project structure diagram')]:guide.extend([PageBreak(),Paragraph(title,styles['Title']),Image(str(ROOT/f'diagrams/{name}.png'),width=490,height=360)])
    guide.extend([PageBreak(),Paragraph('Dashboard reference',styles['Title']),Image(str(ROOT/'outputs/dashboard.png'),width=490,height=302),Spacer(1,15),Paragraph('Open outputs/dashboard.html for the interactive version. These charts reflect synthetic data and designed channel assumptions.',styles['BodyProject'])])
    for name,story in [('Marketing_ROI_Complete_Guide.pdf',guide),('Marketing_Campaign_ROI_Project_Report.pdf',md(ROOT/'docs/FINAL_REPORT.md'))]:SimpleDocTemplate(str(ROOT/'docs'/name),pagesize=(595.28,841.89),rightMargin=44,leftMargin=44,topMargin=42,bottomMargin=52,title=name.replace('_',' '),author='Kavali Harshavardhan').build(story,onFirstPage=footer,onLaterPages=footer)
    print('Generated three diagram pairs and two PDFs')
if __name__=='__main__':build()

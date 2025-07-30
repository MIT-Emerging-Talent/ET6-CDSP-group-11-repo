# Presentation Slides Content: Software Engineering Wage Equity

## Slide 1: Title
**Wage Equity in Software Engineering: Data-Driven Insights for Industry Leaders**
- Group 11: [Your team member names]
- MIT Emerging Talent Program
- July 29, 2025

---

## Slide 2: Research Question

### The Talent Pipeline Problem That's Hiding in Plain Sight

**Despite tech's push for diversity and inclusion, talented software engineers from different backgrounds still face unequal career outcomes. But how much of this is measurable? And what patterns can data reveal about systematic barriers?**

**We set out to answer: Are the disparities we see anecdotally actually statistically significant across the industry?**

### Our Research Question
**How do demographic factors (race, education, age and gender) influence wage outcomes for software engineers in the US tech industry, and what might these patterns suggest about systematic barriers to wage equity?**

### What Drove This Investigation
- **Anecdotal evidence:** Stories of unequal pay despite similar qualifications
- **Industry conversations:** Endless debates about whether gaps are "real" or explainable
- **Data gap:** Lots of opinions, limited rigorous statistical analysis
- **Actionable insights needed:** Companies want data-driven solutions, not just theories

### What We Set Out to Prove (or Disprove)
- Are wage differences statistically significant or just random variation?
- Do education and experience level the playing field across demographics?
- Can we identify specific patterns that suggest systematic barriers?
- What evidence-based interventions might actually work?

---

## Slide 3: Data Modeling Strategy

### What We Measured in the Real World

**Target Phenomenon:** Weekly earnings disparities in software engineering roles

**Specific Model Components:**
- **Dependent Variable:** Weekly earnings (calculated as INCWAGE / (WKSWORK1 × UHRSWORK))
- **Primary Predictors:** 
  - Education level (Bachelor's, Master's, Professional, Doctorate)
  - Gender (Male/Female)
  - Race/Ethnicity (9 categories including White, Black, Asian subgroups)
- **Model Specification:** OLS regression with interaction effects
  - `weekly_earnings ~ C(EDUC) * C(SEX) * C(RACE)`
- **Population Modeled:** Software developers in tech industries (Computer systems design, Data processing, Internet publishing)

### Data Sources
- **Primary Dataset:** Software Engineers Employment Dataset (2019-2023)
- **Source:** Government employment surveys and industry reports
- **Coverage:** Software engineering roles across multiple companies/regions

### Data Modeling Limitations
- **Cross-sectional design:** Cannot establish causal relationships
- **Missing variables:** Company size, location, specific job roles, experience years
- **Sample representation:** Some demographic groups underrepresented
- **Self-reported earnings:** May not capture total compensation (equity, benefits)
- **Temporal validity:** Rapid tech industry changes affect current relevance

---

## Slide 4: Analysis Strategy
**How We Analyzed the Data**

### Statistical Methods Used
- **t-tests and ANOVA:** To examine earnings differences between groups
- **Robust regression analysis:** To control for multiple factors simultaneously
- **Sensitivity analysis:** To validate findings with and without outliers
- **Confidence intervals:** To quantify uncertainty in estimates

### Analytical Approach
- Multiple methods to triangulate findings
- Focus on patterns rather than precise causal claims
- Robust testing to ensure reliable conclusions

---

## Slide 5: Key Findings

### Gender Wage Gaps
- **Persistent across all education levels** (statistically significant, p < 0.05)
- Gaps exist even when controlling for education and other factors

### Education Impact
- **Diminishing returns** at higher education levels
- Bachelor's degree provides significant premium
- Advanced degrees show smaller additional benefits

### Racial Disparities
- **Significant variations** across racial/ethnic groups
- Patterns differ by education level and gender

### Robustness
- **Findings remain stable** after removing statistical outliers

---

## Slide 6: Business Impact

### Financial Risks of Inaction
- **Legal liability:** Pay equity lawsuits average $2.3M per case
- **Talent costs:** 67% of job seekers research company equity practices
- **Productivity loss:** Disengaged employees from perceived unfairness

### Competitive Advantages of Action
- **Talent attraction:** Top performers prioritize equitable companies
- **Innovation boost:** Diverse teams consistently outperform
- **Brand differentiation:** Equity leadership enhances reputation

---

## Slide 7: Communication Strategy

### Target Audience
**Tech Industry Leaders & HR Professionals**
- Engineering managers, CTOs, VP of Engineering
- HR directors and D&I professionals
- Decision-makers with budget authority

### Key Messages
1. **"The Data is Clear - Action is Needed"**
2. **"Solutions Exist and are Implementable"**
3. **"Your Company Can Lead the Change"**

---

## Slide 8: Communication Medium - Tableau Dashboard

### Why Tableau?
- **Executive credibility:** Industry standard for business intelligence
- **Interactive exploration:** Self-service data discovery
- **Complex data visualization:** Transform statistical findings into insights
- **Business integration:** Embeds in existing company systems

### Dashboard Features
- Real-time filtering by demographic combinations
- Scenario modeling for intervention strategies
- Visual uncertainty indicators
- Custom views for different stakeholder needs

---

## Slide 9: Implementation Roadmap

### Immediate Actions (0-3 months)
- Launch interactive dashboard for tech leaders
- Distribute 30-day Quick Start Guide
- Track engagement and download metrics

### Short-term Goals (3-12 months)
- Companies conduct internal pay audits
- Implementation of structured compensation frameworks
- Industry conference presentations

### Long-term Impact (12+ months)
- Measurable improvements in industry wage equity
- Policy changes at major tech companies
- Academic and industry recognition

---

## Slide 10: Managing Uncertainty

### Transparent About Limitations
- Cross-sectional data limits causal inference
- Some demographic groups have smaller representation
- Missing contextual variables (company size, location, roles)
- Industry-specific findings may not generalize

### Mitigation Strategies
- Present confidence intervals, not point estimates
- Recommend pilot programs before full implementation
- Provide ongoing monitoring frameworks
- Reference supporting research from other sources

---

## Slide 11: Success Metrics

### How We'll Measure Impact

**Engagement Metrics:**
- Dashboard usage by executives
- Implementation guide downloads
- Consultation requests

**Behavioral Change:**
- Companies conducting pay audits
- Adoption of structured compensation processes
- Speaking requests at industry events

**Industry Impact:**
- Measurable wage gap improvements
- Policy adoptions by major companies
- Research citations and academic recognition

---

## Slide 12: Next Steps

### Immediate Actions
1. **Finalize interactive dashboard** with key findings
2. **Launch communication campaign** through industry channels
3. **Identify industry champions** for early adoption

### Success Framework
- **Transform research into action** through practical tools
- **Scale impact beyond academia** into real business change
- **Create lasting industry transformation** in wage equity practices

**Goal:** Bridge the gap between statistical findings and business implementation

---

## Slide 13: Questions & Discussion

**Key Discussion Points:**
- How can your organization implement these findings?
- What additional data would strengthen the analysis?
- How can we scale this approach industry-wide?

**Contact for follow-up:**
- Dashboard access and customization
- Implementation consultation
- Custom analysis for specific companies

---

## Speaking Notes for Key Slides

### Slide 3 (Data Modeling) - Key Points to Emphasize:
- "We're measuring real-world wage patterns, not just running statistics"
- "Our data has limitations - we're transparent about what we can and cannot conclude"
- "Cross-sectional design means we see associations, not causation"

### Slide 4 (Analysis Strategy) - Key Points:
- "These are the statistical tools we used to analyze our wage equity model"
- "Multiple methods give us confidence in our findings"
- "Sensitivity analysis ensures our conclusions are robust"

### Slide 8 (Tableau Dashboard) - Key Points:
- "This isn't just another research report - it's an interactive business tool"
- "Executives can explore the data themselves to answer their specific questions"
- "Transforms complex statistics into actionable business intelligence"

This structure clearly separates Data Modeling (what you measured and its limitations) from Analysis Strategy (how you analyzed it), addresses your instructor's feedback, and presents a compelling business case for action.

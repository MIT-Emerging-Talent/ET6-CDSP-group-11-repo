# Variable Definitions: Software Engineer Earnings Dataset

This file summarizes the key variables selected from the IPUMS USA extract used
for our analysis. For full metadata, refer to the
[official IPUMS codebook (XML)](https://live.usa.datadownload.ipums.org/web/extracts/usa/2599142/usa_00002.xml?jwt=eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ1bWEiLCJleHAiOjE3NTI3MDU5MDMsIm5iZiI6MTc1MjcwNTAwMywic3ViIjoiZGE5YjFkNDAtMzdkMi0wMTNlLWRhNzgtMDI0MjBhMWMwMzA2IiwiY29sbGVjdGlvbnMiOlsidXNhIl19.cOxsBmJXe5MfjIxegAh-TWZTL4vqsqdP7N_vLJuikxskbvgnaM16n5zIZ9KouRwbjIsWzeUsxEXnUYKxcEnXWf7_PjEuTM291N4wnYr_mVyZTkGwP3oQFDVpaKKSzfj4qaG_RDlxA8NWpeCqnmJPrYGu4xQixhpGa79-m26wkaDoQYzH8nNZom1Z5LdhGcq9cxZy-cKpUgZ97FrrgKfXJnH78-LDXBkM-UI_dER_7tBTLKjrDkWHwMpI6BBffBHCy-LP-25rxe3yvcjcAAPciVTNYcFm2Ke62_bWReHIUwO44H_Lh7kvdi2KuAlpFgMR0LvTXUwgvr22Na-1mhB9Iw).

---

## Selected Variables and Their Descriptions

- **OCC2010** : **Occupation** (2010 Census classification). We filtered this for
*1106: Software Developers, Applications and Systems Software*.
- **IND** :**Industry** (Census 2017 industry codes). We filtered for
tech-related industries:

  - 7270 (Computer systems design)
  - 7370 (Data processing/hosting)
  - 7380 (Internet publishing/web portals)  
  - 7390 (Other information services).

- **INCWAGE** : Total **annual income from wages/salary**.
- **WKSWORK1** : **Weeks worked** in the past year. Used to normalize income
to weekly figures.
- **UHRSWORK** : **Usual hours worked per week**. Also used to compute weekly
earnings.
- **EMPSTAT** : **Employment status**. We filter for *1: Employed*.
- **SEX** : **Sex** of the respondent. *1 = Male, 2 = Female*.
- **AGE** : **Age** in years.
- **RACE** : **Race** (recoded into broad categories):  
  - 1 = White  
  - 2 = Black  
  - 3 = American Indian or Alaska Native  
  - 4 = Chinese  
  - 5 = Japanese  
  - 6 = Other Asian or Pacific Islander  
  - 7 = Other race  
  - 8 = Two major races  
  - 9 = Three or more major races
- **EDUC** : **Educational attainment**:  
  - 61 = Bachelor’s degree  
  - 65 = Master’s degree  
  - 71 = Professional school degree  
  - 81 = Doctorate degree  
(Other values include high school, some college, etc.)
- **CLASSWKR** : **Class of worker** (e.g., private wage/salary, government,
self-employed). Optional use for deeper segmentation.

---

## Derived Variables

- **weekly_earnings** : Calculated field:  
- **weekly_earnings** = INCWAGE / (WKSWORK1 * UHRSWORK)
Estimates the respondent’s average weekly income from wages,
 used as the main outcome variable.

---

## Notes

- All values are based on **self-reported survey responses** from the American
Community Survey (ACS).
- Variable codes (e.g., for *EDUC, RACE*) can be mapped to human-readable
labels using the IPUMS codebook or directly in your cleaning script.

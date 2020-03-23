jernames=[
"JEReta0pt0Up",
"JEReta1pt0Up",
"JEReta2pt0Up",
"JEReta3pt0Up",
"JEReta2pt1Up",
"JEReta3pt1Up",
"JEReta0pt0Down",
"JEReta1pt0Down",
"JEReta2pt0Down",
"JEReta3pt0Down",
"JEReta2pt1Down",
"JEReta3pt1Down",
]


if False : #split in match vs nomatch
  jerUponly=[x for x in jernames if "Up" in x]
  jernames=[]
  for suffix in ["MatchUp","MatchDown","NotMatchUp","NotMatchDown"] :
	  jernames+=[x[:-2]+suffix for x in jerUponly]

print "JERNAMES"
print jernames

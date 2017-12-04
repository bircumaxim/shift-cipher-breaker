# Shift cipher breaker

There are 2 methods of cipher braker one based on Frequnecy analyses and one based on a simple dictionary Hack. 
For dictionary was used Enchant library in order to change the language just simply install it and change the parameter 
at dictionary loading, now it's "en-US"

### Simple Dictionary hack
This method step by step shifts with one character to the right the content and save all decryptions in a dictionary, 
for each version of decrypted message it's the number of words that exists and I case when we chive the same number of 
words as in cryptogram then we break. And at the end we simply should get the solution with the most words existing.


### Frequency analysis
This method is based on the letters frequency in a specific language, I hardcoded a dictionary with english latters 
order descending starting with the most frequent and so on. Then I simply compute frequency for all letters from the 
cryptogram and also save int a dictionary and ordered descending by frequency, after all I simply take one by one 
letters from the dictionary with letter frequencies of the cryptogram and one by one letters from the english letters 
frequency dictionary and compute the delta between them and try to shift with that delta the cryptogram, compute how
much existing words there are in each result and save all this stuff into a dictionary 
And at the end we simply should get the solution with the most words existing.


## Let's see how we decrypt some messages :)

Deadline

AB ZNRL MAX WXTWEBGX YHK MABL ETUHKTMHKR BL MAX MPXGMBXMA HY WXVXFUXK B PHNEW EBDX 
MH PBLA RHN ZHHW ENVD PBMA BM TGW ATOX T GBVX EBYX

Key:7 <br/>
Message: hi guys the deadline for this laboratory is the twentieth of december i would like to wish you good luck with it and have a nice life

Message 1

WKHSWEC: WI XKWO SC WKHSWEC NOMSWEC WOBSNSEC, MYWWKXNOB YP DRO KBWSOC YP DRO XYBDR, 
QOXOBKV YP DRO POVSH VOQSYXC, VYIKV COBFKXD DY DRO DBEO OWZOBYB, WKBMEC KEBOVSEC. PKDROB DY K 
WEBNOBON CYX, RECLKXN DY K WEBNOBON GSPO. KXN S GSVV RKFO WI FOXQOKXMO, SX DRSC VSPO YB DRO XOHD.

Key:-10 <br/>
Message: maximus my name is maximus decimus meridius commander of the armies of the north general of the felix legions loyal servant to the true emperor marcus aurelius father to a murdered son husband to a murdered wife and i will have my vengeance in this life or the next


Message 2

XOXKR IETG BL MH UX VHGLBWXKXW, XOXKR XQIXWBXGM MKBXW TGW XOXKR FXMAHW MTDXG UXYHKX 
FTMMXKL TKX UKHNZAM MH MABL ETLM XQMKXFBMR. ZHHW HYYBVXKL WXVEBGX ZXGXKTE XGZTZXFXGML 
PAXKX MAX HWWL TKX MHH ZKXTM, TGW IKXYXK MAX XFIEHRFXGM HY LMKTMTZXF TGW YBGXLLX 
MH WXLMKHR MAX XGXFR TL FNVA TL IHLLBUEX PBMAHNM XQIHLBGZ MAXBK HPG YHKVXL.

Key:7 <br/>
Message: every plan is to be considered every expedient tried and every method taken before matters are brought to this last extremity good officers decline general engagements where the odds are too great and prefer the employment of stratagem and finesse to destroy the enemy as much as possible without exposing their own forces



Message 3

RD QTAJ KTW YMJ WTRFS JRUNWJ NX ZSIJSNFGQD LWJFYJW YMFS KTW RDXJQK. YMJ LWJFYJXY 
JRUNWJ JAJW YT MFAJ JCNXYJI. N UQJILJ RD JYJWSFQ XJWANYZIJ FSI N FR KTWJAJW GTZSI 
YT XJWAJ NY, NS QNKJ FSI NS IJFYM. YMJD MFAJ RJWJQD LNAJS ZX: WTFIX, HJSYWFQ 
MJFYNSL, HTSHWJYJ, YMJ HFQJSIFW, FSI KQZXMNSL YTNQJYX FSI XJBJWX.

Key:-5 <br/>
Message: my love for the roman empire is undeniably greater than for myself the greatest empire ever to have existed i pledge my eternal servitude and i am forever bound to serve it in life and in death they have merely given us roads central heating concrete the calendar and flushing toilets and sewers




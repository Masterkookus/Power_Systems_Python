import numpy as np

curvetype = ['1-102','2-135','3-140','4-106','5-114','6-136','7-152','8-113',
             '9-131','11-141','13-142','14-119','15-112','16-139','17-103',
             '18-151','A-101','B-117','C-133','D-116','E-132','F-163','G-121',
             'H-122','J-164','KG-165','KP-162','L-107','M-118','N-104','P-115',
             'R-105','T-161','V-137','W-138','Y-120','Z-134','6k','8k','10k',
             '12k','15k','20k','25k','30k','40k','50k','65k','80k','100k',
             '140k','200k','6T','8T','10T','12T','15T','20T','25T','30T','40T',
             '50T','65T','80T','100T','140T','200T','Amod0','Amod1','Amod2',
             'Amod3','Bmod0','Bmod1','Bmod2','Bmod3','Cmod0','Cmod1','Cmod2',
             'Cmod3','Dmod0','Dmod1','Dmod2','Dmod3','Emod0','Emod1','Emod2',
             'Emod3','Fmod0','Fmod1','Fmod2','Fmod3','EFmod0','EFmod1',
             'EFmod2','EFmod3','KFmod0','KFmod1','KFmod2','KFmod3','Nmod0',
             'Nmod1','Nmod2','Nmod3','Rmod0','Rmod1','Rmod2','Rmod3','TFmod0',
             'TFmod1','TFmod2','TFmod3','A_H','B_H','C_H','A_4H','B_4H',
             'C_4H','A_L','B_L','C_L','D_L','def1a1s','U1','U2','U3','U4','U5','C1',
             'C2','C3','C4','C5','ITE-51E','ITE-51I','ITE-51Y','ITE-51S',
             'MICRO51-E','MICRO-I','MICRO-Y','MICRO-S','MCO-2S','MCO-5L',
             'MCO-6D','MCO-7M','MCO-8I','MCO-9Y','MCO-11E','DPU-E','DPU-I',
             'DPU-Y','DPU-S']

curvefile = ['./curves/1-102.txt','./curves/2-135.txt','./curves/3-140.txt',
             './curves/4-106.txt','./curves/5-114.txt','./curves/6-136.txt',
             './curves/7-152.txt','./curves/8-113.txt','./curves/9-131.txt',
             './curves/11-141.txt','./curves/13-142.txt','./curves/14-119.txt',
             './curves/15-112.txt','./curves/16-139.txt','./curves/17-103.txt',
             './curves/18-151.txt','./curves/A-101.txt','./curves/B-117.txt',
             './curves/C-133.txt','./curves/D-116.txt','./curves/E-132.txt',
             './curves/F-163.txt','./curves/G-121.txt','./curves/H-122.txt',
             './curves/J-164.txt','./curves/KG-165.txt','./curves/KP-162.txt',
             './curves/L-107.txt','./curves/M-118.txt','./curves/N-104.txt',
             './curves/P-115.txt','./curves/R-105.txt','./curves/T-161.txt',
             './curves/V-137.txt','./curves/W-138.txt','./curves/Y-120.txt',
             './curves/Z-134.txt','./curves/6k.txt','./curves/8k.txt',
             './curves/10k.txt','./curves/12k.txt','./curves/15k.txt',
             './curves/20k.txt','./curves/25k.txt','./curves/30k.txt',
             './curves/40k.txt','./curves/50k.txt','./curves/65k.txt',
             './curves/80k.txt','./curves/100k.txt','./curves/140k.txt',
             './curves/200k.txt','./curves/6T.txt','./curves/8T.txt',
             './curves/10T.txt','./curves/12T.txt','./curves/15T.txt',
             './curves/20T.txt','./curves/25T.txt','./curves/30T.txt',
             './curves/40T.txt','./curves/50T.txt','./curves/65T.txt',
             './curves/80T.txt','./curves/100T.txt','./curves/140T.txt',
             './curves/200T.txt','./curves/A.txt','./curves/Amod1.txt',
             './curves/Amod2.txt','./curves/Amod3.txt','./curves/B.txt',
             './curves/Bmod1.txt','./curves/Bmod2.txt','./curves/Bmod3.txt',
             './curves/C.txt','./curves/Cmod1.txt','./curves/Cmod2.txt',
             './curves/Cmod3.txt','./curves/D.txt','./curves/Dmod1.txt',
             './curves/Dmod2.txt','./curves/Dmod3.txt','./curves/E.txt',
             './curves/Emod1.txt','./curves/Emod2.txt','./curves/Emod3.txt',
             './curves/F.txt','./curves/Fmod1.txt','./curves/Fmod2.txt',
             './curves/Fmod3.txt','./curves/EF.txt','./curves/EFmod1.txt',
             './curves/EFmod2.txt','./curves/EFmod3.txt','./curves/KF.txt',
             './curves/KFmod1.txt','./curves/KFmod2.txt',
             './curves/KFmod3.txt','./curves/N.txt','./curves/Nmod1.txt',
             './curves/Nmod2.txt','./curves/Nmod3.txt','./curves/R.txt',
             './curves/Rmod1.txt','./curves/Rmod2.txt','./curves/Rmod3.txt',
             './curves/TF.txt','./curves/TFmod1.txt','./curves/TFmod2.txt',
             './curves/TFmod3.txt','./curves/H-3H-5A.txt',
             './curves/H-3H-5B.txt','./curves/H-3H-5C.txt',
             './curves/4H-6H-5A.txt','./curves/4H-6H-5B.txt',
             './curves/4H-6H-5C.txt','./curves/L-25A.txt',
             './curves/L-25B.txt','./curves/L-25C.txt','./curves/L-25D.txt',
             './curves/def1a1s.txt']

tccCoef=np.array([[0.0226,0.0104,0.02,1,0,0,0],#U1
                  [0.180,5.95,2,1,0,0,0],#U2
			   [0.0963,3.88,2,1,0,0,0],#U3
			   [0.0352,5.67,2,1,0,0,0],#U4
			   [0.00262,0.00342,0.02,1,0,0,0],#U5
			   [0,0.14,0.02,1,0,0,0],#C1
			   [0,13.5,1,1,0,0,0],#C2
			   [0,80,2,1,0,0,0],#C3
			   [0,120,1,1,0,0,0],#C4
			   [0,0.05,0.04,1,0,0,0],#C5
			   [110,17640,0.5,2,5.367,1.667,24000],#ITE-51E
			   [478,4122,0.275,1,8.544,3.444,24000],#ITE-51I
			   [310,2756,1.35,1,5.389,1.889,24000],#ITE=51Y
			   [112,735,0.58,1,5,0,24000],#ITE-51S
			   [110,17640,0.5,2,4.667,1.667,24000],#MICRO51-E
			   [478,4122,0.55,1,8.722,3.222,24000],#MICRO51-I
			   [310,2756,1.35,1,6.533,2.333,24000],#MICRO51-Y
			   [112,735,0.675,1,8.111,3.111,24000],#MICRO51-S
			   [112,735,0.675,1,0,0,24000],#MCO-2S
			   [8197,13769,1.13,1,0,0,24000],#MCO-5L
			   [785,671,1.19,1,0,0,24000],#MCO-6D
			   [525,3121,0.8,1,0,0,24000],#MCO-7M
			   [478,4122,1.27,1,0,0,24000],#MCO-8I
			   [310,2756,1.35,1,0,0,24000],#MCO-9Y
			   [110,17640,0.5,2,0,0,24000],#MCO-11E
			   [0.025,6.407,2,1,14,5,9],#DPU-E
			   [0.0185,0.0086,0.02,1,14,5,9],#DPU-I
			   [0.0712,2.855,2,1,14,5,9],#DPU-Y
			   [0.0037,0.00172,0.02,1,14,5,9]])#DPU-S
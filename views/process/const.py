nodes = {
    'nodes':[
            {
                'id':1,
                'label': 'Bait', 'color':'#c8ffa8', 
                'image':'./assets/icons/00_meat.png','shape':'image',
                'x':0, 'y':200, 'size':50
            },
            {
                'id':2,
                'label': 'Washing', 
                'image':'./assets/icons/01_lavado.svg','shape':'image', 
                'x':200, 'y':200, 'size':30
            },
            {
                'id':3,
                'label': 'Base \n Treatment', 
                'image':'./assets/icons/02_tratamiento.svg','shape':'image', 
                'x':400, 'y':200, 'size':40
            },
            {
                'id':4,
                'label': 'Acid \n Treatment', 
                'image':'./assets/icons/02_tratamiento.svg','shape':'image', 
                'x':600, 'y':200, 'size':40 
            },
            {
                'id':5,
                'label': 'Extraction',
                'image':'./assets/icons/03_extraccion.svg','shape':'image', 
                'x':800, 'y':200, 'size':50
            },
            {
                'id':6,
                'label': 'Centrifugation',
                'image':'./assets/icons/04_centrifugacion.svg','shape':'image', 
                'x':0, 'y':400, 'size':30
            },
            {
                'id':7,
                'label': 'Filtration', 
                'image':'./assets/icons/05_filtracion.svg','shape':'image',
                'x':200, 'y':400, 'size':40
            },
            {
                'id':8,
                'label': 'Ionic \n Exchange', 
                'image':'./assets/icons/06_intercambio.svg','shape':'image',
                'x':400, 'y':400, 'size':30
            },
            {
                'id':9,
                'label': 'Ultrafiltration \n UF1',
                'image':'./assets/icons/07_ultrafiltracion.svg','shape':'image', 
                'x':600, 'y':400, 'size':40
            },
            {
                'id':10,
                'label': 'Ultrafiltration \n UF2',
                'image':'./assets/icons/07_ultrafiltracion.svg','shape':'image', 
                'x':800, 'y':400, 'size':40
            },
            {
                'id':11,
                'label': 'Flash \n Evaporation', 
                'image':'./assets/icons/01_lavado.svg','shape':'image',
                'x':1000, 'y':400, 'size':40
            },
            {
                'id':12,
                'label': 'Sterilization', 
                'image':'./assets/icons/08_esterilizador.svg','shape':'image',
                'x':0, 'y':600, 'size':40
            },
            {
                'id':13,
                'label': 'Gelification', 
                'image':'./assets/icons/09_gelificacion.svg','shape':'image',
                'x':200, 'y':550, 'size':30
            },
            {
                'id':14,
                'label': 'Refrigeration', 
                'image':'./assets/icons/10_refrigeracion.svg','shape':'image',
                'x':200, 'y':650, 'size':30
            },
            {
                'id':15,
                'label': 'Drying', 
                'image':'./assets/icons/11_secador.svg','shape':'image',
                'x':400, 'y':600, 'size':40
            },
            {
                'id':16,
                'label': 'Grinding', 
                'image':'./assets/icons/12_molienda.svg','shape':'image',
                'x':550, 'y':600, 'size':40
            },
            {
                'id':17,
                'label': 'Separation \n Mixture', 
                'shape':'box',
                'x':700, 'y':600
            },
            {
                'id':18,
                'label': 'Gelatin', 'shape':'image', 'color':'#fafa8e', 
                'image':'./assets/icons/id18_gelatin.jpg',
                'x':900, 'y':600
            }, 
            {
                'id':'conn_1a', 'shape':'text', 'color':'#ffffff',
                'x': 800, 'y':320
            },
            {
                'id':'conn_1b', 'shape':'text', 'color':'#ffffff',
                'x': 0, 'y':320
            },
            {
                'id':'conector_2a', 'shape':'text', 'color':'#ffffff',
                'x': 1000, 'y':500
            },
            {
                'id':'conector_2b', 'shape':'text', 'color':'#ffffff',
                'x': 0, 'y':500
            }
        ],
        'edges':[
            {'id': '1-2', 'from':1, 'to':2, 'arrows':'to'},
            {'id': '2-3', 'from':2, 'to':3, 'arrows':'to'},

            {'id': '3-4', 'from':3, 'to':4, 'arrows':'to'},
            {'id': '4-5', 'from':4, 'to':5, 'arrows':'to'},
            
            {'id': '5-6a', 'from':5, 'to':'conn_1a', 'color':'#0341fc'},
            {'id': '5-6b', 'from':'conn_1a', 'to':'conn_1b', 
                'color':'#0341fc', 'label':'Raw \n Extract'},
            {'id': '5-6c', 'from':'conn_1b', 'to':6, 'arrows':'to', 'color':'#0341fc'},

            {'id': '6-7', 'from':6, 'to':7, 'arrows':'to'},
            {'id': '7-8', 'from':7, 'to':8, 'arrows':'to'},
            {'id': '8-9', 'from':8, 'to':9, 'arrows':'to',
            'label':'Light \n liquour'},
            {'id': '9-10', 'from':9, 'to':10, 'arrows':'to'},
            
            {'id': '10-11', 'from':10, 'to':11, 'arrows':'to'},

            {'id': '11-12a', 'from':11, 'to':'conector_2a', 'color':'#0341fc'},
            {'id': '11-12b', 'from':'conector_2a', 'to':'conector_2b', 'color':'#0341fc',
            'label':'Heavy \n liquour'},
            {'id': '11-12c', 'from':'conector_2b', 'to':12, 'arrows':'to', 'color':'#0341fc'},
            
            {'id': '12-13', 'from':12, 'to':13},
            {'id': '12-14', 'from':12, 'to':14},
            
            {'id': '13-15', 'from':13, 'to':15, 'arrows':'to'},
            {'id': '14-15', 'from':14, 'to':15, 'arrows':'to'},

            {'id': '15-16', 'from':15, 'to':16, 'arrows':'to'},
            {'id': '16-17', 'from':16, 'to':17, 'arrows':'to'},
            {'id': '17-18', 'from':17, 'to':18, 'arrows':'to'},
        ]
}

process_values=[
    {'id':1,
    'name':'Bait',
    'var': [
"RawMaterial Press",
"Carnage",
"Leather",
"Rounds",
"Hoof",
"Cowhide Leather"],
    'var_id':[
"D03_vap_press",
"D03_carnaza",
"D03_cuero",
"D03_orillo",
"D03_patica",
"D03_vaqueta"],
    'initial':[
55.0,
1.0,
1.0,
0.0,
0.0,
0.0]
    },

    {'id':5,
    'name':"Extraction",
    'var': ["ph Light Liquor",
"Total Residue All Reactors in",
"Extraction Duration h",
"Clarity Light Liquor"],
    'var_id':["D04_ph_initial_liq",
"D04_total_residue",
"D04_extract_duration",
"D04_clarity_initial_liq"],
    'initial':[2.01,
25.5,
0.0,
100.0]
    },
     {'id':8,
    'name':"Ionic Exchange",
    'var': ["Towers pH",
"pH Soda Outlet UF2"],
    'var_id':["D06_phT",
"D06_phUF2",],
    'initial':[7.872,
6.622]
    },
         {'id':11,
    'name':"Flash Evaporation",
    'var': ["Condensing Temperature",
"Liquor Temp Separator Leg",
"Heavy Liquor Temp",
"Heavy Liquor Concentration",
"Triplex A Frequency",
"Triplex B Frequency",
"Triplex D Frequency",
"Vacuum Pressure"],
    'var_id':["D09_T_condensing",
"D09_T_leg",
"D09_T_liquor",
"D09_Conc_liquor",
"D09_Tri_FrecA",
"D09_Tri_FrecB",
"D09_Tri_FrecD",
"D10_P_vaccum"],
    'initial':[2.42,
59.51,
61.6,
27.1,
26.6,
19.5,
15.3,
20.8181]
    },
    
         {'id':12,
    'name':"Sterilization",
    'var': ["Sterilization Temp",
"Water Outlet Temp"],
    'var_id':["D10_T_esteril",
"D10_T_out_water"],
    'initial':[142.0,
36.045]
    },
             {'id':14,
    'name':"Refrigeration",
    'var': ["Suction Temperature"],
    'var_id':["D11_Ts_ref"],
    'initial':[20.976]
    },
             {'id':15,
    'name':"Drying",
    'var': ["Water Exchanger Press",
"Kathene Level",
"Atomization Conditioner Press",
"Atomization Regenerator Press",
"Cambridge Filter Dropout Press",
"Conditioner Dropout Press",
"Regenerator Dropout Press",
"Air Temp A",
"Air Temp B",
"Air Temp D",
"Zone 3D Temp",
"Vapor Pressure A",
"Vapor Pressure B",
"Vapor Pressure D",
"Zone 2B Temp",
"Zone 3A Temp",
"Zone 3B Temp",
"Zone 4A Temp",
"Zone 4B Temp",
"Zone 4D Temp",
"Zone 5A Temp",
"Zone 5B Temp",
"Zone 5D Temp",
"Zone 6A Temp",
"Zone 6B Temp",
"Zone 6D Temp",
"Zone 7A Temp",
"Zone 7B Temp",
"Zone 7D Temp"],
    'var_id':["D12_P_Exch_Water",
"D12_Kath_Lvl",
"D12_P_atom_cond",
"D12_P_atom_regn",
"D12_P_filt",
"D12_P_cond",
"D12_P_regen",
"D12_TA",
"D12_TB",
"D12_TD",
"D14_3D",
"D14_vpA",
"D14_vpB",
"D14_vpD",
"D14_T2B",
"D14_T3A",
"D14_T3B",
"D14_T4A",
"D14_T4B",
"D14_T4D",
"D14_T5A",
"D14_T5B",
"D14_T5D",
"D14_T6A",
"D14_T6B",
"D14_T6D",
"D14_T7A",
"D14_T7B",
"D14_T7D"],
    'initial':[4.25,
12.025,
4.5,
0.2,
0.42,
1.8,
0.9,
37.875,
37.125,
50.025,
44.5,
40.0,
39.0,
39.5,
45.25,
50.25,
50.25,
55.25,
55.25,
49.75,
60.25,
61.25,
55.5,
60.0,
62.5,
59.25,
67.0,
69.75,
63.75]
    },
             {'id':16,
    'name':"Grinding",
    'var': ["Hydrogen Peroxide ppm",
"Sulfur Dioxide ppm",
"Clarity Light Liquor Tank1 NTU",
"Clarity Light Liquor Tank3 NTU",
"Clarity Liquor Press Filter1",
"Clarity Liquor Press Filter2",
"Clarity Liquor Press Filter4"],
    'var_id':["D05_peroxido_hid",
"D05_dioxido_azufre",
"D05_NTU_L1",
"D05_NTU_L3",
"D05_NTU_FP1",
"D05_NTU_FP2",
"D05_NTU_FP4"],
    'initial':[40.266,
12.727,
128.25,
26.666,
57.5,
29.333,
17.5]
    }

    ]
output_values=[
    {'id':'out1',
    'name':'Bloom',
    },
     {'id':'out2',
    'name':'Clarity',
    },
         {'id':'out3',
    'name':'Viscosity'
    }
    ]

modal = {}
for i in range(len(process_values)):
        modal['items_modal'+str(i+1)] = [
        {
        'id':process_values[i]['var_id'][j],  
        'label':process_values[i]['var'][j], 
        'placeholder':'input value',
        'type':'number',
        'kind':'input_text',
        'debounce':True,
        'value':process_values[i]['initial'][j],
        } for j in range(len(process_values[i]['var']))]


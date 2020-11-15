from knowledge_module.modal_specs.modal_specs import modal_specs

ns = 'viscosity'
viscosity_modal_specs = modal_specs[modal_specs['Output'] == 'viscosity']
viscosity_modal_ls = {}

for i in range(len(viscosity_modal_specs['Modal'].unique())):
    temp_specs = viscosity_modal_specs[viscosity_modal_specs['Modal'] == i+1]
    
    viscosity_modal_ls['M{}'.format(i+1)] = [
        {
            'id': '{}_input{}'.format(ns, k[1]['id']),
            'label': k[1]['label'],
            'placeholder': round(k[1]['placeholder'], 3),
            'type': k[1]['type'],
            'kind': k[1]['kind'],
            'value': round(k[1]['value'], 3),
            'debounce': k[1]['debounce']
        } for k in temp_specs.iterrows()
    ]

# Utilization
# P.ej. viscosity_modal_ls['M1']   ---> refers to Modal1

viscosity_nodes = {
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
                'x':800, 'y':200, 'size':50, 
                'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20} 
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
                'label': 'Ionic exchange', 
                'image':'./assets/icons/06_intercambio.svg','shape':'image',
                'x':400, 'y':400, 'size':30, 
                'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20} 
            },
            {
                'id':9,
                'label': 'Ultrafiltration \n UF1',
                'image':'./assets/icons/07_ultrafiltracion.svg','shape':'image', 
                'x':600, 'y':400, 'size':30, 
                'font':{'color':'black', 'background':'white'}
            },
            {
                'id':10,
                'label': 'Ultrafiltration \n UF2',
                'image':'./assets/icons/07_ultrafiltracion.svg','shape':'image', 
                'x':800, 'y':400, 'size':30
            },
            {
                'id':11,
                'label': 'Flash \n Evaporation', 
                'image':'./assets/icons/01_lavado.svg','shape':'image',
                'x':1000, 'y':400, 'size':30,
                'font':{'color':'black', 'background':'white'}
            },
            {
                'id':12,
                'label': 'Sterilization', 
                'image':'./assets/icons/08_esterilizador.svg','shape':'image',
                'x':0, 'y':600, 'size':40, 
                'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20} 
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
                'x':200, 'y':650, 'size':30, 
                'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20} 
            },
            {
                'id':15,
                'label': 'Drying', 
                'image':'./assets/icons/11_secador.svg','shape':'image',
                'x':400, 'y':600, 'size':40, 
                'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20} 
            },
            {
                'id':16,
                'label': 'Grinding', 
                'image':'./assets/icons/12_molienda.svg','shape':'image',
                'x':550, 'y':600, 'size':40,

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
            },
            {
                'id':'conector_esteril_a', 'shape':'text', 'color':'#ffffff',
                'x': 100, 'y':550
            },
            {
                'id':'conector_esteril_b', 'shape':'text', 'color':'#ffffff',
                'x': 100, 'y':650
            },
            {
                'id':19, 'shape':'text', 'color':'#ffffff',
                'x': 500, 'y':500,
                'label':'Heavy liquour', 'font':{'color':'#ffffff', 'background':'#8b2dad', 'strokeWidth':0, 'strokecolor':'black', 'size':20}
            },
        ],
        'edges':[
            {'id': '1-2', 'from':1, 'to':2, 'arrows':'to'},
            {'id': '2-3', 'from':2, 'to':3, 'arrows':'to'},

            {'id': '3-4', 'from':3, 'to':4, 'arrows':'to'},
            {'id': '4-5', 'from':4, 'to':5, 'arrows':'to'},
            
            # Connectors raw extract
            {'id': '5-6a', 'from':5, 'to':'conn_1a', 'color':'#0341fc'},
            {'id': '5-6b', 'from':'conn_1a', 'to':'conn_1b', 
                'color':{'color':'#0341fc'}, 'label':'Raw Extract', 'font':{'background':'#ffffff'}},
            {'id': '5-6c', 'from':'conn_1b', 'to':6, 'arrows':'to', 'color':{'color':'#0341fc'}},

            # Connectors light liquour
            {'id': '6-7', 'from':6, 'to':7, 'arrows':'to'},
            {'id': '7-8', 'from':7, 'to':8, 'arrows':'to'},
            {'id': '8-9', 'from':8, 'to':9, 'arrows':'to',
            'label':'Light \n liquour', 'font':{'background':'#ffffff'}},
            {'id': '9-10', 'from':9, 'to':10, 'arrows':'to'},
            {'id': '10-11', 'from':10, 'to':11, 'arrows':'to'},

            # Connectors heavy liquour
            {'id': '11-12a', 'from':11, 'to':'conector_2a', 'color':{'color':'#0341fc'}},
            {'id': '11-12b', 'from':'conector_2a', 'to':'conector_2b', 'color':{'color':'#0341fc'}},
            {'id': '11-12c', 'from':'conector_2b', 'to':12, 'arrows':'to', 'color':{'color':'#0341fc'}},
            
            # Connectors refrigeration
            {'id': '12-13a', 'from':12, 'to':'conector_esteril_a'},
            {'id': '12-13b', 'from':'conector_esteril_a', 'to':13, 'color':{'color':'#0341fc'}},
            {'id': '12-14a', 'from':12, 'to':'conector_esteril_b'},
            {'id': '12-14b', 'from':'conector_esteril_b', 'to':14, 'color':{'color':'#0341fc'}},
            
            # Conectors to drying
            {'id': '13-15', 'from':13, 'to':15, 'arrows':'to'},
            {'id': '14-15', 'from':14, 'to':15, 'arrows':'to'},

            {'id': '15-16', 'from':15, 'to':16, 'arrows':'to'},
            {'id': '16-17', 'from':16, 'to':17, 'arrows':'to'},
            {'id': '17-18', 'from':17, 'to':18, 'arrows':'to'},
        ]
}

output_values = [
    {'id': 'viscosity_out',
     'name': 'Viscosity:',
     }
]

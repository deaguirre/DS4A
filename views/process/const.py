

items_modal = [
    {
        'id':'input1', 
        'label':'Variable 1', 
        'placeholder':'Ingrese su nombre',
        'type':'text',
        'kind':'input_text'
    },
    {
        'id':'input2', 
        'label':'Variable 2', 
        'placeholder':'Ingrese su apellido',
        'type':'text',
        'kind':'input_text'
    }
]

items_modal2 = [
    {
        'id':'input3', 
        'label':'Variable 3', 
        'placeholder':'Ingrese su nombre',
        'type':'text',
        'kind':'input_text'
    },
    {
        'id':'input4', 
        'label':'Variable 4', 
        'placeholder':'Ingrese su apellido',
        'type':'text',
        'kind':'input_text'
    }
]

items_modal3 = [
    {
        'id':'input5', 
        'label':'Variable 3', 
        'placeholder':'Ingrese su nombre',
        'type':'text',
        'kind':'input_text'
    },
    {
        'id':'input6', 
        'label':'Variable 4', 
        'placeholder':'Ingrese su apellido',
        'type':'text',
        'kind':'input_text'
    }
]


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
                'label': 'Ionic \n exchange', 
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
                'label': 'Esterilization', 
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
    'name':'Extraction',
    'var': ['Var1','Var2'],
    'var_id':['Evar1','Evar2'],
    'initial':[1,2]
    },
    {'id':2,
    'name':'Ultrafiltration-UF1',
    'var': ['Var1','Var2','Var3'],
    'var_id':['UEvar1','UEvar2','UEvar3'],
    'initial':[1,2,3]
    },
     {'id':3,
    'name':'Ultrafiltration-UF2',
    'var': ['Var1','Var2'],
    'var_id':['U2Evar1','U2Evar2'],
    'initial':[1,2]
    },
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
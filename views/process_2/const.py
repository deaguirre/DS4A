

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
                'label': 'Proceso 1'
            },
            {
                'id':2,
                'label': 'Proceso 2'
            },
            {
                'id':3,
                'label': 'Proceso 3'
            }
        ],
        'edges':[
            {'id': '1-2', 'from':1, 'to':2},
            {'id': '2-3', 'from':2, 'to':3},
            
            
        ]
}
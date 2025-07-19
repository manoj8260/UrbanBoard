from urbanstay.models import Flat

PERMISSION_CONFIG = {
    'boarder' :{
        Flat : ['view',],      
    } ,
    'landlord' :{
        Flat :['view','add','change',]
    } ,    
}
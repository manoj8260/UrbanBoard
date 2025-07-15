from PG.models import PGlisting

PERMISSION_CONFIG = {
    'boarder' :{
        PGlisting : ['view',],
        
        
    } ,
    'landlord' :{
        PGlisting :['view','add','change',]
    } ,
    
}
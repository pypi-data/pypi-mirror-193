#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:02:59 2023

@author: lucas

New INPUTMAKER with a "dictionary to XML" structure 

"""
# %% Imports
from lxml import etree as et

# %% General functions
def dict2elem(d, head=None, text_mode=False):
    """ transform a dictionary to a etree.element
    
    Args:
        d (dict) dictionary with attributes in key:value format
        _format: {'head':str, attr1:value1, ..., 'Opes':[dicts, ]}   
        head (string) node for the etree.Element
        text_mode (bool) choose the output format, etree.Element or etree.tostring
        
    Return: 
        string format of the etree.Element if text_mode else the etree._Element
        
        E.g.
        
        _In: dict2elem({'head':'node', 'attr1':'value1', 'Opes':[{'Op_element':'op'}]}, text_mode=True)
        
        _Out: b'<node attr1="value1"/>' 
        
        # missing the operators part...
    """
    if not isinstance(d, dict):
        raise SyntaxError('Provide a dictionary to transform in a lxml element.')
    xml = et.Element(d['head']) if head==None else et.Element(head)
    # set the attributes of the lxml element removing the head and Operators part
    [xml.set(str(key), str(value)) for key, value in d.items() if key not in ('head', 'Opes')]

    return et.tostring(xml) if text_mode else xml

def printx(xmlelem):
    print(et.tostring(xmlelem, pretty_print=True).decode())

# %% Class functions
def hamilt_elem(propag, Hp):    
    # Create a lxml element to be appended to the self.propag 
    Hel = et.SubElement(propag, 'hamiltonian')
    # upper element of self.qdng
    if Hp['type'] == 'Sum':
        Hel.set('name', Hp['type'])
        # (Hel.append(dict2elem(melOpe) ) for melOpe in Hp['Mels']['Opes'] )
        for opes in Hp['Mels']['Opes']:
            Operator = et.SubElement(Hel, opes['head'])
            [Operator.set(str(key), str(value)) for key, value in opes.items() if key not in ('head','Opes')]
            # Hel.append( dict2elem(opes)) 

    elif Hp['type'] == 'Multistate':
        Hel.set('name', Hp['type'])
        if None == Hp['Mels']:
            raise SyntaxError('Include states for the Multistate hamiltonian!')
        else:
            for mel in Hp['Mels'][:]:
                if not mel:
                    pass
                else:
                    branch = et.SubElement(Hel, mel['head'])
                    [branch.set(str(key), str(value)) for key, value in mel.items() if key not in ('head','Opes')]

                    if 'Opes' in  mel.keys():
                        for ind in range(len(mel['Opes'])):
                            branch.append( dict2elem(mel['Opes'][ind])) 
    return Hel

def filterpost(filter_list):
    Filt = et.Element('filterpost')
    
    for dic in filter_list:
        [et.SubElement(Filt, str(opes), values) for opes, values in dic.items() 
         if not opes.startswith('m')]
        [et.SubElement(Filt.getchildren()[-1], str(opes), values) for opes, values in dic.items() 
          if opes.startswith('m')]
    return Filt

def wfun_elem(wfp):
    # wfel = et.SubElement(branch, 'wf', name=wfp['name'])
    # wfp = ['name', 'file', 'states', 'coeff2', 'normalize']
    if wfp['type'] == 'file':
        wfel = et.Element('wf')
        wfel.set('file', wfp['file'])
        
    elif wfp['type'] == 'LC':
        wfel = et.Element('wf', name=wfp['type'])
        if 'normalize' in wfp.keys() and wfp['normalize']: wfel.set('normalize', 'true')
        for ind in range(wfp['states']):
            wfstate = et.SubElement(wfel, 'wf'+str(ind))
            wfstate.set('file', wfp['file'][ind])
        
    elif wfp['type'] == 'Multistate':
        wfel = et.Element('wf', name=wfp['type'])
        wfel.set('states', str(wfp['states']))
        if 'normalize' in wfp.keys() and wfp['normalize']: wfel.set('normalize', 'true')
        # if wfp['states']!=len(wfp['file']): raise SyntaxError('number of states not equal to provided files!')
        for ii, index in enumerate(wfp['index']):
            wfstate = et.SubElement(wfel, 'wf'+str(index), file=str(wfp['file'][ii]))
            if 'coeff2' in wfp.keys(): wfstate.set('coeff2', wfp['coeff2'][ii])
        
    else:
        raise SyntaxError('Wvefunction type not defined.')
    return wfel

# %% Class
class InpXML:
    """ InpXMl class for the creation of a qdng calculation input in xml format.
    requires the lxml.etree package
    
    Args:
        qdng_params (dict) parameters for the qdng calculation
        _format: {attr1:value1, attr2:value2, ... }
        * qdng [ -d output directory] [-p cpus] <input file> [var1=val1] ... [varN=valN]
        
    Attributes:
        qdng (etree._Element) root of the lxml tree
        program (etree._Element) program body: 
            either propa or eigen
        propag (etree._Element) branch of a program
        hamilt (etree._Element) branch a propagation: 
            subelement required for a Cheby propagation
        wavefunc (etree._Element) wavefunction body: 
            inclusion of initial wavefunctions for the calculations
        
        
    * comments from QDng documentation
    """
        
    # %% Initiate the input layout 
    def __init__(self, qdng_params=None):
        # Root of the XML tree: self.qdng, with the tag-headline
        self.qdng = et.Element("qdng")
        # set the attributes for the root if qdng_params dict is provided
        if not qdng_params==None:
            for key, value in qdng_params.items():
                self.qdng.set(str(key), str(value))
      
    def __str__(self):
        return et.tostring(self.qdng, pretty_print=True).decode()
    
    def show(self):
        print(self)
    # %% Programs
    def program(self, ptype, program_params, wf_params):
        """ Main program for the calculation. Either propagation or eigenfunction derivation.
                
        Args:
            ptype (string) type of program:
            _either 'propa' or 'eigen'
            program_params (dict) program parameters dictionary:
            _format: {'dt':num, 'steps':num, 'directory':str,'Nef':num, 'conv':num }
            wf_params (dict) wavefunction parameters dictionary:
            _format: {'name':str, 'states':num, 'file':[strs, ], 'normalize':True or None}
            
        """
        # %% PROPA
        if not ptype in ['propa','eigen']:
            raise SyntaxError('Choose an appropriate program!')  
        # Make the self.program lxml element
        self.prog = dict2elem(program_params, ptype)
        # append to the root, qdng
        self.qdng.append( self.prog )
        
        # %% WAVEFUNCTION 
        if not wf_params:
            raise SyntaxError('Provide wavefunction parameters.')
        self.wavefunc = wfun_elem( wf_params) # save wavefunction part to be appended after propagation
        # self.prog.append(self.wavefunc) 
        
    # %% Operators
        # %% Propagator
    def propagation(self, name, hamilt_params):
        """ Method for the wavefunction propagation. Return a etree.SubElement of previous defined program.
        
        Args:
            name (string) name of the propagation method:
                *GSPO, Cheby, *SIL, *Arnoldi (*not defined yet)
            hamilt_params (dict) parameters dictionary for the required Cheby hamiltonian
            _format: {'type':hamiltonian type, 'Matrix_elems':[mij, ]} 
            _type in ('Sum', 'Multistate', )
            _matrix elements for multistate, see hamilt_elem() function for format
            
        """
        # Chebychev propagator
        if name == 'Cheby':# requires hamiltonian
            # create the propagator subelement of the program
            self.propag = et.SubElement(self.prog, 'propagator', name=name)
            # include the hamiltonian as a subelement of propag
            self.hamilt = hamilt_elem(self.propag, hamilt_params) 
            try:
                self.prog.append( self.wavefunc ) # append wavefunction after the propagation
            except:
                raise SyntaxError('Wavefunction was not properly defined for propa.')    
        else:
            raise SyntaxError('Propagator type not defined.')
        # others propagators
        
    def addfilter(self, ftype, params):
        
        if ftype == 'filterpost':
            if not isinstance(params, list):
                params = [params]
            self.prog.append(filterpost(params))
        
    def writexml(self, file_name='test_file', text=False):
        """ Write the constructed lxml element to a XML file.
        """
        tree = et.ElementTree(self.qdng)
        if file_name.endswith('.txt'): 
            text = not text 
            file_name = file_name.strip('.txt')
        tree.write(file_name + ('.txt' if text else '.xml'), pretty_print=True)
        
    
# %% Name == Main 
if __name__ == "__main__":
    
    # dt, steps = 20, 1000
    # propag, hamilt = 'Cheby', 'Sum'
    # Nef, conv = 20, 1e-9
    # name_T, name_V = "GridNablaSq", "GridPotential"
    # mass, pot_file = 2000, 'pot_Vg'
    # directory = 'efs_g'
    # wf_file = 'wfguess'
    # file_name='teste_dt_'
    # key = 'T'

    # nparams = {'dt':dt, 'steps':steps, 'directory':directory,'Nef':Nef, 'conv':conv }
   
    # T00 = {'head':'T', 'name':name_T, 'mass':mass, 'key':'T'}
    # V00 = {'head':'V', 'name':name_V, 'file':pot_file}
    # m00 = {'head':'m0.0', 'name':'Sum', 'Opes':[T00, V00]} 
    # T11 = {'head':'T', 'ref':'T'}
    # V11 = {'head':'V', 'name':name_V, 'file':pot_file}
    # m11 = {'head':'m1.1', 'name':'Sum', 'Opes':[T11, V11]} 
    # m10 = {'head':'m1.0', 'name':'GridDipole', 'file':'mu', 'laser':'Et', 'Opes':[]} 

    # Hparams = {'type':'Multistate', 'Mels':[m00,m11,m10]} 
    # Hsum = {'type':'Sum', 'Opes':[T00, V00]} 
    # WFparams = {'type':'Multistate', 'states':3, 'file':['ef'+str(i) for i in range(3)], 
    #             'normalize':True}
    # #%%
    # struct = InpXML()
    # struct.program('eigen', nparams, WFparams)
    # struct.propagation('Cheby', Hparams)
    # struct.writexml(text=True)
    # '''
    # # find if theres a way to obtain the simplified version in a text file
    # # put this script in a higher folder, to be easily accessed for other projects
    # '''
    
    # printx(struct.qdng)

    mCO = 1240 
    # printx(struct.qdng)
    eigpar = {'dt':1, 'steps':int(1000), 'dir':'efs_g', 'Nef':20, 'conv':1e-11 }

    T = {'head':'T', 'name':"GridNablaSq", 'mass':mCO}
    Vg = {'head':'V', 'name':"GridPotential", 'file':'pot_Vg'}
    Ve = {'head':'V', 'name':"GridPotential", 'file':'pot_Ve'}
    mel = {'head':'m0.0', 'name':'Sum', 'Opes':[T, Vg]}

    Hparams = {'type':'Sum', 'Mels':mel} 
    WFpar = {'type':'file', 'states':1, 'file':'wfguess', 'normalize':False}

    # eigx = InpXML()
    # eigx.program('eigen', eigpar, WFpar)
    # eigx.propagation('Cheby', Hparams)
    # eigx.show()
    #%% 
    propapar = {'dt': 0.165697, 'steps': 500, 'wcycle': 100, 'dir': 'propa_files', 'nfile': 'norm'}
    prop = InpXML()
    prop.program('propa', propapar, WFpar)
    prop.propagation('Cheby', Hparams)
    prop.addfilter('filterpost', {'expeconly':{'name':'Flux', 'int':'True'}})
    prop.show()

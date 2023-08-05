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
    # upper element of self.qdng
    if Hp['type'] == 'Sum':
        Hel = et.SubElement(propag, 'hamiltonian')
        Hel.set('name', Hp['type'])
        for ind in range(len(Hp['Opes'])):
            Hel.append(dict2elem(Hp['Opes'][ind]) )            

    elif Hp['type'] == 'Multistate':
        Hel = et.SubElement(propag, 'hamiltonian')
        Hel.set('name', Hp['type'])
        if None == Hp['Mels']:
            raise SyntaxError('Include states for the Multistate hamiltonian!')
        else:
            for mel in Hp['Mels']:
                if mel == {}:
                    pass
                else:
                    branch = et.SubElement(Hel, mel['head'])
                    [branch.set(str(key), str(value)) for key, value in mel.items() if key not in ('head','Opes')]

                    if 'Opes' in  mel.keys():
                        for ind in range(len(mel['Opes'])):
                            branch.append( dict2elem(mel['Opes'][ind])) 
    return Hel

def wfun_elem(qdng, wfp):
    wfel = et.SubElement(qdng, 'wf', name=wfp['name'])
    # wfp = ['name', 'file', 'states', 'coeff2', 'normalize']
    if wfp['name'] == 'file':
        wfel.set('file', wfp['file'])
        
    elif wfp['name'] == 'LC':
        if 'normalize' in wfp.keys() and wfp['normalize']: wfel.set('normalize', 'true')
        for ind in range(wfp['states']):
            wfstate = et.SubElement(wfel, 'wf'+str(ind))
            wfstate.set('file', wfp['file'][ind])
        
    elif wfp['name'] == 'Multistate':
        if 'normalize' in wfp.keys() and wfp['normalize']: wfel.set('normalize', 'true')
        # if wfp['states']!=len(wfp['file']): raise SyntaxError('number of states not equal to provided files!')
        for ind in range(len(wfp['file'])):
            wfstate = et.SubElement(wfel, 'wf'+str(ind), file=str(wfp['file'][ind]))
            if 'coeff2' in wfp.keys(): wfstate.set('coeff2', wfp['coeff2'][ind])
        
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
        self.wavefunc = wfun_elem(self.qdng, wf_params)
        
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
        else:
            raise SyntaxError('Propagator type not defined.')
        # others propagators
    
    def writexml(self, file_name='test', text=False):
        """ Write the constructed lxml element to a XML file.
        """
        file_name += ('.txt' if text else '.xml')
        (et.ElementTree(self.qdng)).write(file_name, pretty_print=True)
        # tree = et.ElementTree(self)
        # tree.write(file_name, pretty_print=True)
        # print(file_name)
        
    
# %% Name == Main 
if __name__ == "__main__":
    
    dt, steps = 20, 1000
    propag, hamilt = 'Cheby', 'Sum'
    Nef, conv = 20, 1e-9
    name_T, name_V = "GridNablaSq", "GridPotential"
    mass, pot_file = 2000, 'pot_Vg'
    directory = 'efs_g'
    wf_file = 'wfguess'
    key = 'T'

    nparams = {'dt':dt, 'steps':steps, 'directory':directory,'Nef':Nef, 'conv':conv }
   
    T00 = {'head':'T', 'name':name_T, 'mass':mass, 'key':'T'}
    V00 = {'head':'V', 'name':name_V, 'file':pot_file}
    m00 = {'head':'m0.0', 'name':'Sum', 'Opes':[T00, V00]} 
    T11 = {'head':'T', 'ref':'T'}
    V11 = {'head':'V', 'name':name_V, 'file':pot_file}
    m11 = {'head':'m1.1', 'name':'Sum', 'Opes':[T11, V11]} 
    m10 = {'head':'m1.0', 'name':'GridDipole', 'file':'mu', 'laser':'Et', 'Opes':[]} 

    Hparams = {'type':'Multistate', 'Mels':[m00,m11,m10]} 
    Hsum = {'type':'Sum', 'Opes':[T00, V00]} 
    WFparams = {'name':'Multistate', 'states':3, 'file':['ef'+str(i) for i in range(3)], 
                'normalize':True}
    #%%
    struct = InpXML()
    struct.program('eigen', nparams, WFparams)
    struct.propagation('Cheby', Hparams)
    struct.writexml()
    '''
    # find if theres a way to obtain the simplified version in a text file
    # put this script in a higher folder, to be easily accessed for other projects
    '''
    
    printx(struct.qdng)



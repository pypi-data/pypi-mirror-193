# Python package for making QDng calculations inputs

### Module:
- `inpxml.py`: **InpXML** class with methods designed for the creation of *xml* structures intended as input files for quantum chemistry calculations with QDng package. Requires *lxml*.
### Example: 

    propapar = {'dt': 0.165697, 'steps': 500, 'wcycle': 100, 'dir': 'propa_files', 'nfile': 'norm'}
    prop = InpXML()
    prop.program('propa', propapar, WFpar)
    prop.propagation('Cheby', Hparams)
    prop.addfilter('filterpost', {'expeconly':{'name':'Flux', 'int':'True'}})
    prop.show()

> Output:
`<qdng>`
`  <propa dt="0.165697" steps="500" wcycle="100" dir="propa_files" nfile="norm">`
`    <propagator name="Cheby">`
`      <hamiltonian name="Sum">`
`        <T name="GridNablaSq" mass="1240"/>`
`        <V name="GridPotential" file="pot_Vg"/>`
`      </hamiltonian>`
`    </propagator>`
`    <wf file="wfguess"/>`
`    <filterpost>`
`      <expeconly name="Flux" int="True"/>`
`    </filterpost>`
`  </propa>`
`</qdng>`

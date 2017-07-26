

testdata  = [
    (2, 5, 7),
    (0, 0, 0),
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_add(a, b, expected):
    assert rhf.add(a, b) == expected
    assert rhf.add(b, a) == expected
                                            

import psi4

def test_rhf():

    mol = psi4.geometry("""
    O
    H 1 1.1
    H 1 1.1 2 104
    symmetry c1
    """
    )

    bas = 'sto-3g'

    options = {'energy_conv' : 1.0e-6, 'density_conv' : 1.0e-6,'max_iter': 25,
                'diis' : 'off'} 

    molecule = rhf.Rhf(mol, bas, options)
    molecule.get_energy()                                           
    psi4.set_options({"scf_type": "pk"})
    psi4_energy = psi4.energy("SCF/"+ bas, molecule=mol)
    assert np.allclose(psi4_energy, molecule.E)


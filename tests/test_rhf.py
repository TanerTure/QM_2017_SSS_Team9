

testdata  = [
    (2, 5, 7),
    (0, 0, 0),
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_add(a, b, expected):
    assert rhf.add(a, b) == expected
    assert rhf.add(b, a) == expected
                                            

import psi4
import numpy as np

def test_rhf():
    """
    This function tests the rhf module without damping or diis
    """

    mol = psi4.geometry("""
    O
    H 1 1.1
    H 1 1.1 2 104
    symmetry c1
    """
    )

    bas = 'sto-3g'

    options = {'energy_conv' : 1.0e-6, 'density_conv' : 1.0e-6,'max_iter': 25,
                'diis' : 'off', 'damping' : 'off','nelec' : 10} 

    molecule = rhf.RHF(mol, bas, options)
    molecule.get_energy()                                           
    psi4.set_options({"scf_type": "pk"})
    psi4_energy = psi4.energy("SCF/"+ bas, molecule=mol)
    assert np.allclose(molecule.E, psi4_energy)

def test_rhf_damp():

    """
    This function tests the rhf module with damping
    """

    mol = psi4.geometry("""
    O
    H 1 1.1
    H 1 1.1 2 104
    symmetry c1
    """
    )

    bas = 'cc-pvtz'

    options = {'energy_conv' : 1.0e-6, 'density_conv' : 1.0e-6,'max_iter': 25,
                'diis' : 'off', 'nelec' : 10, 'damping': 'on', 'damping_start' : 5, 'damping_value' : 0.2}

    molecule = rhf.RHF(mol, bas, options)
    molecule.get_energy()                                           
    psi4.set_options({"scf_type": "pk"})
    psi4_energy = psi4.energy("SCF/"+ bas, molecule=mol)
<<<<<<< HEAD
    assert np.allclose(psi4_energy, molecule.E)

=======
    assert np.allclose(molecule.E, psi4_energy)
>>>>>>> fd7e8c57d955d4a8545431a6c238f5d47e163eac

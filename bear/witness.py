from .instance import shared_beard_instance

from bearbase.exceptions import WitnessDoesNotExistsException


class Witness(dict):
    """ Read data about a witness in the chain

        :param str witness: Name of the witness
        :param Beard beard_instance: Beard() instance to use when
        accessing a RPC

    """

    def __init__(self, witness, beard_instance=None):
        self.beard = beard_instance or shared_beard_instance()
        self.witness_name = witness
        self.witness = None
        self.refresh()

    def refresh(self):
        witness = self.beard.get_witness_by_account(self.witness_name)
        if not witness:
            raise WitnessDoesNotExistsException
        super(Witness, self).__init__(witness)

    def __getitem__(self, key):
        return super(Witness, self).__getitem__(key)

    def items(self):
        return super(Witness, self).items()

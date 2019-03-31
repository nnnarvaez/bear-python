import bear as stm
import sys

_shared_beard_instance = None


def get_config_node_list():
    from bearbase.storage import configStorage
    nodes = configStorage.get('nodes', None)
    if nodes:
        return nodes.split(',')


def shared_beard_instance():
    """ This method will initialize _shared_beard_instance and return it.
    The purpose of this method is to have offer single default Bear
    instance that can be reused by multiple classes.  """

    global _shared_beard_instance
    if not _shared_beard_instance:
        if sys.version >= '3.5':
            _shared_beard_instance = stm.beard.Beard(
                nodes=get_config_node_list())
        else:
            _shared_beard_instance = stm.Beard(
                nodes=get_config_node_list())
    return _shared_beard_instance


def set_shared_beard_instance(beard_instance):
    """ This method allows us to override default bear instance for all
    users of _shared_beard_instance.  """

    global _shared_beard_instance
    _shared_beard_instance = beard_instance

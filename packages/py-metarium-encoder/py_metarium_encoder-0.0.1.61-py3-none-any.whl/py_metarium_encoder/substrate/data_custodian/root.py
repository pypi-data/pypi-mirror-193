# Author: MetariumProject

# local libraries
from .base import SubstrateScribeUpdater


class SubstrateDataCustodianAdderAsRoot(SubstrateScribeUpdater):

    FUNCTION_CALL = "force_add_node_to_topic_custodian_set"


class SubstrateDataCustodianRemoverAsRoot(SubstrateScribeUpdater):

    FUNCTION_CALL = "force_remove_node_from_topic_custodian_set"
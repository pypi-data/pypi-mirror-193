from abc import ABC, abstractmethod

from ..ensemble.results import PartialResult


class ProgressionObserver(ABC):
    """
    The ProgressionObserver interface declares the onPartialResult method, called by the PEC Instance.
    It has available self.data wich is the dataset used for clustering as numpy matrix.
    It is useful for computing metrics such as, ClusteringMetrics.davies_bouldin_index(data, labels).
    """
    def __init__(self, sender, data, args):
        self._sender = sender
        self.data = data

    def _isEarlyTermination(self, previousResult, currentResult):
        if previousResult is not None and not isinstance(previousResult, PartialResult):
            raise RuntimeError(f'previousResult must be instance of PartialResult')
        if not isinstance(currentResult, PartialResult):
            raise RuntimeError(f'currentResult must be instance of PartialResult')

        iteration = currentResult.info.iteration
        if iteration > 0:
            et = self.earlyTerminationOccurs(iteration, previousResult, currentResult)
            if et is None:
                return False
            elif et is False:
                return False
            elif et is True:
                return True
            else:
                raise RuntimeError(f'earlyTerminationOccurs must return None, or a boolean')
        else:
            return False

    def _notifyPartialResult(self, previousResult, currentResult):
        """Called ONLY by the PEC instance"""
        if previousResult is not None and not isinstance(previousResult, PartialResult):
            raise RuntimeError(f'previousResult must be instance of PartialResult')
        if not isinstance(currentResult, PartialResult):
            raise RuntimeError(f'currentResult must be instance of PartialResult')

        iteration = currentResult.info.iteration
        self.onPartialResult(iteration, currentResult)

    @abstractmethod
    def earlyTerminationOccurs(self, iteration, previousResult, currentResult):
        """
        Receive the previousResult and the  currentResult, and must return a boolean (or None as False) indicating
        if the early termination occurs at the current iteration. The function is called, at each iteration,
        from the second one (iteration==1) because the first iteration (iteration==0) has not a previousResult.
        """
        pass

    @abstractmethod
    def onPartialResult(self, iteration, partialResult):
        """
        Receive a partialResult (instance of pec.PartialResult) and the current iteration number.
        Iterations start from 0.
        """
        pass


